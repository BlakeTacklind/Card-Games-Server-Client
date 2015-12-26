'use strict';
var React = require('react');

var GameListElement = React.createClass({
	render: function(){
		return <div onClick = {this.props.clicked}>
				<p>{this.props.data.name} {this.props.data.type}</p>
			</div>;
	},
});

module.exports = GameListElement;