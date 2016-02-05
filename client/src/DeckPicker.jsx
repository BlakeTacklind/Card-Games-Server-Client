var React = require('react');
var database = require('./databaseHook.js')
var DeckList = require('./DeckList.jsx')
const Messages = require('./Messages.js')

var DeckPicker = React.createClass({
  contextTypes: {
    router: React.PropTypes.object.isRequired
  },
	getInitialState : function(){
		return {currentSelected: []};
	},
	handleMessage: function(reqNum, args){
		
	},
	render: function(){
		return (<div>
				<div>
					<button onClick={this.selectDecks}>Done</button>
					<button onClick={this.cancelSelect}>Cancel</button>
				</div>
				<DeckList elementClicked={this.removeFromList} data={this.state.currentSelected} style={{backgroundColor: 'LightCoral'}}/>
				<DeckList elementClicked={this.addToList} data={this.props.data} />
			</div>);
	},
	addToList: function(index){
		var arr = [...this.state.currentSelected, this.props.data[index]];
		console.log(arr);
		this.setState({currentSelected:arr})
	},
	removeFromList: function(index){
		var cS = this.state.currentSelected
		cS.splice(index, 1)
		this.setState({currentSelected: cS})
	}, 
	selectDecks: function(){
		database.sendRequest(Messages['GetDeckChooserSuccess'], {decks:this.state.currentSelected.map((cv)=>{return cv.id;})})
		this.setState({currentSelected: []});
	},
	cancelSelect: function(){
		database.sendRequest(Messages['GetDeckChooserFail'], null)
		this.context.router.push('/p/'+String(window.sessionStorage.username)+'/games')
	},

});

module.exports = DeckPicker;