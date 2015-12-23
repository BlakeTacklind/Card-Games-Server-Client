'use strict';
var React = require('react');

//displays a single card
//props: card{id, name, info, resource}
var CardViewer = React.createClass({
	render: function(){
		return <img src={this.props.card["resource"]} alt={this.props.card["name"]}>;
	},
});

module.exports = CardViewer;