
var React = require('react');
var ZoneSelectorScreen = require('./ZoneSelectorScreen.jsx')

ZoneSelectorScreen.myName = "Take top card from zone:"
ZoneSelectorScreen.zoneClicked = function(){
	console.log("take")
}

module.exports = React.createClass(ZoneSelectorScreen)