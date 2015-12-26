'use strict';
var React = require('react');
var database = require('./databaseHook.js');
var WelcomeScreen = require('./WelcomeScreen.jsx');
var PlayerScreen = require('./PlayerScreen.jsx');
var playerdata = require('./playerdata');
var GameListScreen = require('./GameListScreen.jsx')


var CardGame = React.createClass({

	gotMessageCallback:function(reqNum, args){
		// console.log(reqNum);
		// console.log(args);
		var output = this.refs.onScreen.handleMessage(reqNum, args);
		if(output != null)
			this.setState({currScreen: output});
		// this.setState({currScreen: this.state.handler(reqNum, args)});
		// if(reqNum == 11){
		// 	playerdata.userid = args['id'];
		// 	playerdata.username = args['username'];
		// 	playerdata.displayname = args['displayname'];
		// 	this.setState({currScreen: <PlayerScreen username = {playerdata.username}/>});
		// 	console.log("changed state")
		// }
		
	},

	getInitialState : function(){
		database.init(this.gotMessageCallback);
		// console.log(database.isopen);
		return {currScreen: "WelcomeScreen"};
	},

	render: function(){
		// return this.state.currScreen;
		if(this.state.currScreen == "WelcomeScreen"){
			return <WelcomeScreen ref="onScreen" />;
		}
		if(this.state.currScreen == "PlayerScreen"){
			return <PlayerScreen ref="onScreen" />;
		}
		if(this.state.currScreen == "GameListScreen")
			return <GameListScreen ref="onScreen" />
	},

	// sendMessage: function(){
	// 	database.sendRequest(10, ["Bob"]);
	// },
});


module.exports = CardGame;