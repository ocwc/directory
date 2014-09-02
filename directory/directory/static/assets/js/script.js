jQuery(document).ready(function($) {
    $('.facets dt').click(function(){
        $(this).parent('dl').toggleClass('selected-false');
    });

    $('.expertise dt').click(function(){
        $(this).parent('dl').toggleClass('selected-false');
    });

    $('.form-group').each(function(index, el) {
        $(el).addClass('clearfix');
    });
});