var gulp = require('gulp');
var shell = require('gulp-shell');
var watch = require('gulp-watch');

gulp.task('serve', [], function() {
    gulp.watch(["templates/**/*.html","static/**/*"]).on('change', function(file) {
        gulp.start('build_site');
    });
    gulp.start('build_site');
});

gulp.task('build_site', function() {
    console.log('++ rebuilding');
    return gulp.src('')
        .pipe(shell([
            './build.sh'
        ], {
            templateData: {
                f: function (s) {
                    return s
                }
        }
        }))
        ;
});

gulp.task('default', ['serve']);