'use strict';
var React = require('react');

var ZoneListElement = require('./ZoneListElement.jsx')

var ZoneList = React.createClass({
	render: function(){
		if(this.props.data == null) return null
		return (<div>
				{this.props.data.map(function(curr, i){
						return <ZoneListElement data={curr} key={i} 
							clicked={function(){
								this.props.zoneReq(curr.id, curr.name, curr.owner);
							}.bind(this)} 
							dealZone={function(){
								this.props.dealZone(curr.id)
							}.bind(this)}
							buttons={true} />
					}.bind(this))
				}
				</div>
		);
		// return null
	},
});

module.exports = ZoneList;