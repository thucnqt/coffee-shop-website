
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
$(window).scroll(function () { AnimationOnScroll() });


// Hàm scroll down khi bấm nút
// Add smooth scrolling to the buton
$(".btn").on('click', function (event) {

    // Make sure this.hash has a value before overriding default behavior
    if (this.hash !== "") {
        // Prevent default anchor click behavior
        event.preventDefault();

        // Store hash
        var hash = this.hash;

        // Using jQuery's animate() method to add smooth page scroll
        // The optional number (800) specifies the number of milliseconds it takes to scroll to the specified area
        $('html, body').animate({
            scrollTop: $(hash).offset().top
        }, 1200, function () {

            // Add hash (#) to URL when done scrolling (default click behavior)
            window.location.hash = hash;
        });
    } // End if
});



