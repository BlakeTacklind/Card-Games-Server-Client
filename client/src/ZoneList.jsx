'use strict';
var React = require('react');

var playerdata = require('./playerdata.js');
var ZoneListElement = require('./ZoneListElement.jsx')

var ZoneList = React.createClass({
	render: function(){
		if(this.props.data == null) return null
		return (<div>
				{this.props.data.map(function(curr, i){
						return <ZoneListElement data={curr} key={i} 
							clicked={function(){
								this.props.zoneReq(curr.id, curr.name); 
								// if(playerdata.zoneSelected == -1)
								// 	playerdata.zoneSelected = i;
							}.bind(this)} />
					}.bind(this))
				}
				</div>
		);
		// return null
	},
});

module.exports = ZoneList;