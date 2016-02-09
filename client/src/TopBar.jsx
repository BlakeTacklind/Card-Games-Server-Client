var React = require('react');
var database = require('./databaseHook.js');

var TopBar = React.createClass({
  contextTypes: {
    router: React.PropTypes.object.isRequired
  },
  componentDidMount: function(){
    database.connectionEvent = this.connectionEvent
  },
	getInitialState : function(){
		return {reconnect: null};
	},
	render: function(){
		return (<div>
				<button onClick={this.getNotifications}>Messages</button>
				{this.state.reconnect}
			</div>);
	},
	getNotifications: function(){
		this.context.router.push('/p/'+String(window.sessionStorage.username)+'/messages')
	},
	connectionEvent: function(isConnected){
		if(isConnected){
			this.setState({reconnect: null})
		}
		else{
			this.setState({reconnect: <button onClick={database.reconnect}>Reconnect</button>})
		}
	}
});

module.exports = TopBar;