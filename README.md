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

## TODO

- url -> variables (no magic strings)
- change List hold data as states instead of props
- better multithreading on server
- implement display name change
- implement delete game
- add reconnect (if disconnected)
- make url enquires work (new HTML server)
- add board (multi zone display)
- make connections more modular
- add css
- add chat
- add login tokens and passwords
- add cheat prevention (game rules)
- add friends system
- add filter for new game page

## To Learn

- better history management (certain variables also held in history)
- expose functions of children (react router). Used in message handleing
