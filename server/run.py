from app import create_app
from flask_script import Manager
import os
import click
import sys
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv(".env")
if os.environ.get('FLASK_ENV') == 'production':
    load_dotenv('.env.prod')
elif os.environ.get('FLASK_ENV') == 'testing':
    load_dotenv('.env.test')
elif os.environ.get('FLASK_ENV') == 'development':
    load_dotenv('.env.dev')

app = create_app(os.environ.get('FLASK_CONFIG', 'development'))
manager = Manager(app)
CORS(app)

COV = None
if os.environ.get('FLASK_COVERAGE'):
    import coverage
    COV = coverage.coverage(branch=True, include='app/*')
    COV.start()


@app.cli.command()
@click.option('--coverage/--no-coverage', default=False, 
    help='Run tests under code coverage.')
def test(coverage):
    """Run the unit tests."""
    if coverage and not os.environ.get('FLASK_COVERAGE'):
        os.environ['FLASK_COVERAGE'] = '1'
        os.execvp(sys.executable, [sys.executable] + sys.argv) 
    import unittest

    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
    
    if COV:
        COV.stop()
        COV.save()
        print('Coverage Summary:')
        COV.report()
        basedir = os.path.abspath(os.path.dirname(__file__))
        covdir = os.path.join(basedir, 'tmp/coverage')
        COV.html_report(directory=covdir)
        print('HTML version: file://%s/index.html' % covdir)
        COV.erase()

if __name__ == "__main__":
    manager.run()

