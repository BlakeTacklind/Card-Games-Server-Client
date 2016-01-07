var React = require('react');
var playerdata = require('./playerdata.js');
var database = require('./databaseHook.js')
var CardList = require('./CardList.jsx')
var B4C = require('./ButtonsForCards.jsx')

var ZoneDataScreen = React.createClass({
  contextTypes: {
    router: React.PropTypes.object.isRequired
  },
  componentDidMount: function(){
		database.sendRequest(210, {id: playerdata.gameData[playerdata.zoneSelected].id});
    console.log("change")
    database.callback = this.handleMessage
  },
	getInitialState : function(){
		// console.log("sending "+playerdata.gameData[playerdata.zoneSelected].id);
		return {cards: null};
	},

	handleMessage: function(reqNum, args){
		// console.log("test 1")
		if (reqNum == 212)
			return null
		if (reqNum == 211){
			// console.log("Args: " + args)
			playerdata.zoneData = args;
			this.setState({cards: playerdata.zoneData});
		}
		return null
	},
	render: function(){
		return <div>
				<h1>{playerdata.games[playerdata.selGame].name} - {playerdata.gameData[playerdata.zoneSelected].name}</h1>
				<B4C ref="buttons" router={this.context.router}/>
				<CardList data={this.state.cards} clicked={this.moveCardToZone}/>
			</div>;
	},
	moveCardToZone: function(){
		if(this.refs.buttons.getSelectedState()){
			this.context.router.push('/zones/place')
			// this.props.setParentState("ZoneSelectorCardPlace")
		}
	},
});

module.exports = ZoneDataScreen;