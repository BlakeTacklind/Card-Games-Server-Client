var webpack = require('webpack')
var HtmlWebpackPlugin = require('html-webpack-plugin')
var path = require("path");
var srcPath = path.join(__dirname, 'src');

module.exports = {
  entry: {
    module: path.join(srcPath, 'main.jsx'),
    common: ['react', 'react-router']
  },
  output: {
    path: "/home/blake/cards/",
    publicPath: '/',
    filename: '[name].js',
    chunkFilename: '[id].chunk.js',
  },
  // resolve: {
  //   root: srcPath,
  //   extensions: ['', '.js', '.jsx', '.css'],
  //   modulesDirectories: ['node_modules', 'src']
  // },
  module: {
    loaders: [
      { test: /\.css$/, loader: "style!css" },
      { test: /\.js?x$/, exclude: /node_modules/, loader: 'babel' }
    ]
  },
  plugins: [
    new webpack.optimize.CommonsChunkPlugin('common', 'common.js'),
    new HtmlWebpackPlugin({
      inject: true,
      template: 'src/index.html'
    })
  ],
  devServer: {
    contentBase: './dist',
  }
};
