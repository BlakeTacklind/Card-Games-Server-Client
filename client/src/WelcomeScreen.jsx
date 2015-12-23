'use strict';
var React = require('react');
var database = require('./databaseHook.js');

var WelcomeScreen = React.createClass({
  getInitialState: function() {
    return {value: ''};
  },
  handleChange: function(event) {
    this.setState({value: event.target.value});
  },
  loginClicked: function(){
    // console.log("button pushed");
    database.sendRequest(10, [this.state.value]);
  },
  render: function() {
    var value = this.state.value;
    return <div>
              <h1>Welcome</h1>
              <input type="text" value={value} onChange={this.handleChange} />
              <button onClick={this.loginClicked}>Log In</button>
           </div>;
  }
});

module.exports = WelcomeScreen;