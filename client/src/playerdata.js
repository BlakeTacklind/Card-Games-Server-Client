
var playerdata = {
	userid: 0,
	username: null,
	displayname: null,
	name: function(){return (this.displayname == null) ? this.username : this.displayname},
	games: null
}


module.exports = playerdata;
