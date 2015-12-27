'use strict';
var React = require('react');
var database = require('./databaseHook.js');
var WelcomeScreen = require('./WelcomeScreen.jsx');
var PlayerScreen = require('./PlayerScreen.jsx');
var playerdata = require('./playerdata');
var GameListScreen = require('./GameListScreen.jsx')
var GameDataScreen = require('./GameDataScreen.jsx')
var ZoneDataScreen = require('./ZoneDataScreen.jsx')
var ZoneSelectorScreen = require('./ZoneSelectorScreen.jsx')

var CardGame = React.createClass({

	gotMessageCallback:function(reqNum, args){
		var output = this.refs.onScreen.handleMessage(reqNum, args);
		if(output != null){
			// playerdata.onWin = output;
			this.setState({currScreen: output});
		}
	},

	getInitialState : function(){
		database.init(this.gotMessageCallback);
		// if(typeof(window.localStorage) !== "undefined"){
		// 	console.log("Works")
		// }
		// else{
		// 	console.log("Doesn't works")
		// }
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
			return <ZoneDataScreen ref="onScreen" setParentState={this.setScreen} />;
		if(this.state.currScreen == "ZoneSelectorCardPlace")
			return <ZoneSelectorScreen ref="onScreen" setParentState={this.setScreen} 
				name="Place card where" zoneClicked={function(i){
					database.sendRequest(1010, 
						{posF: playerdata.selectedCard.pos, fromZ: playerdata.gameData[playerdata.zoneSelected].id, toZ:i, posT: 0}); 
						this.setState({currScreen: "ZoneData"});
					}.bind(this)} />;
		if(this.state.currScreen == "ZoneSelectorTakeCard")
			return <ZoneSelectorScreen ref="onScreen" setParentState={this.setScreen} 
				name="Get card from where" zoneClicked={function(i){
					database.sendRequest(1010, 
						{posF: 0, fromZ: i, toZ:playerdata.gameData[playerdata.zoneSelected].id, posT: 0}); 
						this.setState({currScreen: "ZoneData"});
					}.bind(this)} />;
		return null
	},

	setScreen: function(str){
		this.setState({currScreen: str});
	},
});


module.exports = CardGame;