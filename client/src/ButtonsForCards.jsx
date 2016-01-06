'use strict';
var React = require('react');

var Buttons = React.createClass({
  componentDidMount: function(){
    database.callback = this.handleMessage
  },
	getInitialState: function(){
		return {selecting: false}
	},
	buttonName: function(){
		if(this.state != null && this.state.selecting == true)
			return "cancel move card to zone"
		else
			return "move card to zone";
	},
	render: function(){
		return <div>
			<button onClick={this.clickedGiveCard}>{this.buttonName()}</button>
			<button onClick={this.clickerTakeCard}>get card from zone</button>
		</div>
	},
	clickedGiveCard: function(){
		this.setState({selecting: this.state.selecting == false})
	},
	clickerTakeCard: function(){
		this.context.router.push('/zones/take')
	},
	getSelectedState: function(){
		return this.state.selecting;
	},
});

module.exports = Buttons;