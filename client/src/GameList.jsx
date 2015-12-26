'use strict';
var React = require('react');

var playerdata = require('./playerdata.js');
var GameListElement = require('./GameListElement.jsx')

var GameList = React.createClass({
	render: function(){
		if(this.props.data == null) return null
		return (<div>
				{this.props.data.map(function(curr, i){
						return <GameListElement data={curr} key={i} clicked={function(){this.props.gameReq(curr.id); playerdata.selGame=i}.bind(this)} />
					}.bind(this))
				}
				</div>
		);
		// return null
	},
});

module.exports = GameList;