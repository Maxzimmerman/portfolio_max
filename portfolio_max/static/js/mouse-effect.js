$(function () {
    const mousemover = document.querySelector(".cursor");

    window.onmousemove = function (s) {
        mousemover.style.top = s.clientY + "px";
        mousemover.style.left = s.clientX + "px";
    }
})