'use strict';
var React = require('react');
var database=require('./databaseHook.js')

var ZoneListElement = React.createClass({
	render: function(){
		return <div onClick={this.props.clicked}>
				<p>{this.getName()}</p>
			</div>;
	},
	getName: function(){
		if(this.props.data.displayname==null)
			return this.props.data.username
		return this.props.data.displayname
	},
});

module.exports = ZoneListElement;