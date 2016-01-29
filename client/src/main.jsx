'use strict';
var render = require('react-dom').render;
var React = require('react');

import {Router, Redirect, Route, Link, browserHistory} from 'react-router'

const CardGame = require('./CardGame.jsx');
const WelcomeScreen = require('./WelcomeScreen.jsx');
const PlayerScreen = require('./PlayerScreen.jsx');
var GameListScreen = require('./GameListScreen.jsx')
var GameDataScreen = require('./GameDataScreen.jsx')
var ZoneDataScreen = require('./ZoneDataScreen.jsx')
var ZoneSelectorScreenPlace = require('./ZoneSelectorScreenPlace.jsx')
var ZoneSelectorScreenTake = require('./ZoneSelectorScreenTake.jsx')
var NewGameScreen = require('./NewGameScreen.jsx')
var NotificationList = require('./NotificationListScreen.jsx')
var GameBoardScreen = require('./GameBoardScreen.jsx')

var database = require('./databaseHook.js')

var NoPage = React.createClass({
  contextTypes: {
    router: React.PropTypes.object.isRequired
  },

	componentDidMount: function(){
		console.log(this.props.location.pathname)
	},
	goHome: function(){
		this.context.router.push("/login")
	},
	render: function(){
		return <h1>Page Not Found</h1>;
	}
})


render((
	<Router history={browserHistory}>
		<Route path="/" component={CardGame} >
			<Route path="login" component={WelcomeScreen} />
			<Route path="p/:name" component={PlayerScreen} />
			<Route path="p/:name/games" component={GameListScreen} />
			<Route path="p/:name/messages" component={NotificationList} />
			<Route path="g/:id" component={GameDataScreen} />
			<Route path="g/:id/board" component={GameBoardScreen} />
			<Route path="z/:id" component={ZoneDataScreen} />
			<Route path="newgame" component={NewGameScreen} />
			<Route path="zones/place" component={ZoneSelectorScreenPlace} />
			<Route path="zones/take" component={ZoneSelectorScreenTake} />
			<Route path="*" component={NoPage} />
		</Route>
	</Router>
	),
  document.getElementById('main')
);

			// <Route path="(player/)games" component={GameListScreen} />
			// <Route path="g/:id" component={GameDataScreen} />
			// <Route path="z/:id" component={ZoneDataScreen} />
			// <Route path="zones" component={ZoneSelectorScreen} />
			// <Route path="newGame" component={NewGameScreen} />