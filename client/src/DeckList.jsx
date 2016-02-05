var React = require('react');
var database = require('./databaseHook.js')
var DeckElement = require('./DeckElement.jsx')

var DeckList = React.createClass({

	render: function(){
		return (<div>
				{this.props.data.map(function(curr, i){
						return (<DeckElement data={curr} key={i} other={i%2==1}
							clicked={function(){
								this.props.elementClicked(i);
							}.bind(this)} />)
					}.bind(this))
				}
				</div>
		);	},

});

module.exports = DeckList;