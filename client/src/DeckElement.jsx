var React = require('react');
var database = require('./databaseHook.js')

var DeckElement = React.createClass({

	render: function(){
		if (this.props.other)
			var style={backgroundColor: 'Gainsboro'}
		else
			var style={backgroundColor: 'GhostWhite'}

		return (<div onClick = {this.props.clicked} style={style}>{this.props.data.name}</div>);
	},

});

module.exports = DeckElement;