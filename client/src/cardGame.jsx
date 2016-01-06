
var Router = require('react-router').Router
var Route = require('react-router').Route
var Link = require('react-router').Link
var browserHistory = require('react-router').browserHistory 

var React = require('react');
var database = require('./databaseHook.js');
const WelcomeScreen = require('./WelcomeScreen.jsx');
const PlayerScreen = require('./PlayerScreen.jsx');
var playerdata = require('./playerdata');
var GameListScreen = require('./GameListScreen.jsx')
var GameDataScreen = require('./GameDataScreen.jsx')
var ZoneDataScreen = require('./ZoneDataScreen.jsx')
var ZoneSelectorScreen = require('./ZoneSelectorScreen.jsx')
var NewGameScreen = require('./NewGameScreen.jsx')

const CardGame = React.createClass({
  contextTypes: {
    router: React.PropTypes.object.isRequired
  },

	gotMessageCallback:function(reqNum, args){
		// var output = this.refs.onScreen.handleMessage(reqNum, args);

		console.log("Test 2")
		// if(this.props.children != null)
		// 	this.props.children.type.prototype.handleMessage(reqNum, args)
		// if(output != null){
		// 	this.setState({currScreen: output});
		// }
	},

	// getInitialState : function(){

	// 	return {currScreen: "WelcomeScreen"};
	// },
	componentDidMount: function(){
		database.init();
		if(this.props.route.path=="/")
			this.context.router.replace('/login')
	},
	render: function(){
		return <div>{this.props.children}</div>;
		// return (
		// 	<Router history={browserHistory}>
		// 		<Route path="/" component={WelcomeScreen} />
		// 		<Route path="/name" component={PlayerScreen} />
		// 	</Router>
		// 	)
		// if(this.state.currScreen == "WelcomeScreen")
		// 	return <WelcomeScreen ref="onScreen" />;
		// if(this.state.currScreen == "PlayerScreen")
		// 	return <PlayerScreen ref="onScreen" setParentState={this.setScreen} />;
		// if(this.state.currScreen == "GameListScreen")
		// 	return <GameListScreen ref="onScreen" setParentState={this.setScreen} />;
		// if(this.state.currScreen == "GameData")
		// 	return <GameDataScreen ref="onScreen" setParentState={this.setScreen} />;
		// if(this.state.currScreen == "ZoneData")
		// 	return <ZoneDataScreen ref="onScreen" setParentState={this.setScreen} />;
		// if(this.state.currScreen == "ZoneSelectorCardPlace")
		// 	return <ZoneSelectorScreen ref="onScreen" setParentState={this.setScreen} 
		// 		name="Place card where" zoneClicked={function(i){
		// 			database.sendRequest(1010, 
		// 				{posF: playerdata.selectedCard.pos, fromZ: playerdata.gameData[playerdata.zoneSelected].id, toZ:i, posT: 0}); 
		// 				this.setState({currScreen: "ZoneData"});
		// 			}.bind(this)} />;
		// if(this.state.currScreen == "ZoneSelectorTakeCard")
		// 	return <ZoneSelectorScreen ref="onScreen" setParentState={this.setScreen} 
		// 		name="Get card from where" zoneClicked={function(i){
		// 			database.sendRequest(1010, 
		// 				{posF: 0, fromZ: i, toZ:playerdata.gameData[playerdata.zoneSelected].id, posT: 0}); 
		// 				this.setState({currScreen: "ZoneData"});
		// 			}.bind(this)} />;
		// if(this.state.currScreen == "NewGameScreen")
		// 	return <NewGameScreen ref="onScreen" setParentState={this.setScreen} />;
		// return null
	},

	setScreen: function(str){
		this.setState({currScreen: str});
	},
});


module.exports = CardGame;