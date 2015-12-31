'use strict';
var React = require('react');
var database = require('./databaseHook.js');
var playerdata = require('./playerdata');

var NameGame = React.createClass({
  getInitialState: function(){
    return {value: ""}
  },
  handleChange: function(event) {
    this.setState({value: event.target.value});
  },
  render: function() {
    var value = this.state.value;
    return <div>
              <input type="text" value={value} onChange={this.handleChange} />
              <button onClick={this.startGame}>Finish Game</button>
           </div>;
  },
  startGame: function(){
    database.sendRequest(150, {players: playerdata.playersSelected, type: Number(window.sessionStorage.selGameType), name: this.state.value});
    this.props.setParentState("GameListScreen")
  },
});

module.exports = NameGame;