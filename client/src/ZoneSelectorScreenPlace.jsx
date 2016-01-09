
var React = require('react');
var ZoneSelectorScreen = require('./ZoneSelectorScreen.jsx')
var database = require('./databaseHook.js')

ZoneSelectorScreen.myName = "Place card into zone"
ZoneSelectorScreen.zoneClicked = function(i, n){
	database.sendRequest(1010, {
			posF: Number(window.sessionStorage.cardPosition), 
			fromZ: Number(window.sessionStorage.zoneSelectedId), 
			toZ:i, 
			posT: 0
		}); 
	window.sessionStorage.cardPosition = -1
	this.context.router.replace('/z/'+Number(window.sessionStorage.zoneSelectedId))
}

module.exports = React.createClass(ZoneSelectorScreen)