var express = require('express')
var webpack = require('webpack')
var webpackDevMiddleware = require('webpack-dev-middleware')
var WebpackConfig = require('./webpack.config')

var app = express()

app.use(webpackDevMiddleware(webpack(WebpackConfig), {
  publicPath: '/dist/',
  stats: {
    colors: true
  }
}))

app.use(express.static(__dirname+"\\dist"))

app.listen(8081, function () {
  console.log('Server listening on http://localhost:8081, Ctrl+C to stop')
})
