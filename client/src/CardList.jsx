'use strict';
var React = require('react');

var playerdata = require('./playerdata.js');
var CardViewer = require('./CardViewer.jsx')

var GameList = React.createClass({
	render: function(){
		if(this.props.data == null) return null
		return (<div>
				{this.props.data.map(function(curr, i){
						return <CardViewer card={curr} key={i} clicked={function(){playerdata.selectedCard = curr; this.props.clicked();}.bind(this)} />
					}.bind(this))
				}
				</div>
		);
		// return null
	},
});

module.exports = GameList;