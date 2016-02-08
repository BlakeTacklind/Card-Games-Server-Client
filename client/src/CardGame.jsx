
// var Router = require('react-router').Router
// var Route = require('react-router').Route
// var Link = require('react-router').Link
var browserHistory = require('react-router').browserHistory 

var React = require('react');
var database = require('./databaseHook.js');
// const WelcomeScreen = require('./WelcomeScreen.jsx');
// const PlayerScreen = require('./PlayerScreen.jsx');
// var GameListScreen = require('./GameListScreen.jsx')
// var GameDataScreen = require('./GameDataScreen.jsx')
// var ZoneDataScreen = require('./ZoneDataScreen.jsx')
// var ZoneSelectorScreen = require('./ZoneSelectorScreen.jsx')
// var NewGameScreen = require('./NewGameScreen.jsx')
var TopBar = require('./TopBar.jsx')

const CardGame = React.createClass({
  contextTypes: {
    router: React.PropTypes.object.isRequired
  },

	gotMessageCallback:function(reqNum, args){
		console.log("Shouldn't message callback here")
	},
	componentDidMount: function(){
		database.initConnection();
		if(this.props.route.path=="/")
			this.context.router.replace('/login')
	},
	render: function(){
		return <div><TopBar />{this.props.children}</div>;
	},
});


module.exports = CardGame;