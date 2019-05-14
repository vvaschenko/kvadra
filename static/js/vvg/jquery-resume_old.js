jQuery(document).ready(function () {
    $(".btn").on('click', function () {
        // let myTable = document.getElementById(event.target.id);
        // var myString = myTable.parentNode;
        let myString = $(this).parents('tr');
        let cell = [];

        for (let i = 0, len = myString[0].childElementCount; i < len; i++) {
            cell[i] = myString[0].cells[i].textContent;
        }

        let server_name = cell[0],
            name = cell[1],
            info = cell[3];

        let data={ server_name:server_name, name:name, info:info,};
        $.postJSON('', data, function (results) {

            $("#myModal.modal-body").html("<p>траттататат</p>");
            // $.myModal("<div><h1>Ответ от сервера:</h1></div>");

        });
    });


    jQuery.postJSON = function (url, args, callback) {
        args.csrfmiddlewaretoken = getCookie('csrftoken');
        $.ajax({
            url: url, data: $.param(args), dataType: "text", type: "POST",
            success: function (results) {
                if (callback) callback(eval("(" + response + ")"));
            }, error: function (response) {
                console.log("ERROR:", response);
            }
        });
    }

    function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        let cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            let cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

});



