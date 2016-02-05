var React = require('react');
var database = require('./databaseHook.js');

var TopBar = React.createClass({
  contextTypes: {
    router: React.PropTypes.object.isRequired
  },
	render: function(){
		//<button onClick={database.reconnect}>Reconnect</button>
		return (<div>
				<button onClick={this.getNotifications}>Messages</button>
			</div>);
	},
	getNotifications: function(){
		this.context.router.push('/p/'+String(window.sessionStorage.username)+'/messages')
	},
});

module.exports = TopBar;