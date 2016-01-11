'use strict';
var React = require('react');

//displays a single card
//props: card{id, name, info, resource}
var CardViewer = React.createClass({
	render: function(){
		return <div onClick={this.props.clicked}>{this.card()}</div>
	},
	card: function(){
		if(this.props.card["resource"] != null)
			return <div><img src={this.props.card["resource"]} alt={this.props.card["name"]} /></div>;
		else
			return <p>{this.props.card["name"]}</p>;
	},
});

module.exports = CardViewer;