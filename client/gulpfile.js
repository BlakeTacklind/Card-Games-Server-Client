'use strict';
var gulp = require('gulp');
var less = require('gulp-less');
var sourcemaps = require('gulp-sourcemaps');
var browserify = require('browserify');
var transform = require('vinyl-transform');
var reactify = require('reactify');

gulp.task('main.js', function (){
	var browserifed = transform(function(filename) {
		var b = browserify({entries: filename, debug: true});
		b.transform(reactify);
		return b.bundle();
	});

	return gulp.src(['./src/main.jsx'])
		.pipe(browserifed)
		.pipe(gulp.dest('./dist'));
});

//All gulp need a default function 
gulp.task('default', ['src', 'deps']);

//run src when elements of array has been run
gulp.task('src', ['main.js', 'less', 'index.html']);

gulp.task('index.html', function() {
 return gulp.src('src/index.html')
  .pipe(gulp.dest('dist'));
});
 
gulp.task('less', function() {
 return gulp.src('src/**/*.less')
  .pipe(sourcemaps.init())
  .pipe(less({
      // paths: [ path.join(__dirname, 'less', 'includes') ]
    }))
  .pipe(sourcemaps.write())
  .pipe(gulp.dest('dist'));
});
 
gulp.task('bootstrap-fonts', function() {
 return gulp.src('node_modules/bootstrap/dist/fonts/*')
  .pipe(gulp.dest('dist/fonts'));
});
 
gulp.task('bootstrap', ['bootstrap-fonts'], function() {
 return gulp.src([
 'node_modules/bootstrap/dist/js/bootstrap.js',
 'node_modules/bootstrap/dist/css/bootstrap.css',
 'node_modules/bootstrap/dist/css/bootstrap.css.map',
 'node_modules/bootstrap/dist/css/bootstrap-theme.css',
 'node_modules/bootstrap/dist/css/bootstrap-theme.css.map'
 ])
  .pipe(gulp.dest('dist'));
});
 
gulp.task('jquery', function() {
 return gulp.src([
 'node_modules/jquery/dist/jquery.js',
 ])
  .pipe(gulp.dest('dist'));
});
 
gulp.task('deps',['bootstrap','jquery']);

//Watch files to check for changes in src directory
//and any changes cause default to be run again
gulp.task('watch', ['default'], function (){
	gulp.watch('./src/**/*.*', ['default']);
});