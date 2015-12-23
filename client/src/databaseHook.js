
socket = null
isopen = false

var database = {

   sendMessage: function(obj){
      if (isopen) {
         socket.send(JSON.stringify(obj));
         console.log("Something sent");     
      } else {
         console.log("Not Connected");
      }
   },

   init: function(){

      socket = new WebSocket("ws://127.0.0.1:11337");
      socket.binaryType = "arraybuffer";

      socket.onopen = function() {
         // console.log(socket);
         console.log("Connected!");
         isopen = true;
         // console.log(this.isopen);
      }

      socket.onmessage = function(e) {
         if (typeof e.data == "string") {
            console.log("Text message received: " + e.data);
         }
      }

      socket.onclose = function(e) {
         console.log("Connection closed.");
         socket = null;
         isopen = false;
      }
   },
}

module.exports = database;
