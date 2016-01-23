'use strict';
var React = require('react');
var clientdata = require('./clientdata.js');
var database = require('./databaseHook.js')
var NotificationElement = require('./NotificationElement.jsx')
const Messages = require('./Messages.js')

var NotificationList = React.createClass({
	render: function(){
		if(this.props.data == null) return null
		return (<div>
				{this.props.data.map(function(curr, i){
						return (<NotificationElement data={curr} key={i} 
							clicked={function(){
								// this.props.notationClicked(curr.id, curr.name, curr.owner);
							}.bind(this)} />)
					}.bind(this))
				}
				</div>
		);
		// return null
	},
});

module.exports = NotificationList;