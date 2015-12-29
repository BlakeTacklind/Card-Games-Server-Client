'use strict';
var React = require('react');
var database=require('./databaseHook.js')

var ZoneListElement = React.createClass({
	render: function(){
		return <div onClick={this.props.clicked}>
				<h4>{this.props.data.name}</h4>
				<p>{this.props.data.info}</p>
			</div>;
	},
});

module.exports = ZoneListElement;