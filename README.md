# Card-Games-Server-Client

This is a personnal project to enable the playing of any card game with other people accross web devices

## General structure

### postgres database

not included in this repo (yet)

### database frontend - python
Found in: database/

manages queries to the postgres database and incoming websocket connections
Set up:
```
> python setup.py
```

Run with:
```
> python server.py
```

### html server - express - javascript
Found in: client/

Handles serving html files
Set up:
```
> npm install
```

Run with:
```
> node server.js
```
(must have webpacked items initially)

### html client files
Found in: client/

Handles serving html files
Set up:
```
> npm install
> webpack
```

visit page: [http://localhost:8081](http://localhost:8081)
