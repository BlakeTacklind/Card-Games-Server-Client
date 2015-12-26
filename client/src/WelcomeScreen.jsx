'use strict';
var React = require('react');
var database = require('./databaseHook.js');
var playerdata = require('./playerdata');

var WelcomeScreen = React.createClass({
  handleMessage: function (reqNum, args){
    if(reqNum == 11){
      playerdata.username = args["username"]
      playerdata.userid = args["id"]
      playerdata.displayname = args["displayname"]
      return "PlayerScreen";
    }
    if(reqNum == 12){
      this.setState({mes: "bad log in"})
    }
    return null
  },
  getInitialState: function() {
    this.props.messageFunc
    return {value: '', mes: ''};
  },
  handleChange: function(event) {
    this.setState({value: event.target.value});
  },
  loginClicked: function(){
    // console.log("button pushed");
    database.sendRequest(10, {username: this.state.value});
  },
  render: function() {
    var value = this.state.value;
    return <div>
              <h1>Welcome</h1>
              <input type="text" value={value} onChange={this.handleChange} />
              <button onClick={this.loginClicked}>Log In</button>
              <h4>{this.state.mes}</h4>
           </div>;
  },
  getSelf: function(){
    return <WelcomeScreen />;
  }
});

module.exports = WelcomeScreen;