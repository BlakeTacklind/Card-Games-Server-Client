'use strict';
var React = require('react');
var playerdata = require('./playerdata.js');
var database = require('./databaseHook.js')
var ZoneList = require('./ZoneList.jsx')

var GameDataScreen = React.createClass({
	requestZoneData: function(i){
		playerdata.zoneSelected = i;
		this.props.setParentState("ZoneData")
		// console.log("sending request "+i)
		// database.sendRequest(210, {id: i})

	},
	getInitialState : function(){
		// database.sendRequest(120, {id: playerdata.userid});
		// console.log(database.isopen);
		return {zones: null};
	},

	handleMessage: function(reqNum, args){
		// console.log("test 1")
		if (reqNum == 122)
			return null
		if (reqNum == 121){
			// console.log("test 2")
			playerdata.gameData = args;
			this.setState({zones: playerdata.gameData});
		}
		return null
	},
	render: function(){
		return <div>
				<h1>{playerdata.games[playerdata.selGame].name}</h1>
				<ZoneList data={this.state.zones} zoneReq={this.requestZoneData} />
			</div>;
	},
});

module.exports = GameDataScreen;