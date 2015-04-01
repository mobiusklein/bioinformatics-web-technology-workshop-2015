module.exports = function(grunt){
    grunt.initConfig({
        watch: {
            files: ["slides.md"],
            tasks: 'shell:bedeck'
        },
        shell: {
            bedeck: {
                command: "bedecked --theme simple --opt-slide-number true slides.md > slides.html"
            }
        }
    })
    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.loadNpmTasks('grunt-shell')
    grunt.registerTask('default', ['shell:bedeck', 'watch']);
}
