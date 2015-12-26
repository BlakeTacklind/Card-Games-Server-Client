'use strict';
var React = require('react');

var ZoneListElement = React.createClass({
	render: function(){
		return <div onClick = {this.props.clicked}>
				<p>{this.props.data.name} {this.props.data.owner} {this.props.data.ds}</p>
			</div>;
	},
});

module.exports = ZoneListElement;