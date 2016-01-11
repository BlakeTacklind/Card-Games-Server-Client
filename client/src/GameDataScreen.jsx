'use strict';
var React = require('react');
var clientdata = require('./clientdata.js')
var database = require('./databaseHook.js')
var ZoneList = require('./ZoneList.jsx')
const Messages = require('./Messages.js')

var GameDataScreen = React.createClass({
  contextTypes: {
    router: React.PropTypes.object.isRequired
  },
  componentDidMount: function(){
    // console.log("change")
		database.sendRequest(Messages.GetGameData, {id: Number(window.sessionStorage.gameSelectedId)});
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
				<h1>{String(window.sessionStorage.gameSelectedName)}</h1>
				<ZoneList data={this.state.zones} zoneReq={this.requestZoneData} />
			</div>;
	},
});

module.exports = GameDataScreen;