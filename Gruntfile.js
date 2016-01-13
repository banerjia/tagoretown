module.exports = function(grunt) {

  grunt.initConfig({
    sass: {
      options: {
        sourceMap: 'none'
      },
      dist: {
        files: [{
          expand: true,
          cwd: 'static/src/sass/',
          src: ['*.scss', '*.sass'],
          dest: 'static/css',
          ext: '.css'
        }]
      }
    },
    cssmin:{
      options: {
        sourceMap: 'none'
      },
      target: {
        files: [{
          expand: true,
          cwd: 'static/css',
          src: ['*.css', '!*.min.css'],
          dest: 'release/css',
          ext: '.min.css'
        }]
      }

    }
  });

  grunt.loadNpmTasks('grunt-contrib-cssmin');
  grunt.loadNpmTasks('grunt-contrib-sass');
//  grunt.loadNpmTasks('grunt-contrib-watch');

  grunt.registerTask('default', ['sass']);

};