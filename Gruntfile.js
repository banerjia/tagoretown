module.exports = function(grunt) {

  grunt.initConfig({
    sass: {
      options: {
        sourcemap: 'none'
      },
      dist: {
        files: [{
          expand: true,
          cwd: 'static/src/sass/',
          src: ['*.scss', '*.sass'],
          dest: 'static/src/compiled_assets',
          ext: '.css'
        }]
      }
    },
    cssmin:{
      options: {
        sourceMap: false
      },
      target: {
        files: [{
          expand: true,
          cwd: 'static/src/compiled_assets',
          src: ['*.css', '!*.min.css'],
          dest: 'static/css',
          ext: '.min.css'
        }]
      }
    },
    coffee: {
      compileBare:{
        options:{
          bare: true,
        },
        files:[{
          expand: true,     // Enable dynamic expansion.
          cwd: 'static/src/coffee/',      // Src matches are relative to this path.
          src: ['*.coffee'], // Actual pattern(s) to match.
          dest: 'static/src/compiled_assets/',   // Destination path prefix.
          ext: '.js',   // Dest filepaths will have this extension.
          extDot: 'first'   // Extensions in filenames begin after the first dot
        }],
      }
    },
    uglify:{
      dynamic_mapping:{
        files:[{
          expand: true,     // Enable dynamic expansion.
          cwd: 'static/src/compiled_assets/',      // Src matches are relative to this path.
          src: ['*.js','!*.min.js'], // Actual pattern(s) to match.
          dest: 'static/js/',   // Destination path prefix.
          ext: '.min.js',   // Dest filepaths will have this extension.
          extDot: 'first'   // Extensions in filenames begin after the first dot
        }],
      },
    },
    concat: {
      options: {
        separator: ';',
      },
      dist: {
        files:{
          'static/js/app.min.js': ['bower_components/jquery/dist/jquery.min.js', 'bower_components/bootstrap/dist/js/bootstrap.min.js', 'static/js/tagoretown.min.js'],
          'static/css/app.min.css': ['bower_components/font-awesome/css/font-awesome.min.css', 'bower_components/bootstrap/dist/css/bootstrap.min.css',  'static/src/css/bootstrap-superhero.min.css'],
        },
      },
    },
    copy:{
      dist:{
        files:[{
          expand: true,
          cwd: 'bower_components/font-awesome/fonts',
          src: ['*-webfont.*'],
          dest: 'static/fonts'
        },{
          expand: true,
          cwd: 'bower_components/bootstrap/fonts',
          src: ['*.*'],
          dest: 'static/fonts'
        }]
      }
    }
  });

  grunt.loadNpmTasks('grunt-contrib-cssmin');
  grunt.loadNpmTasks('grunt-contrib-sass');
  grunt.loadNpmTasks('grunt-contrib-coffee');
  grunt.loadNpmTasks('grunt-contrib-uglify');
  grunt.loadNpmTasks('grunt-contrib-concat');
  grunt.loadNpmTasks('grunt-contrib-copy');

  grunt.registerTask('default', ['sass', 'cssmin', 'coffee:compileBare', 'uglify:dynamic_mapping','concat','copy']);

};