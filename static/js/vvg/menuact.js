$(document).ready(function () {
    var url = document.location.href;
    $.each($(".menunumber a"), function () {
        if (this.href == url) {
            $(this.parentElement.parentElement)[0].style.display = 'block';
            $(this).addClass('active');
        }
    });
});
