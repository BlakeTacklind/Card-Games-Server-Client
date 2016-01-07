
var React = require('react');
var ZoneSelectorScreen = require('./ZoneSelectorScreen.jsx')
var playerdata = require('./playerdata.js')
var database = require('./databaseHook.js')

ZoneSelectorScreen.myName = "Place card into zone"
ZoneSelectorScreen.zoneClicked = function(i){
	database.sendRequest(1010, 
		{posF: playerdata.selectedCard.pos, fromZ: playerdata.gameData[playerdata.zoneSelected].id, toZ:i, posT: 0}); 
	this.context.router.goBack()
}

module.exports = React.createClass(ZoneSelectorScreen)