'use strict';
var React = require('react');
var database = require('./databaseHook.js')

//Handler for once logged in
var PlayerScreen = React.createClass({
  contextTypes: {
    router: React.PropTypes.object.isRequired
  },
	handleMessage: function(reqNum, args){
		return null
	},
  componentDidMount: function(){
    database.callback = this.handleMessage
  },
	render: function(){
		var name = (String(window.sessionStorage.displayname) == null) ? String(window.sessionStorage.username) : String(window.sessionStorage.displayname);
		return <div>
				<h1>{name}</h1>
				<button onClick={this.getGames}>Games</button>
				<button onClick={this.getNotifications}>Messages</button>
			</div>;
	},
	getGames: function(){
		this.context.router.push('/p/'+String(window.sessionStorage.username)+'/games')
	},
	getNotifications: function(){
		this.context.router.push('/p/'+String(window.sessionStorage.username)+'/messages')
	},
});

module.exports = PlayerScreen;