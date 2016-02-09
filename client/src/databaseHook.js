
socket = null
isopen = false

function getRequest(i, args){
   return {rq: i , ag: args};
}

var event = new Event('data');

var database = {

   sendMessage: function(obj){
      if (isopen) {
         socket.send(JSON.stringify(obj));
         // console.log("Something sent");     
      } else {
         console.log("Not Connected");
      }
   },

   sendPlainMessage: function(obj){
      if (isopen) {
         socket.send(obj);
         // console.log("Something sent");     
      } else {
         console.log("Not Connected");
      }
   },

   sendRequest: function(i, args){
      this.sendMessage(getRequest(i, args));
   },
   callback: function(req, args){
      console.log("No call back set")
   },
   connectionEvent: function(isConnected){
      console.log("No connection Event set")
   },
   initConnection: function(){
      // callback=cb;
      console.log("test")

      socket = new WebSocket("ws://127.0.0.1:11337");

      console.log("test 2")

      socket.binaryType = "arraybuffer";

      socket.onopen = function() {
         // console.log(socket);
         console.log("Connected!");
         isopen = true;
         this.connectionEvent(isopen)
         // console.log(this.isopen);
      }.bind(this)

      socket.onmessage = function(e) {
         if (typeof e.data == "string") {
            out = JSON.parse(e.data);
            console.log("Text message received: " + e.data);
            this.callback(out['rq'], out['ag']);
         }
      }.bind(this)

      socket.onclose = function(e) {
         console.log("Connection closed.");
         socket = null;
         isopen = false;
         this.connectionEvent(isopen)
      }.bind(this)
   },
   reconnect: function(){
      if (isopen){
         socket.close()
         socket = null;
         isopen = false;
      }
      this.initConnection;
   },
}

module.exports = database;
