
var playerdata = {
	userid: 0,
	username: null,
	displayname: null,
	name: function(){return (this.displayname == null) ? this.username : this.displayname},
	games: null,
	selGame: -1,
	gameData: null,
	zoneData: null,
	zoneSelected: -1,
}


module.exports = playerdata;
