var React = require('react');
var database = require('./databaseHook.js')
var GameTypeList = require('./GameTypeList.jsx')
var PlayersSelector = require('./PlayersSelector.jsx')
var DeckPicker = require('./DeckPicker.jsx')
const Messages = require('./Messages.js')

var NewGame = React.createClass({
  contextTypes: {
    router: React.PropTypes.object.isRequired
  },
	getInitialState : function(){
		this.playersSelected = [Number(window.sessionStorage.userid),]
		this.gameType = -1
    database.callback = this.handleMessage
		return {onList: "type", deckPickeing: false, decks: []};
	},
	handleMessage: function(reqNum, args){

		if (reqNum == Messages['CreateNewGameSuccess'] || reqNum == Messages['CreateNewGameFail']){
			this.context.router.push('/p/'+String(window.sessionStorage.username)+'/games')
			return
		}
		if (reqNum == Messages['GetDeckChooser']){

			this.setState({deckPickeing: true, decks: args})
			return
		}

		this.refs.GamesList.handleMessage(reqNum, args)
		this.refs.PlayerList.handleMessage(reqNum, args)

	},
	render: function(){
		if (!this.state.deckPickeing){
			return <div>
					<h1>New Game</h1>
					<GameTypeList ref="GamesList" selection={this.selection}/>
					<PlayersSelector ref="PlayerList" handleChecked={this.handleChecked}/>
					<button onClick={this.doneClicked}>Finish and Name</button>
				</div>;
			}
		else{
			console.log("test 1")
			return <DeckPicker data={this.state.decks}/>;
		}
	},
	handleChecked: function(e, id){
		if(e.target.checked){
			this.playersSelected.push(id)
		}
		else{
			var index = this.playersSelected.indexOf(id)
			if(index > -1)
				this.playersSelected.splice(index, 1)
		}
		// console.log(this.playersSelected)
	},
	selection: function(i){
		this.gameType = i;
	},
	doneClicked: function(){
		let name = prompt('Name the Game')

		if(name!=null && this.isValid(name)){
			database.sendRequest(Messages.CreateNewGame, {players: this.playersSelected, type: this.gameType, name: name});
			// this.context.router.push('/p/'+String(window.sessionStorage.username)+'/games')
		}
	},
  isValid: function (str){
    return !/[^a-zA-Z0-9_ -]/g.test(str);
  }
});

module.exports = NewGame;