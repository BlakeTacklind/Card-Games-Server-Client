var React = require('react');
var database = require('./databaseHook.js')

var DeckElement = React.createClass({

	render: function(){
		return (<div onClick = {this.props.clicked}>{this.props.data.name}</div>);
	},

});

module.exports = DeckElement;