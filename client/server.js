var express = require('express')
var webpack = require('webpack')
var webpackDevMiddleware = require('webpack-dev-middleware')
var WebpackConfig = require('./webpack.config')

var app = express()

app.use(webpackDevMiddleware(webpack(WebpackConfig), {
  publicPath: '/dist/',
  stats: {
    colors: true
  }, 
  quiet: false,
  lazy:true
}))

app.get("/", express.static(__dirname+"\\dist"))
app.get('*', function(req, res){
// 	res.send('Answer is: '+req.originalUrl)
	// res.sendfile(express.static(__dirname+"\\dist"))
	res.redirect('/')
})

app.listen(8081, function () {
  console.log('Server listening on http://localhost:8081, Ctrl+C to stop')
})

console.log('path: '+app.path())