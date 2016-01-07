
var React = require('react');
var ZoneSelectorScreen = require('./ZoneSelectorScreen.jsx')
var database = require('./databaseHook.js')

ZoneSelectorScreen.myName = "Take top card from zone:"
ZoneSelectorScreen.zoneClicked = function(i, n){
	database.sendRequest(1010, {
		posF: 0, 
		fromZ: i, 
		toZ: Number(window.sessionStorage.zoneSelectedId), 
		posT: 0
	}); 

	this.context.router.replace('/z/'+Number(window.sessionStorage.zoneSelectedId))
}

module.exports = React.createClass(ZoneSelectorScreen)