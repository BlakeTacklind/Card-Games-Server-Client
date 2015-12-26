'use strict';
var React = require('react');
var playerdata = require('./playerdata.js');
var database = require('./databaseHook.js')

//Handler for once logged in
//props: ID, username, display name, ?games list, ?friends
var PlayerScreen = React.createClass({
	getInitialState : function(){
		database.sendRequest(100, {id: playerdata.userid});
		// console.log(database.isopen);
		return {};
	},

	handleMessage: function(reqNum, args){
		return null
	},
	render: function(){
		return <div>
				<h1>{playerdata.name() + "'s Games"}</h1>
			</div>;
	},
});

module.exports = PlayerScreen;