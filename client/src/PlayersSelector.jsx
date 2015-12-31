'use strict';
var React = require('react');
var playerdata = require('./playerdata.js');
var database = require('./databaseHook.js')
var PlayerElement = require('./PlayerElement.jsx')

var GameTypeList = React.createClass({
	getInitialState : function(){
		database.sendRequest(170, {});
		playerdata.playersSelected = [Number(window.sessionStorage.userid),]
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

		var data = this.state.data.map(function(curr, i){
					if(curr.id != window.sessionStorage.userid)
						return {value: curr.id, label: curr.username}
				})
			

		return (
			<div>
				<button onClick={this.doneClicked}>Done</button>
				<form action="players">
					<div>
						<input type="checkbox" checked/>
						<PlayerElement data={{username:window.sessionStorage.username+" (Me)", displayname:window.sessionStorage.displayname+" (Me)", id:window.sessionStorage.userid}} key={-1} readOnly/>
					</div>
					{this.state.data.map(function(curr, i){
							if(curr.id == window.sessionStorage.userid)
								return null;
							return (
								<div>
									<input type="checkbox" value={"b"+i} name="player" key={"c"+i} onClick={function(e){this.handleChecked(e, curr.id)}.bind(this)}/>
									<PlayerElement data={curr} key={i}/>
								</div>)
						}.bind(this))
					}
				</form>
			</div>
		)
	},
	handleChecked: function(e, id){
		// console.log(id +" "+ e.target.checked)
		if(e.target.checked){
			playerdata.playersSelected.push(id)
		}
		else{
			var index = window.sessionStorage.playersSelected.indexOf(id)
			if(index > -1)
				playerdata.playersSelected.splice(index, 1)
		}
		console.log(playerdata.playersSelected)
	},
	doneClicked: function(){
		// console.log("1")
		this.props.setParentState("name")
		// console.log("2")
	},
});

module.exports = GameTypeList;