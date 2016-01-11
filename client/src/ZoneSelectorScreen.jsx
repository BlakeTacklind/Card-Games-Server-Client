'use strict';
var React = require('react');
var clientdata = require('./clientdata.js');
var database = require('./databaseHook.js')
const Messages = require('./Messages.js')
var ZoneList = require('./ZoneList.jsx')

var ZoneSelector = {
  contextTypes: {
    router: React.PropTypes.object.isRequired
  },
  componentDidMount: function(){
		database.sendRequest(Messages.GetGameData, {id: Number(window.sessionStorage.gameSelectedId)});
    database.callback = this.handleMessage
  },
	getInitialState : function(){
		return {zones: clientdata.zoneList};
	},

	handleMessage: function(reqNum, args){
		if (reqNum == Messages.GetGameDataFail)
			return null
		if (reqNum == Messages.GetGameDataSuccess){
			clientdata.zoneList = args;
			this.setState({zones: clientdata.zoneList});
		}
		return null
	},
	render: function(){
		return <div>
				<h1>{this.myName}</h1>
				<ZoneList data={this.state.zones} zoneReq={this.zoneClicked} />
			</div>;
	},
};

module.exports = ZoneSelector;