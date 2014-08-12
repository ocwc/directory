module.exports = function (grunt) {
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),

    uglify: {
      build: {
        files: {
          'build/js/script.min.js': [
            'bower_components/jquery-legacy/dist/jquery.min.js',
            'assets/js/script.js',
          ]
        }
      }
    },
    
    sass: {
      options: {
        includePaths: ['bower_components/foundation/scss']
      },
      dist: {
        options: {
          outputStyle: 'compressed'
        },
        files: {
          'build/css/app.css': 'assets/scss/app.scss',
          'build/css/ie8.css': 'assets/scss/ie8.scss',
        }
      }
    },

    pixrem: {
      options: {
        rootvalue: '14px'
      },
      dist: {
        src: 'build/css/app.css',
        dest: 'build/css/app.css'
      }
    },

    watch: {
      grunt: { files: ['Gruntfile.js'] },
      options: {
        livereload: true,
      },

      sass: {
        files: ['assets/scss/*.scss', 'Gruntfile.js'],
        tasks: ['sass', 'pixrem']
      }
    }

  });

  grunt.loadNpmTasks('grunt-contrib-uglify');
  grunt.loadNpmTasks('grunt-sass');
  grunt.loadNpmTasks('grunt-contrib-watch');
  grunt.loadNpmTasks('grunt-pixrem');

  grunt.registerTask('build', ['sass', 'pixrem', 'uglify']);
  grunt.registerTask('default', ['build','watch']);
};
