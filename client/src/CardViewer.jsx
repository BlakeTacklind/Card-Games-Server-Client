'use strict';
var React = require('react');

//displays a single card
//props: card{id, name, info, resource}
var CardViewer = React.createClass({
	// getInitialState: function(){
	// 	return {selected: false}
	// },
	// changeSelection: function(){
	// 	// console.log("try me")
	// 	if(this.state.selected==false)
	// 		this.props.sel();
	// 	else
	// 		this.props.unsel();
	// 	this.setState({selected: this.state.selected==false});
	// },
	render: function(){
		return <div onClick={this.props.clicked}>{this.card()}</div>
	},
	card: function(){
		if(this.props.card["resource"] != null)
			return <div><img src={this.props.card["resource"]} alt={this.props.card["name"]} /></div>;
		// else if (this.state.selected == true)
		// 	return <p><b>{this.props.card["name"]}</b></p>;
		else
			return <p>{this.props.card["name"]}</p>;
	},
});

module.exports = CardViewer;