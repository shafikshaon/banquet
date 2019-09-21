$(function () {
    let current_link = window.location.pathname;

    let link_list = $(".nav-link");

    $.each(link_list, function (k, value) {
        let link = $(value).attr('href');
        if (current_link === link) {
            $(value).addClass('active');
        }
    })
});