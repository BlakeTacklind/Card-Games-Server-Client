'use strict';
var render = require('react-dom').render;
var React = require('react');

import {Router, Redirect, Route, Link, browserHistory} from 'react-router'

// var Router = require('react-router').Router
// var Redirect = require('react-router').Redirect
// var Route = require('react-router').Route
// var Link = require('react-router').Link
// var browserHistory = require('react-router').browserHistory 
// var RouterContext = require('react-router').RouterContext 

const CardGame = require('./CardGame.jsx');
const WelcomeScreen = require('./WelcomeScreen.jsx');
const PlayerScreen = require('./PlayerScreen.jsx');
var GameListScreen = require('./GameListScreen.jsx')
var GameDataScreen = require('./GameDataScreen.jsx')
var ZoneDataScreen = require('./ZoneDataScreen.jsx')
var ZoneSelectorScreen = require('./ZoneSelectorScreen.jsx')
var NewGameScreen = require('./NewGameScreen.jsx')

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
			<Route path="g/:id" component={GameDataScreen} />
			<Route path="z/:id" component={ZoneDataScreen} />
			<Route path="newgame" component={NewGameScreen} />
			<Route path="zones/place" component={ZoneSelectorScreen} testprop="haha"/>
			<Route path="zones/take" component={ZoneSelectorScreen} />
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