var React = require('react');
var clientdata = require('./clientdata.js');
var database = require('./databaseHook.js')
var CardList = require('./CardList.jsx')
var B4C = require('./ButtonsForCards.jsx')

var ZoneDataScreen = React.createClass({
  contextTypes: {
    router: React.PropTypes.object.isRequired
  },
  componentDidMount: function(){
    database.callback = this.handleMessage
		database.sendRequest(210, {id: Number(window.sessionStorage.zoneSelectedId)});
  },
	getInitialState : function(){
		return {cards: null};
	},

	handleMessage: function(reqNum, args){
		if (reqNum == 212)
			return null
		if (reqNum == 211){
			clientdata.cards = args;
			this.setState({cards: clientdata.cards});
		}
		return null
	},
	render: function(){
		return <div>
				<h1>{String(window.sessionStorage.gameSelectedName)} - {String(window.sessionStorage.zoneSelectedName)}</h1>
				<B4C ref="buttons" router={this.context.router}/>
				<CardList data={this.state.cards} clicked={this.moveCardToZone}/>
			</div>;
	},
	moveCardToZone: function(i){
		if(this.refs.buttons.getSelectedState()){
			this.context.router.push('/zones/place')
		}
	},
});

module.exports = ZoneDataScreen;