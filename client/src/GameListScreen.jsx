'use strict';
var React = require('react');
var playerdata = require('./playerdata.js');
var database = require('./databaseHook.js')
var GameList = require('./GameList.jsx')

var GameListScreen = React.createClass({
	requestGameData: function(i){
		this.props.setParentState("GameData")
		// console.log("sending request "+i)
		database.sendRequest(120, {id: i})

	},
	getInitialState : function(){
		database.sendRequest(100, {id: Number(window.sessionStorage.userid)});
		// console.log(database.isopen);
		return {games: null};
	},

	handleMessage: function(reqNum, args){
		if (reqNum == 102)
			return null
		if (reqNum == 101){
			// console.log("test 2")
			playerdata.games = args;
			this.setState({games: playerdata.games});
		}
		return null
	},
	render: function(){
		var name = (String(window.sessionStorage.displayname) == null) ? String(window.sessionStorage.username) : String(window.sessionStorage.displayname);
		return <div>
				<h1>{name + "'s Games"}</h1>
				<button onClick={function(){this.props.setParentState("NewGameScreen")}.bind(this)}>New Game</button>
				<GameList data={this.state.games} gameReq={this.requestGameData} />
			</div>;
	},
});

module.exports = GameListScreen;