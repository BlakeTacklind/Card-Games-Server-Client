var React = require('react');
var database = require('./databaseHook.js')
var ZoneListElement = require('./ZoneListElement.jsx')
const Messages = require('./Messages.js')

var DealZones = React.createClass({
	doneDeal: function(){
		let n = prompt("Enter Number of cards to be distributed (-1 for all)")

		n = parseInt(n)

		if(!isNaN(n)){
			this.props.doneDeal(n)
		}
	},
	render: function(){
		if(this.props.data == null)
			return null

		console.log(this.props.data.find((ele) => {
			return ele.id == Number(window.sessionStorage.zoneSelectedId)
		}))		

		return (<form action="deal">
				<div>
					<button onClick={this.doneDeal}>Finish</button>
					<button onClick={this.props.cancel}>Cancel</button>
					<ZoneListElement data={this.props.data.find((ele) => {return ele.id == Number(window.sessionStorage.zoneSelectedId)})} buttons={false} key={-1} />
				</div>
				{this.props.data.map(function(curr, i){
						if(curr.id == Number(window.sessionStorage.zoneSelectedId))
							return null;
						return (
							<div>
								<input type="checkbox" value={"b"+i} name="zone" key={"c"+i} onClick={function(e){this.props.handleChecked(e, curr.id)}.bind(this)}/>
								<ZoneListElement data={curr} buttons={false} key={i}/>
							</div>)
					}.bind(this))
				}
			</form>
		)
	},
});

module.exports = DealZones;