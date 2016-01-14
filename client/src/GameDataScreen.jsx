'use strict';
var React = require('react');
var clientdata = require('./clientdata.js')
var database = require('./databaseHook.js')
var ZoneList = require('./ZoneList.jsx')
const Messages = require('./Messages.js')
var DealList = require('./DealList.jsx')

var GameDataScreen = React.createClass({
  contextTypes: {
    router: React.PropTypes.object.isRequired
  },
  componentDidMount: function(){
		database.sendRequest(Messages.GetGameData, {id: Number(window.sessionStorage.gameSelectedId)});
    database.callback = this.handleMessage
  },
	requestZoneData: function(id, name, owner){
		var go = true;
		if(owner != Number(window.sessionStorage.userid)){
			go = confirm("This might be cheating")
		}

		if(go){
			window.sessionStorage.zoneSelectedId = id;
			window.sessionStorage.zoneSelectedName = name;
	
			this.context.router.push('/z/'+id)
		}
	},
	dealZone: function(id){
		window.sessionStorage.zoneSelectedId = id;
		this.zonesSelected=[];

		this.setState({dealing: true})
	},
	cancelDeal: function(){
		this.zonesSelected=[];

		this.setState({dealing: false})
	},
	getInitialState : function(){
		return {zones: clientdata.zoneList, dealing:false};
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
	handleChecked: function(e, id){
		if(e.target.checked){
			this.zonesSelected.push(id)
		}
		else{
			var index = this.zonesSelected.indexOf(id)
			if(index > -1)
				this.zonesSelected.splice(index, 1)
		}
		console.log(this.zonesSelected)
	},
	dealFinished: function(num){
		database.sendRequest(Messages.DealCardsRQ, {fromZ: Number(window.sessionStorage.zoneSelectedId), toZarr: this.zonesSelected, num})
		// console.log({fromZ: Number(window.sessionStorage.zoneSelectedId), toZarr: this.zonesSelected, num})
		this.setState({dealing: false})
	},
	render: function(){
		if(this.state.dealing){
			return <div>
					<h1>{String(window.sessionStorage.gameSelectedName)}</h1>
					<DealList data={this.state.zones} cancel={this.cancelDeal} handleChecked={this.handleChecked} doneDeal={this.dealFinished}/>
				</div>;
		}
		else{
			return <div>
					<h1>{String(window.sessionStorage.gameSelectedName)}</h1>
					<ZoneList data={this.state.zones} zoneReq={this.requestZoneData} dealZone={this.dealZone} />
				</div>;
		}
	},
});

module.exports = GameDataScreen;