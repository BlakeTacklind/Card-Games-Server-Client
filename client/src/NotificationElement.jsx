var React = require('react');

var NotationElement = React.createClass({
	render: function(){
		name = (this.props.data.displayname==null) ? this.props.data.displayname:this.props.data.username;

		return <div onClick={this.props.clicked}>
				<p>{name}@{this.props.data.timestamp}: {this.props.data.message}</p>
			</div>;
	},
});

module.exports = NotationElement;