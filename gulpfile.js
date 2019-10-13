const gulp            = require("gulp");
const sass            = require("gulp-sass");
const autoprefixer    = require("gulp-autoprefixer");
const sourcemaps      = require("gulp-sourcemaps");
const plumber         = require("gulp-plumber");
const rename          = require("gulp-rename");
const webpack         = require("webpack");
const csso            = require('gulp-csso');

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
});


gulp.task("es6", function(cb) {
    return webpack(require("./webpack.config.js"), function(err, stats) {
        if (err) throw err;
        console.log(stats.toString());
        cb();
    })
})

gulp.task("watch", function() {
    gulp.watch("./blog/static/src/styles/**/*.scss", ["sass"]);
    gulp.watch("./blog/static/src/js/**/*.js", ["es6"]);
});

gulp.task("default", function() {
    gulp.start(["sass", "es6",  "watch"]);
});