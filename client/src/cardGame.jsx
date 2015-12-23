'use strict';
var React = require('react');
var database = require('./databaseHook.js');
var WelcomeScreen = require('./WelcomeScreen.jsx');
var PlayerScreen = require('./PlayerScreen.jsx');
var playerdata = require('./playerdata');


var CardGame = React.createClass({

	gotMessageCallback:function(reqNum, args){
		console.log(reqNum);
		console.log(args);
		if(reqNum == 11){
			playerdata.userid = args[0];
			playerdata.username = args[1];
			playerdata.displayname = args[2];
			this.setState({status: 1});
			console.log("changed state")
		}
	},

	getInitialState : function(){
		database.init(this.gotMessageCallback);
		// console.log(database.isopen);
		return {status: 0};
	},

	render: function(){
		if(this.state.status == 0){
			return <WelcomeScreen />;
		}
		if(this.state.status == 1){
			return <PlayerScreen username = {playerdata.username}/>;
		}
	},

	// sendMessage: function(){
	// 	database.sendRequest(10, ["Bob"]);
	// },
});


module.exports = CardGame;