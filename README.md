# Telegrach

Description coming soon.

## Getting Started

### Installing

Install dependencies for server 

```
cd server/  && 
virtualenv -p python3 venv && 
source venv/bin/activate && 
pip3 install -r requirements.txt
```

Install dependencies for client 

```
cd client/
npm install
```

## Configuration

Server configuration stores in following files:
- `server/.env` - general
- `server/.env.test` - for `testing` enviroment
- `server/.env.dev` - for `development` enviroment
- `server/.env.prod` - for `production` enviroment

Ensure that settings for MongoDB are correct.

## Development

Run server
```
cd server/ 
FLASK_ENV=development flask run 
```

Run front
```
cd client/ 
npm run serve
```

## Running the tests

```
cd server/
FLASK_ENV=testing flask test
```

## Deployment


Building frontend and put it into `server/public`
```
cd client/
npm run build
```

Then, run flask with static serving from `server/public/`
```
cd server/
FLASK_ENV=production flask run
```

## Authors

* **Alex Gorbov** - [foobic](https://github.com/foobic)
* **Vlad Novosadenko** - [v-lad](https://github.com/v-lad)
* **Oleksandr Zhinzher** - [foobic](https://github.com/alle-zhinzher)

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments
Inspired by telegra.ph.

