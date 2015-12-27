'use strict';
var React = require('react');
var database=require('./databaseHook.js')

var ZoneListElement = React.createClass({
	render: function(){
		return <div>
				<p onClick={this.props.clicked}>{this.props.data.owner==null?null:(this.props.data.ownerd==null?this.props.data.owneru:this.props.data.owneru)+"'s"} {this.props.data.name}</p>
				<button onClick={this.shuffleZone}>Shuffle</button>
			</div>;
	},
	shuffleZone: function(){
		database.sendRequest(1000, {'zone':this.props.data.id});
	},
});

module.exports = ZoneListElement;