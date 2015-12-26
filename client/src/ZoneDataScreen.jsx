'use strict';
var React = require('react');
var playerdata = require('./playerdata.js');
var database = require('./databaseHook.js')
var CardList = require('./CardList.jsx')

var ZoneDataScreen = React.createClass({
	// requestZoneData: function(i){
	// 	this.props.setParentState("ZoneData")
	// 	// console.log("sending request "+i)
	// 	database.sendRequest(210, {id: i})

	// },
	getInitialState : function(){
		// console.log("sending "+playerdata.gameData[playerdata.zoneSelected].id);
		database.sendRequest(210, {id: playerdata.gameData[playerdata.zoneSelected].id});
		return {cards: null};
	},

	handleMessage: function(reqNum, args){
		// console.log("test 1")
		if (reqNum == 212)
			return null
		if (reqNum == 211){
			// console.log("Args: " + args)
			playerdata.zoneData = args;
			this.setState({cards: playerdata.zoneData});
		}
		return null
	},
	render: function(){
		return <div>
				<h1>{playerdata.games[playerdata.selGame].name} - {playerdata.gameData[playerdata.zoneSelected].name}</h1>
				<CardList data={this.state.cards} />
			</div>;
	},
});

module.exports = ZoneDataScreen;