'use strict';
var React = require('react');
var database = require('./databaseHook.js');
var WelcomeScreen = require('./WelcomeScreen.jsx');
var PlayerScreen = require('./PlayerScreen.jsx');
var playerdata = require('./playerdata');
var GameListScreen = require('./GameListScreen.jsx')
var GameDataScreen = require('./GameDataScreen.jsx')
var ZoneDataScreen = require('./ZoneDataScreen.jsx')

var CardGame = React.createClass({

	gotMessageCallback:function(reqNum, args){
		var output = this.refs.onScreen.handleMessage(reqNum, args);
		if(output != null)
			this.setState({currScreen: output});
		
	},

	getInitialState : function(){
		database.init(this.gotMessageCallback);
		// console.log(database.isopen);
		return {currScreen: "WelcomeScreen"};
	},

	render: function(){
		if(this.state.currScreen == "WelcomeScreen")
			return <WelcomeScreen ref="onScreen" />;
		if(this.state.currScreen == "PlayerScreen")
			return <PlayerScreen ref="onScreen" setParentState={this.setScreen} />;
		if(this.state.currScreen == "GameListScreen")
			return <GameListScreen ref="onScreen" setParentState={this.setScreen} />;
		if(this.state.currScreen == "GameData")
			return <GameDataScreen ref="onScreen" setParentState={this.setScreen} />;
		if(this.state.currScreen == "ZoneData")
			return <ZoneDataScreen ref="onScreen" />;
		return null
	},

	setScreen: function(str){
		this.setState({currScreen: str});
	},
});


module.exports = CardGame;