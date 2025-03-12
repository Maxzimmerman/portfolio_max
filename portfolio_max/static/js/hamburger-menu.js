$(function () {
    $('.hamburger-menu-content').slideUp(0);

    $('.hamburger-menu').on('click', function () {
        $('.hamburger-menu-content').slideToggle(100);
    });
});
