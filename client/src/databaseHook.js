


var database = {
   socket: null,
   isopen: false,

   sendMessage: function(obj){
      if (this.isopen) {
         this.socket.send(obj);
         console.log("something sent");     
      } else {
         console.log("something not sent");
      }
   },

   init: function(){

      this.socket = new WebSocket("ws://127.0.0.1:11337");
      this.socket.binaryType = "arraybuffer";

      this.socket.onopen = function() {
         // console.log(socket);
         console.log(this.socket);
         console.log("Connected!");
         this.isopen = true;
         this.socket.send("{\"firstName\":\"John\", \"lastName\":\"Doe\"}");
      }

      this.socket.onmessage = function(e) {
         if (typeof e.data == "string") {
            console.log("Text message received: " + e.data);
         }
      }

      this.socket.onclose = function(e) {
         console.log("Connection closed.");
         this.socket = null;
         this.isopen = false;
      }
   },
}

module.exports = database;
