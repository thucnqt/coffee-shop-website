// hàm slideshow

var myIndex = 0;
function slideshow() {
    var txt = ["The amazing flavors will blow your mind.","Since 2001 with you."][myIndex];
    var c = 0;
    document.getElementById("typing").innerHTML = ""
    function typeWriter() {
        if (c < txt.length) {
            document.getElementById("typing").innerHTML += txt.charAt(c);
            c++;
            setTimeout(typeWriter, 2000/txt.length);
        }
    };
    typeWriter();
    var i;
    var x = document.getElementsByClassName("banner-img");
    var t1 = document.getElementsByClassName("line1");
    var t2 = document.getElementsByClassName("line2");
    var t4 = document.getElementsByClassName("line4");
    for (i = 0; i < x.length; i++) {
        x[i].classList.remove("fading");
        t1[0].classList.remove("animation");
        t1[0].innerHTML = "";
        t2[0].classList.remove("animation");
        t2[0].innerHTML = "";
        t4[0].classList.remove("animation");
    };
    t1[0].innerHTML = ["welcome, enjoy the original","outstanding coffee"][myIndex];
    t1[0].classList.add("animation");
    t2[0].innerHTML = ["fresh porto coffee","expresso bar"][myIndex];
    t2[0].classList.add("animation");
    t4[0].classList.add("animation");
    x[myIndex].classList.add("fading");
    x[myIndex].style.zIndex = "1";
    if (myIndex > x.length - 2) {myIndex = -1};
    x[myIndex+1].style.zIndex = "0"
    myIndex++;
    setTimeout(slideshow, 10000);
    setTimeout(typeWriter, 8000)
};
slideshow();

// hàm header fixed khi kéo

var header = document.getElementById("header");
var logo = document.getElementById("header-logo");
var logoIMG = document.getElementById("logo-img");
var toppage = header.offsetTop;

function HeaderScroll() {
    if (window.pageYOffset > toppage) {
        header.classList.remove("header-still");
        logoIMG.classList.remove("logo-still");
        logo.classList.remove("header-vertical");
        header.classList.add("header-scroll");
        logoIMG.classList.add("logo-scroll");
    } else {
        header.classList.remove("header-scroll");
        logoIMG.classList.remove("logo-scroll");
        header.classList.add("header-still");
        logo.classList.add("header-vertical");
        logoIMG.classList.add("logo-still");
    };
};

window.onscroll = function() {HeaderScroll();colorheader();};

// hàm chạy header menu links

var Sects = document.getElementsByClassName("section");
var HeaderItems = document.getElementsByClassName("header-item");
var HeaderLinks = document.getElementsByClassName("header-link");
var sect = 0;

for (sect = 0; sect < Sects.length; sect++) {
    clickheader(HeaderItems[sect].id,Sects[sect].id);
    // colorheader(Sects[sect],HeaderLinks[sect]);
};

function clickheader(start,destination) {
    $("#"+start).click(function() {
        $('html').animate(
            {scrollTop: $("#"+destination).offset().top - $("#header").height()},
            'slow');
    });
}

function colorheader() {
    HeaderHeight = document.getElementById("header").offsetHeight
    for (sect = 0; sect < Sects.length; sect++) {
        section = Sects[sect];
        link = HeaderLinks[sect];
        if ((section.offsetTop - HeaderHeight < window.pageYOffset) &&
            (section.offsetTop - HeaderHeight + section.offsetHeight > window.pageYOffset)) {
            link.classList.add("brown");
            link.classList.remove("white");
        } else {
            link.classList.add("white");
            link.classList.remove("brown");
        };
    };
};

// jQuery: hàm hiển thị vật thể khi kéo tới

function AnimationOnScroll() {
    $('.on-scroll').each(function () {
        var ObjPosition = $(this).offset().top;
        var topOfWindow = $(window).scrollTop();
        var ScreenHeight = screen.height;
        if (ObjPosition - topOfWindow < ScreenHeight) {
            $(this).removeClass('on-scroll');
            $(this).addClass('animation');
        }
    });
};

AnimationOnScroll()
$(window).scroll(function() {AnimationOnScroll()});