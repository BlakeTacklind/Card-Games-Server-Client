'use strict';
var React = require('react');
var playerdata = require('./playerdata.js');
var database = require('./databaseHook.js')

//Handler for once logged in
//props: ID, username, display name, ?games list, ?friends
var PlayerScreen = React.createClass({
	render: function(){
		return <div><h1>{this.props.username}</h1><button onClick={this.getGames}>Games</button></div>;
	},

	getGames: function(){
		database.sendRequest(100, [playerdata.userid]);
	},
});

module.exports = PlayerScreen;