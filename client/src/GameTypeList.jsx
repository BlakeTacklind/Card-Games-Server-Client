'use strict';
var React = require('react');
var playerdata = require('./playerdata.js');
var database = require('./databaseHook.js')
var GameTypeElement = require('./GameTypeElement.jsx')

var GameTypeList = React.createClass({
	getInitialState : function(){
		database.sendRequest(160, {});
		// console.log(database.isopen);
		return {data: null};
	},

	handleMessage: function(reqNum, args){
		if (reqNum == 162)
			return null
		if (reqNum == 161){
			console.log("got message")
			this.setState({data: args})
		}
		return null
	},
	render: function(){
		if(this.state.data == null){
			console.log("state is null")
			return null
		}
		return (<div>
			{this.state.data.map(function(curr, i){
					return <GameTypeElement data={curr} key={i} clicked={function(){window.sessionStorage.selGameType=curr; this.props.setParentState("player")}.bind(this)}/>
				}.bind(this))
			}
			</div>
		)
	},
});

module.exports = GameTypeList;