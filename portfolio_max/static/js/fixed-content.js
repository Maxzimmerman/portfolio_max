$(function () {
    $(".overview-about").hover(function () {
        $(".overview-item-about").animate({
            width: "40px"
        }, 100)
        $(".overview-link-about").animate({
            marginLeft: "50px"
        }, 100)
    }, function () {
        $(".overview-item-about").animate({
            width: "10px"
        }, 100)
        $(".overview-link-about").animate({
            marginLeft: "12px"
        }, 100)
    })

    $(".overview-experience").hover(function () {
        $(".overview-item-experience").animate({
            width: "40px"
        }, 100)
        $(".overview-link-experience").animate({
            marginLeft: "50px"
        }, 100)
    }, function () {
        $(".overview-item-experience").animate({
            width: "10px"
        }, 100)
        $(".overview-link-experience").animate({
            marginLeft: "12px"
        }, 100)
    })

    $(".overview-projects").hover(function () {
        $(".overview-item-projects").animate({
            width: "40px"
        }, 100)
        $(".overview-link-projects").animate({
            marginLeft: "50px"
        }, 100)
    }, function () {
        $(".overview-item-projects").animate({
            width: "10px"
        }, 100)
        $(".overview-link-projects").animate({
            marginLeft: "12px"
        }, 100)
    })

    $(".overview-contact").hover(function () {
        $(".overview-item-contact").animate({
            width: "40px"
        }, 100)
        $(".overview-link-contact").animate({
            marginLeft: "50px"
        }, 100)
    }, function () {
        $(".overview-item-contact").animate({
            width: "10px"
        }, 100)
        $(".overview-link-contact").animate({
            marginLeft: "12px"
        }, 100)
    })
})