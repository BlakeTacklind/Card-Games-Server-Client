
var React = require('react');
var ZoneSelectorScreen = require('./ZoneSelectorScreen.jsx')
const Messages = require('./Messages.js')
var database = require('./databaseHook.js')

ZoneSelectorScreen.myName = "Take top card from zone:"
ZoneSelectorScreen.zoneClicked = function(i, n){
	database.sendRequest(Messages.MoveCardRQ, {
		posF: 0, 
		fromZ: i, 
		toZ: Number(window.sessionStorage.zoneSelectedId), 
		posT: 0
	}); 

	this.context.router.replace('/z/'+Number(window.sessionStorage.zoneSelectedId))
}

module.exports = React.createClass(ZoneSelectorScreen)