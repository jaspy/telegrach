# Telegrach

Platform for creating, editing, viewing and deleting anonymous articles. Available feature to insert images and youtube-videos through markdown support.
Telegrach was written on Flask and VueJS. MongoDB was used as a database.

## Getting Started

### Requirements
- `node 10.15.1`
- `npm 6.4.1`
- `python3.6`
- `mongodb`

### Installing

First, install dependencies for server 

```
cd server  &&  
virtualenv -p python3.6 venv &&
source venv/bin/activate && 
pip3 install -r requirements.txt
```

Then, install dependencies for client 

```
cd client && 
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
cd server && 
FLASK_ENV=development flask run 
```
By default, server starts on `3000` port. You can change that in `server/.env`

Open new shell and run front
```
cd client && 
npm run serve
```

Check `localhost:8080` 

## Running the tests

```
cd server &&
FLASK_ENV=testing flask test
```

## Deployment

Before deploy, make sure that client has correct server host and port in `client/.env`.  

Build frontend and put it into `server/public`
```
cd client/
npm run build
```

And run flask in `production` mode which also provides static serving from `server/public/`
```
cd server/
FLASK_ENV=production flask run
```

## Authors

* **Alex Gorbov** - [foobic](https://github.com/foobic)
* **Vlad Novosadenko** - [v-lad](https://github.com/v-lad)
* **Oleksandr Zhinzher** - [alle-zhinzher](https://github.com/alle-zhinzher)

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments
Inspired by [telegra.ph](https://telegra.ph).

