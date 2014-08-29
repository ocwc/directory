jQuery(document).ready(function($) {
    $('.facets dt').click(function(){
        $(this).parent('dl').toggleClass('selected-false');
    });

    $('.expertise dt').click(function(){
        $(this).parent('dl').toggleClass('selected-false');
    });
});