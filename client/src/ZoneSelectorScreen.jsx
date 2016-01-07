'use strict';
var React = require('react');
var clientdata = require('./clientdata.js');
var database = require('./databaseHook.js')
var ZoneList = require('./ZoneList.jsx')

var ZoneSelector = {
  contextTypes: {
    router: React.PropTypes.object.isRequired
  },
  componentDidMount: function(){
		database.sendRequest(120, {id: Number(window.sessionStorage.gameSelectedId)});
    database.callback = this.handleMessage
  },
	getInitialState : function(){
		return {zones: clientdata.zoneList};
	},

	handleMessage: function(reqNum, args){
		if (reqNum == 122)
			return null
		if (reqNum == 121){
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