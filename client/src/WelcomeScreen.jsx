'use strict';
var React = require('react');
var database = require('./databaseHook.js');
var Router = require('react-router').Router
var Route = require('react-router').Route
var Link = require('react-router').Link
var browserHistory = require('react-router').browserHistory 
// var playerdata = require('./playerdata');

const WelcomeScreen = React.createClass({
  contextTypes: {
    router: React.PropTypes.object.isRequired
  },
  // componentWillMount() {
  //   this.context.router.setRouteLeaveHook(
  //     this.props.route,
  //     this.routerWillLeave
  //   )
  // },
  test(){
    console.log("test")
  },
  componentDidMount: function(){
    // console.log("change")
    database.callback = this.handleMessage
  },
  handleMessage: function (reqNum, args){
    console.log("test")
    if(reqNum == 11){
      window.sessionStorage.username = args["username"]
      window.sessionStorage.userid = Number(args["id"])
      window.sessionStorage.displayname = args["displayname"]
      this.context.router.push('/p/'+window.sessionStorage.username);
      return "PlayerScreen";
    }
    if(reqNum == 12){
      this.setState({mes: "bad log in"})
    }
    if(reqNum == 21){
      window.sessionStorage.username = args["username"]
      window.sessionStorage.userid = Number(args["id"])
      window.sessionStorage.displayname = args["displayname"]
      this.context.router.push('/p/username');
      return "PlayerScreen";
    }
    if(reqNum == 22){
      this.setState({mes: "username already exists"})
    }
    return null
  },
  getInitialState: function() {
    return {value: String(window.localStorage.prevLogin), mes: 'Do not use special characters, please'};
  },
  handleChange: function(event) {
    // window.localStorage.prevLogin = event.target.value;
    this.setState({value: event.target.value});
  },
  loginClicked: function(){
    // console.log("button pushed");
    window.localStorage.prevLogin = this.state.value;
    database.sendRequest(10, {username: this.state.value});
  },
  addPLayer: function(){
    // console.log("button pushed");
    window.localStorage.prevLogin = this.state.value;
    database.sendRequest(20, {name: this.state.value});
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