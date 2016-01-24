'use strict';
var React = require('react');
var clientdata = require('./clientdata.js');
var database = require('./databaseHook.js')
var NotificationList = require('./NotificationList.jsx')
const Messages = require('./Messages.js')

var NotificationsScreen = React.createClass({
  contextTypes: {
    router: React.PropTypes.object.isRequired
  },
  componentDidMount: function(){
    database.callback = this.handleMessage
		database.sendRequest(Messages.RequestMessages, {id: Number(window.sessionStorage.userid)});
  },
	// requestGameData: function(id, name){
	// 	this.context.router.push('/g/'+id)
	// 	window.sessionStorage.gameSelectedId = id
	// 	window.sessionStorage.gameSelectedName = name;
	// },
	getInitialState : function(){
		return {messages: clientdata.messages};
	},

	handleMessage: function(reqNum, args){
		if (reqNum == Messages.RequestMessagesFail)
			return null
		if (reqNum == Messages.RequestMessagesSuccess){
			clientdata.messages = args;
			this.setState({messages: clientdata.messages});
			
			var notReadArr = []
			clientdata.messages.forEach((cv)=>{if(!cv.read){notReadArr.push(cv.id)}})
			// console.log(notReadArr)
			if(notReadArr.length > 0){
				database.sendRequest(Messages.MarkReadRequest, {mesids: notReadArr})
			}
			return null
		}
		if (reqNum == Messages.deleteNotificationRequestSuccess){
			clientdata.messages = clientdata.messages.filter((cv)=>{return cv.id != args.id});
			// console.log(clientdata.messages)
			this.setState({messages: clientdata.messages});
		}
		return null
	},

	deleteNotification: function(nid){
		database.sendRequest(Messages.deleteNotificationRequest, {id: nid})
	},
	render: function(){
		var name = (String(window.sessionStorage.displayname) == null) ? String(window.sessionStorage.username) : String(window.sessionStorage.displayname);
		return (<div>
				<h1>{name + "'s Notifications"}</h1>
				<NotificationList data={this.state.messages} delNot={this.deleteNotification} />
			</div>);
	},
});

module.exports = NotificationsScreen;