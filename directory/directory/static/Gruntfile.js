module.exports = function (grunt) {
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),

    uglify: {
      build: {
        files: {
          'build/js/script.min.js': [
            'assets/js/script.js',
          ]
        }
      }
    },

    jshint: {
      'all': ['assets/js/script.js']
    },
    
    sass: {
      dist: {
        options: {
          style: 'compressed',
          loadPath: ['bower_components/bootstrap-sass-official/assets/stylesheets/']
        },
        files: {
          'build/css/directory.css': 'assets/scss/bootstrap.scss',
        }
      }
    },

    watch: {
      grunt: { files: ['Gruntfile.js'] },
      options: {
        livereload: true,
      },

      sass: {
        files: ['assets/scss/*.scss', 'assets/js/*.js', 'Gruntfile.js'],
        tasks: ['build']
      }
    }

  });

  grunt.loadNpmTasks('grunt-contrib-sass');
  grunt.loadNpmTasks('grunt-contrib-watch');
  grunt.loadNpmTasks('grunt-contrib-uglify');
  grunt.loadNpmTasks('grunt-contrib-jshint');

  grunt.registerTask('build', ['sass', 'jshint', 'uglify']);
  grunt.registerTask('default', ['build','watch']);
};
