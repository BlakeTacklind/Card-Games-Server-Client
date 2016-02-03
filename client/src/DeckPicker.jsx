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
				<DeckList elementClicked={this.removeFromList} data={this.state.currentSelected}/>
				<DeckList elementClicked={this.addToList}/>
			</div>);
	},
	addToList: function(index){
		this.setState({currentSelected:[...currentSelected, this.props.data[index]]})
	},
	removeFromList: function(index){
		cS = currentSelected
		cS.splice(index, 1)
		return cS
	},

});

module.exports = DeckPicker;