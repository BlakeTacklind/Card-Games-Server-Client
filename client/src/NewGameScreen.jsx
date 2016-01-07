'use strict';
var React = require('react');
var database = require('./databaseHook.js')
var GameTypeList = require('./GameTypeList.jsx')
var PlayersSelector = require('./PlayersSelector.jsx')

var NewGame = React.createClass({
	getInitialState : function(){
		this.playersSelected = [Number(window.sessionStorage.userid),]
		this.gameType = -1
    database.callback = this.handleMessage
		return {onList: "type"};
	},

	handleMessage: function(reqNum, args){
		this.refs.GamesList.handleMessage(reqNum, args)
		this.refs.PlayerList.handleMessage(reqNum, args)
	},
	render: function(){
		return <div>
				<h1>New Game</h1>
				<GameTypeList ref="GamesList" selection={this.selection}/>
				<PlayersSelector ref="PlayerList" handleChecked={this.handleChecked}/>
				<button>Finish and Name</button>
			</div>;
	},
	handleChecked: function(e, id){
		if(e.target.checked){
			this.playersSelected.push(id)
		}
		else{
			var index = this.playersSelected.indexOf(id)
			if(index > -1)
				this.playersSelected.splice(index, 1)
		}
		console.log(this.playersSelected)
	},
	selection: function(i){
		this.gameType = i;
	},
});

module.exports = NewGame;