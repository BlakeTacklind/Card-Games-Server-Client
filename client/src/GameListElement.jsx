'use strict';
var React = require('react');

var GameListElement = React.createClass({
	render: function(){
		if (this.props.other)
			var style={backgroundColor: 'Gainsboro'}
		else
			var style={backgroundColor: 'GhostWhite'}
		
		return <div onClick = {this.props.clicked} style={style}>
				<p>{this.props.data.name} {this.props.data.type}</p>
			</div>;
	},
});

module.exports = GameListElement;