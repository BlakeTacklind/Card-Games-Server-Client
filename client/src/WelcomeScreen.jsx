var React = require('react');
var database = require('./databaseHook.js');
var Router = require('react-router').Router
var Route = require('react-router').Route
var Link = require('react-router').Link
var browserHistory = require('react-router').browserHistory 

const WelcomeScreen = React.createClass({
  contextTypes: {
    router: React.PropTypes.object.isRequired
  },
  componentDidMount: function(){
    // console.log("change")
    database.callback = this.handleMessage
  },
  handleMessage: function (reqNum, args){
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
    let val = "";
    if(String(window.localStorage.prevLogin) != null)
      val = String(window.localStorage.prevLogin);

    return {value: val, mes: ''};
  },
  handleChange: function(event) {
    if(this.isValid(event.target.value))
      this.setState({value: event.target.value, mes: ''});
    else
      this.setState({mes: "Alphanumberic characters only"});
  },
  loginClicked: function(){
    window.localStorage.prevLogin = this.state.value;
    database.sendRequest(10, {username: this.state.value});
  },
  addPLayer: function(){
    window.localStorage.prevLogin = this.state.value;
    database.sendRequest(20, {username: this.state.value});
  },
  render: function() {
    return <div>
              <h1>Welcome</h1>
              <input type="text" value={this.state.value} onChange={this.handleChange} />
              <button onClick={this.loginClicked}>Log In</button>
              <button onClick={this.addPLayer}>New Log in</button>
              <h4>{this.state.mes}</h4>
           </div>;
  },
  isValid: function (str){
    return !/[^a-zA-Z0-9_]/g.test(str);
  }
});

module.exports = WelcomeScreen;