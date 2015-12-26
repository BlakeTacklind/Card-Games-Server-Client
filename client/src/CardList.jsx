'use strict';
var React = require('react');

var playerdata = require('./playerdata.js');
var CardViewer = require('./CardViewer.jsx')

var GameList = React.createClass({
	render: function(){
		// console.log("test p 1")
		if(this.props.data == null) return null
		// console.log("test p 2")
		return (<div>
				{this.props.data.map(function(curr, i){
						return <CardViewer card={curr} key={i} /*clicked={function(){this.props.gameReq(curr.id); playerdata.selGame=i}.bind(this)}*/ />
					}.bind(this))
				}
				</div>
		);
		// return null
	},
});

module.exports = GameList;