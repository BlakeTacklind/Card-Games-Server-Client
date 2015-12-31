'use strict';
var React = require('react');
var playerdata = require('./playerdata.js');
var database = require('./databaseHook.js')
var GameTypeList = require('./GameTypeList.jsx')
var PlayersSelector = require('./PlayersSelector.jsx')
var NameGame = require('./NameGame.jsx')

var NewGame = React.createClass({
	getInitialState : function(){
		// database.sendRequest(100, {id: Number(window.sessionStorage.userid)});
		// console.log(database.isopen);
		return {onList: "type"};
	},

	handleMessage: function(reqNum, args){
		// console.log("test 1")
		// if (reqNum == 102)
		// 	return null
		// if (reqNum == 101){
		// 	// console.log("test 2")
		// 	playerdata.games = args;
		// 	this.setState({games: playerdata.games});
		// }
		return this.refs.currList.handleMessage(reqNum, args)
	},
	render: function(){
		var List;
		if(this.state.onList == "type")
			List = <GameTypeList ref="currList" setParentState={this.setParentState}/>
		else if(this.state.onList == "player")
			List = <PlayersSelector ref="currList" setParentState={this.setParentState}/>
		else if(this.state.onList == "name")
			List = <NameGame ref="currList" setParentState={this.props.setParentState} />

		return <div>
				<h1>New Game</h1>
				{List}
			</div>;
	},
	setParentState: function(state){
		this.setState({onList: state})
	}
});

module.exports = NewGame;