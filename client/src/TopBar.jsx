var React = require('react');
var database = require('./databaseHook.js');

var TopBar = React.createClass({
  contextTypes: {
    router: React.PropTypes.object.isRequired
  },
	render: function(){
		return (<div>
				<button onClick={database.reconnect}>Reconnect</button>
				<button onClick={()=>{}}>Messages</button>
			</div>);
	},
});

module.exports = TopBar;