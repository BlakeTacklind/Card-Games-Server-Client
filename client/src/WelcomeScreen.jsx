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
    if(reqNum == 21){
      playerdata.username = args["username"]
      playerdata.userid = args["id"]
      playerdata.displayname = args["displayname"]
      return "PlayerScreen";
    }
    if(reqNum == 22){
      this.setState({mes: "username already exists"})
    }
    return null
  },
  getInitialState: function() {
    return {value: String(window.localStorage.prevLogin), mes: ''};
  },
  handleChange: function(event) {
    window.localStorage.prevLogin = event.target.value;
    this.setState({value: event.target.value});
  },
  loginClicked: function(){
    // console.log("button pushed");
    database.sendRequest(10, {username: this.state.value});
  },
  addPLayer: function(){
    // console.log("button pushed");
    database.sendRequest(20, {id: playerdata.userid, name: this.state.value});
  },
  render: function() {
    var value = this.state.value;
    return <div>
              <h1>Welcome</h1>
              <input type="text" value={value} onChange={this.handleChange} />
              <button onClick={this.loginClicked}>Log In</button>
              <button onClick={this.addPLayer}>New Log in</button>
              <h4>{this.state.mes}</h4>
           </div>;
  },
});

module.exports = WelcomeScreen;