var React = require('react');
var database = require('./databaseHook.js')
var GameTypeElement = require('./GameTypeElement.jsx')

var GameTypeList = React.createClass({
	getInitialState : function(){
		database.sendRequest(160, {});
		return {data: null};
	},

	handleMessage: function(reqNum, args){
		if (reqNum == 162)
			return null
		if (reqNum == 161){
			if(args.length > 0)
				this.props.selection(args[0].id)
			
			this.setState({data: args})
		}
		return null
	},
	render: function(){
		if(this.state.data == null){
			console.log("state is null")
			return null
		}
		return (<div>
			{this.state.data.map(
				function(curr, i){
					return (<GameTypeElement data={curr} key={"t"+i} clicked={function(){this.props.selection(curr.id)}.bind(this)} />)}.bind(this))
			}
			</div>)
	},
});

module.exports = GameTypeList;