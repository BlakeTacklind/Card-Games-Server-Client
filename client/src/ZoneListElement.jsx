'use strict';
var React = require('react');

var ZoneListElement = React.createClass({
	render: function(){
		return <div onClick = {this.props.clicked}>
				<p>{this.props.data.owner==null?null:(this.props.data.ownerd==null?this.props.data.owneru:this.props.data.owneru)+"'s"} {this.props.data.name} {this.props.data.ds}</p>
			</div>;
	},
});

module.exports = ZoneListElement;