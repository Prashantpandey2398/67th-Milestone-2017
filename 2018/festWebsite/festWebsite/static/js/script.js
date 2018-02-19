$("#gallery2-k").prop("disabled", true);

function scroll(speed) {
    $('html, body').animate({ scrollTop: $(document).height() - $(window).height() }, speed, function() {
        $(this).animate({ scrollTop: 0 }, speed);
    });
}
speed = ($(window).width())/734*50000;
scroll(speed)
setInterval(function(){scroll(speed)}, speed * 2);

