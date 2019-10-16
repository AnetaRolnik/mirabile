const gulp            = require("gulp");
const sass            = require("gulp-sass");
const autoprefixer    = require("gulp-autoprefixer");
const sourcemaps      = require("gulp-sourcemaps");
const plumber         = require("gulp-plumber");
const rename          = require("gulp-rename");
const webpack         = require("webpack");
const csso            = require('gulp-csso');
const browserSync     = require('browser-sync').create();
const exec            = require('child_process').exec;

gulp.task("sass", function() {
    return gulp.src("./blog/static/src/styles/main.scss")
        .pipe(plumber())
        .pipe(sourcemaps.init())
        .pipe(sass({
            outputStyle: "compressed"
        }))
        .pipe(autoprefixer({
            browsers: ["> 1%"]
        }))
        .pipe(csso())
        .pipe(rename({
            suffix: ".min",
            basename: "style"
        }))
        .pipe(sourcemaps.write("."))
        .pipe(gulp.dest("./blog/static/dist"))
        .pipe(browserSync.stream({match: "**/*.css"}));
});

gulp.task('runserver', function() {
    const proc = exec('python manage.py runserver')
})
  
gulp.task('browserSync', ['runserver'], function() {
    browserSync.init({
        notify: false,
        port: 8000,
        proxy: '127.0.0.1:8000'
    })
});

gulp.task("es6", function(cb) {
    return webpack(require("./webpack.config.js"), function(err, stats) {
        if (err) throw err;
        console.log(stats.toString());
        cb();
        browserSync.reload();
    })
})

gulp.task("watch", function() {
    gulp.watch("./blog/static/src/styles/**/*.scss", ["sass"]);
    gulp.watch("./blog/static/src/js/**/*.js", ["es6"]);
    gulp.watch('./blog/templates/*.html');
});

gulp.task("default", function() {
    gulp.start(["sass", "es6", "browserSync", "watch"]);
});

