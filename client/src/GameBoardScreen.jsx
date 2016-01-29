'use strict';
var React = require('react');
var database = require('./databaseHook.js')

//Handler for once logged in
var GameBoard = React.createClass({
  contextTypes: {
    router: React.PropTypes.object.isRequired
  },
	handleMessage: function(reqNum, args){
		return null
	},
  componentDidMount: function(){
    database.callback = this.handleMessage
  },
	render: function(){
		return (<div>
				
			</div>);
	},
});

module.exports = GameBoard;