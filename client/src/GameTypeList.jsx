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
			this.setState({data: args})
		}
		return null
	},
	render: function(){
		if(this.state.data == null)
			return null
		return (<div>
			{this.state.data.map(function(curr, i){
					return <GameTypeElement data={curr} key={i} clicked={function(){window.sessionData.selGameType=curr}}/>
				}.bind(this))
			}
			</div>
		)
	},
});

module.exports = GameTypeList;