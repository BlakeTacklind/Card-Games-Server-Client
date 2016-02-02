'use strict';
var React = require('react');

var GameListElement = require('./GameListElement.jsx')

var GameList = React.createClass({
	render: function(){
		if(this.props.data == null) return null
		return (<div>
				{this.props.data.map(function(curr, i)
					{
						return (<GameListElement data={curr} key={i} other={(i%2)==1}
							clicked={function(){
								this.props.gameReq(curr.id, curr.name)
							}.bind(this)
						} />)
					}.bind(this))
				}
				</div>
		);
		// return null
	},
});

module.exports = GameList;