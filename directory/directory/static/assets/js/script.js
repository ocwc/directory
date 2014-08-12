jQuery(document).ready(function($) {
    /* navigation menu */
    var ww = document.body.clientWidth;
    if (ww < 640) {
        $(".menu > li > a").click(function() {
            $(this).parent("li").toggleClass('hover');
            return false;
        });
    } else {
        $('.menu li').hover(function() {
            $(this).addClass('hover');
        }, function() {
            $(this).removeClass('hover');
        });
    }

    $('.toggle-menu').click(function(){
        $('.menu').toggle();
    });
	
});