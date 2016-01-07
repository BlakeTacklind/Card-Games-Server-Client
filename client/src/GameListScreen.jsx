'use strict';
var React = require('react');
var clientdata = require('./clientdata.js');
var database = require('./databaseHook.js')
var GameList = require('./GameList.jsx')

var GameListScreen = React.createClass({
  contextTypes: {
    router: React.PropTypes.object.isRequired
  },
  componentDidMount: function(){
		database.sendRequest(100, {id: Number(window.sessionStorage.userid)});
    database.callback = this.handleMessage
  },
	requestGameData: function(id, name){
		this.context.router.push('/g/'+id)
		window.sessionStorage.gameSelectedId = id
		window.sessionStorage.gameSelectedName = name;
	},
	getInitialState : function(){
		return {games: clientdata.myGames};
	},

	handleMessage: function(reqNum, args){
		if (reqNum == 102)
			return null
		if (reqNum == 101){
			clientdata.myGames = args;
			this.setState({games: clientdata.myGames});
		}
		return null
	},
	render: function(){
		var name = (String(window.sessionStorage.displayname) == null) ? String(window.sessionStorage.username) : String(window.sessionStorage.displayname);
		return (<div>
				<h1>{name + "'s Games"}</h1>
				<button onClick={function(){this.context.router.push('/newgame')}.bind(this)}>New Game</button>
				<GameList data={this.state.games} gameReq={this.requestGameData} />
			</div>);
	},
});

module.exports = GameListScreen;