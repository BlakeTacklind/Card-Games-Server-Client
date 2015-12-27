'use strict';
var React = require('react');
var playerdata = require('./playerdata.js');
var database = require('./databaseHook.js')
var ZoneList = require('./ZoneList.jsx')

var ZoneSelector = React.createClass({
	// zoneClicked: function(i){

	// 	this.props.setParentState("ZoneData")
	// },
	getInitialState : function(){
		database.sendRequest(120, {id: playerdata.userid});
		// console.log(database.isopen);
		return {zones: playerdata.gameData};
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
				<h1>{this.props.name}</h1>
				<ZoneList data={this.state.zones} zoneReq={this.props.zoneClicked} />
			</div>;
	},
});

module.exports = ZoneSelector;