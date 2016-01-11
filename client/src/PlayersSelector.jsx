'use strict';
var React = require('react');
var database = require('./databaseHook.js')
var PlayerElement = require('./PlayerElement.jsx')
const Messages = require('./Messages.js')

var GameTypeList = React.createClass({
	getInitialState : function(){
		database.sendRequest(Messages.GetAllOtherPlayers, {});
		
		return {data: null};
	},

	handleMessage: function(reqNum, args){
		if (reqNum == Messages.GetAllOtherPlayersFail)
			return null
		if (reqNum == Messages.GetAllOtherPlayersSuccess){
			this.setState({data: args})
		}
		return null
	},
	render: function(){
		if(this.state.data == null)
			return null

		return (<form action="players">
				<div>
					<input type="checkbox" checked/>
					<PlayerElement data={{username: String(window.sessionStorage.username)+" (Me)", displayname: String(window.sessionStorage.displayname)+" (Me)", id:Number(window.sessionStorage.userid)}} key={-1} readOnly/>
				</div>
				{this.state.data.map(function(curr, i){
						if(curr.id == window.sessionStorage.userid)
							return null;
						return (
							<div>
								<input type="checkbox" value={"b"+i} name="player" key={"c"+i} onClick={function(e){this.props.handleChecked(e, curr.id)}.bind(this)}/>
								<PlayerElement data={curr} key={i}/>
							</div>)
					}.bind(this))
				}
			</form>
		)
	},
});

module.exports = GameTypeList;