'use strict';
var React = require('react');
var playerdata = require('./playerdata.js');
var database = require('./databaseHook.js')
var PlayerElement = require('./PlayerElement.jsx')
var CheckBoxList = require('react-checkbox-list'); 

var GameTypeList = React.createClass({
	getInitialState : function(){
		database.sendRequest(170, {});
		// console.log(database.isopen);
		return {data: null};
	},

	handleMessage: function(reqNum, args){
		if (reqNum == 172)
			return null
		if (reqNum == 171){
			this.setState({data: args})
		}
		return null
	},
	render: function(){
		// var Me = {username:window.sessionStorage.username+" (Me)", displayname:window.sessionStorage.displayname, id:window.sessionStorage.userid};
		if(this.state.data == null)
			return null

		// var data = {this.state.data.map(function(curr, i){
		// 			if(curr.id != window.sessionStorage.userid)
		// 				return {value: curr.username,}<div>
		// 					<input type="checkbox" value={"box"+i} name="player" key={"c"+i} onChange={function(){console.log(this.checked)}}/>
		// 					<PlayerElement data={curr} key={i}/>
		// 				</div>
		// 		}.bind(this))
		// 	}

		return (<div>
			<button onClick={this.doneClicked}>Done</button>
			<form action="players">
			<div>
				<input type="checkbox" value={"box"} name={"Me"} checked/>
				<PlayerElement data={{username:window.sessionStorage.username+" (Me)", displayname:window.sessionStorage.displayname+" (Me)", id:window.sessionStorage.userid}} key={-1} readOnly/>
			</div>
			{this.state.data.map(function(curr, i){
					if(curr.id == window.sessionStorage.userid)
						return null;
					return <div>
						<input type="checkbox" value={"box"+i} name="player" key={"c"+i} onChange={function(){console.log(this.checked)}}/>
						<PlayerElement data={curr} key={i}/>
					</div>
				}.bind(this))
			}
			</form>
			</div>
		)
	},
	doneClicked: function(){

	},
});

module.exports = GameTypeList;