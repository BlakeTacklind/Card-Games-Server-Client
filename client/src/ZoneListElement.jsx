'use strict';
var React = require('react');
var database=require('./databaseHook.js')
const Messages = require('./Messages.js')

var ZoneListElement = React.createClass({
	render: function(){
		if (this.props.other)
			var style={backgroundColor: 'Gainsboro'}
		else
			var style={backgroundColor: 'GhostWhite'}

		if(!this.props.buttons)
			return <p onClick={this.props.clicked} style={style}>{this.props.data.owner==null?null:(this.props.data.ownerd==null?this.props.data.owneru:this.props.data.owneru)+"'s"} {this.props.data.name}</p>
		
		return <div style={style}>
				<p onClick={this.props.clicked}>{this.props.data.owner==null?null:(this.props.data.ownerd==null?this.props.data.owneru:this.props.data.owneru)+"'s"} {this.props.data.name}</p>
				<button onClick={this.shuffleZone}>Shuffle</button>
				<button onClick={this.props.dealZone}>Deal</button>
			</div>;
	},
	shuffleZone: function(){
		database.sendRequest(Messages.SuffleZoneRQ, {'zone':this.props.data.id});
	},
});

module.exports = ZoneListElement;