const gulp = require('gulp');
const sass = require('gulp-sass')(require('sass'));
const browserSync = require('browser-sync').create();

//compile scss into css
function build() {
    return gulp.src('./**/static/**/*.scss')
        .pipe(sass().on('error',sass.logError))
        .pipe(gulp.dest(function (file) {
            return file.base;
        }))
        .pipe(browserSync.stream());
}
function watch() {
    browserSync.init();
    gulp.watch('./**/static/**/*.scss', build)
}
exports.build = build;
exports.watch = watch;