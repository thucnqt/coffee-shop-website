// hàm hiển thị vật thể khi kéo tới

function AnimationOnScroll() {
    $('.on-scroll').each(function () {
        var ObjPosition = $(this).offset().top;
        var topOfWindow = $(window).scrollTop();
        var ScreenHeight = screen.height;
        if (ObjPosition - topOfWindow < ScreenHeight) {
            $(this).removeClass('on-scroll')
            $(this).addClass('animation');
        }
    });
};

AnimationOnScroll()
$(window).scroll(function() {AnimationOnScroll()});