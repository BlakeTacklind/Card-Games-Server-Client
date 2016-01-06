'use strict';
var React = require('react');
// var playerdata = require('./playerdata.js');
var database = require('./databaseHook.js')

//Handler for once logged in
//props: ID, username, display name, ?games list, ?friends
var PlayerScreen = React.createClass({
  contextTypes: {
    router: React.PropTypes.object.isRequired
  },
	handleMessage: function(reqNum, args){
		return null
	},
  componentDidMount: function(){
    // console.log("change")
    database.callback = this.handleMessage
  },
	render: function(){
		var name = (String(window.sessionStorage.displayname) == null) ? String(window.sessionStorage.username) : String(window.sessionStorage.displayname);
		return <div>
				<h1>{name}</h1>
				<button onClick={this.getGames}>Games</button>
			</div>;
	},
	getGames: function(){
		// this.props.setParentState("GameListScreen")
		this.context.router.push('/p/'+window.sessionStorage.username+'/games')
		//database.sendRequest(100, {id: playerdata.userid});
	},
});

module.exports = PlayerScreen;