'use strict';
var React = require('react');
var clientdata = require('./clientdata.js')
var database = require('./databaseHook.js')
var ZoneList = require('./ZoneList.jsx')

var GameDataScreen = React.createClass({
  contextTypes: {
    router: React.PropTypes.object.isRequired
  },
  componentDidMount: function(){
    // console.log("change")
		database.sendRequest(120, {id: Number(window.sessionStorage.gameSelectedId)});
    database.callback = this.handleMessage
  },
	requestZoneData: function(id, name){
		window.sessionStorage.zoneSelectedId = id;
		window.sessionStorage.zoneSelectedName = name;

		this.context.router.push('/z/'+id)
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
				<h1>{String(window.sessionStorage.gameSelectedName)}</h1>
				<ZoneList data={this.state.zones} zoneReq={this.requestZoneData} />
			</div>;
	},
});

module.exports = GameDataScreen;