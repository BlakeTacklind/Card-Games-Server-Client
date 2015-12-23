'use strict';
var React = require('react');


var database = require('./databaseHook.js')


var CardGame = React.createClass({

	getInitialState : function(){
		// console.log(database.isopen);
		return null;
	},

	render: function(){
		return <div><h1>HAHA</h1><button onClick={this.sendMessage}>Test</button></div>;
	},

	sendMessage: function(){
		database.init();
		console.log(database.isopen);
	},
});


module.exports = CardGame;