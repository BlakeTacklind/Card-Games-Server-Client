'use strict';
var React = require('react');
var clientdata = require('./clientdata.js');
var database = require('./databaseHook.js')
var GameList = require('./GameList.jsx')
const Messages = require('./Messages.js')

var GameListScreen = React.createClass({
  contextTypes: {
    router: React.PropTypes.object.isRequired
  },
  componentDidMount: function(){
		database.sendRequest(Messages.GetGameList, {id: Number(window.sessionStorage.userid)});
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
		if (reqNum == Messages.GetGameListFail)
			return null
		if (reqNum == Messages.GetGameListSuccess){
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