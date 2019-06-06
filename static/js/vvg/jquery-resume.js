jQuery(document).ready(function () {
    let data = {};
    data.csrfmiddlewaretoken = getCookie('csrftoken');

    $(".btn.btn-append.btn-sm").on('click', function (e) {
        e = e || window.event;
        e.preventDefault();
        // let data = {};

        let submit_btn = document.getElementById(e.target.id);
        data.server_name = submit_btn.dataset.server_name;
        data.name = submit_btn.dataset.name;
        data.info = submit_btn.dataset.info;
        data.rs_locale = submit_btn.dataset.locale;
        $("#otvet").remove();
        // data = {server_name: server_name, name: name, info: info,};

        $.ajax({
            url: 'dsi/',
            type: 'POST',
            data: data,
            success: function (data) {
                $(".modal-body").html('<h4 id = "otvet">' + data.otvet + '</h4>');
                // $(".modal-body").append('<p>'+ data.otvet + '</p>');
            },
            error: function (xhr, status, error) {
                alert('Возникла ошибка: ' + +xhr.responseText);
            }
        })
    });

// Надо переписать обработку конпки не по класу а по функции onclick = function (id)
    $(".btn.btn-info.btn-sm").on('click', function (e) {
        e = e || window.event;
        e.preventDefault();
        // let data = {};
        // $(".modal-title").html('<h4 class="modal-title">Error log</h4>');

        let submit_btn = document.getElementById(e.target.id);
        data.server_name = submit_btn.dataset.server_name;
        // data.server_name = 'abankcp866_rs';
        data.name = submit_btn.dataset.name;
        data.id = submit_btn.dataset.id;
        data.regim = submit_btn.dataset.regim;
        $("#otvet").remove();

        $.ajax({
            url: 'foolinfo_rs/',
            type: 'POST',
            data: data,
            beforeSend: function () {
                $('.modal-body').html('<div class="row" align="center" id="spiner"><p>Подготовка информации</p><img id="imgcode" src="' + static_url + 'ajax-loader.gif" ></div>');
            },
            success: function (data) {
                // $("#spiner").remove();
                $(".modal-body").html('<div class="row"><div class="col-md-12" id="otvet"></div></div>');

                // $.each(data.log,function () {
                //     $("#otvet").append('<p>'+this+'</p>');
                $("#otvet").html('<p>Подробная информация о выбраном сервере</p>');
                //
                //             });
                // scroll_bottom(1);
                // $(".modal-body").append('<p>'+ data.otvet + '</p>');
            },
            error: function (xhr, status, error) {
                alert('Возникла ошибка: ' + +xhr.responseText);
            }
        });

    });


    // $(".btn.btn-primary.btn-sm").on('click', function (e) {
    //     e = e || window.event;
    //     e.preventDefault();
    //     // let data = {};
    //     // let data = {};
    //     // data.csrfmiddlewaretoken = getCookie('csrftoken');
    //     let submit_btn = document.getElementById(e.target.id);
    //     data.server_name = submit_btn.dataset.server_name;
    //     data.name = submit_btn.dataset.name;
    //     data.info = submit_btn.dataset.info;
    //     data.rs_locale = submit_btn.dataset.locale;
    //     data.regim = submit_btn.dataset.regim;
    //     let regimr = data.regim;
    //     $("#otvet").remove();
    //     // data = {server_name: server_name, name: name, info: info,};
    //     // data.csrfmiddlewaretoken = getCookie('csrftoken');
    //
    //     $.ajax({
    //         url: 'dsi/',
    //         type: 'POST',
    //         data: data,
    //         success: function (data, textStatus, XHR) {
    //             if (regimr === XHR.responseJSON.nameobj) {
    //                 // $(".modal-body").html('<h4 id = "otvet">' + data.otvet + '</h4>');
    //                 $("#logview").html('<h4 id = "otvet">' + data.otvet + '</h4>');
    //                 // $(".modal-body").append('<p>'+ data.otvet + '</p>');
    //                 regimr = '';
    //             }
    //         },
    //         error: function (xhr, status, error) {
    //             alert('Возникла ошибка: ' + +xhr.responseText);
    //         }
    //     });
    //     $('#myModal').on('hide.bs.modal', function (e) {
    //         $("#ol_mini").remove();
    //         $("#otvet").remove();
    //     });
    // });

    $(".btn.btn-danger.btn-sm").on('click', function (e) {
        e = e || window.event;
        e.preventDefault();
        // let data = {};
        // data.csrfmiddlewaretoken = getCookie('csrftoken');
        // let data = {};
        // $(".modal-title").html('<h4 class="modal-title">Error log</h4>');

        let submit_btn = document.getElementById(e.target.id);
        data.server_name = submit_btn.dataset.server_name;
        // data.server_name = 'p24_rs';
        data.name = submit_btn.dataset.name;
        data.info = submit_btn.dataset.info;
        // data.info = 'P48DEPOSIT.ODB_UA';

        data.rs_locale = submit_btn.dataset.locale;
        data.regim = submit_btn.dataset.regim;
        let regimd = data.regim;
        $("#ol_mini").remove();
        $("#otvet_log").remove();
        // data = {server_name: server_name, name: name, info: info,};
        // data.csrfmiddlewaretoken = getCookie('csrftoken');
        // $('.modal-body').html('<div class="row" align="center" id="spiner"><p>Чтение лога test</p><img id="imgcode" src="' + static_url + 'ajax-loader.gif" ></div>');
        $.ajax({
            url: 'dsi/',
            type: 'POST',
            data: data,
            beforeSend: function () {
                $('#logview_log').html('<div class="row" align="center" id="spiner"><p>Чтение лога</p><img id="imgcode" src="' + static_url + 'ajax-loader.gif" ></div>');
            },
            success: function (data, textStatus, XHR) {
                // $("#spiner").remove();
                $("#logview_log").html('<div class="row"><div class="col-md-12" id="otvet_log"></div></div>');
                if (regimd === XHR.responseJSON.nameobj) {
                    $.each(data.log, function () {
                        $("#otvet_log").append('<p>' + this + '</p>');
                    });
                    // scroll_bottom(1);
                    scroll_to_bottom_log(1);
                    regimd = '';
                }
                // else {
                //     $("#logview_log").html('<div class="row"><div class="col-md-12" id="otvet_log"></div></div>');
                // }
                // $(".modal-body").append('<p>'+ data.otvet + '</p>');
            },
            error: function (xhr, status, error) {
                alert('Возникла ошибка: ' + +xhr.responseText);
            }
        });
        $('#myModallog').on('hide.bs.modal', function (e) {
            $("#ol_mini").remove();
            $("#otvet_log").remove();
        });
    });


    $(".checkbox_bids").on("click", function (e) {
        e = e || window.event;
        data.csrfmiddlewaretoken = getCookie('csrftoken');
        usercheckbox = document.getElementById(e.target.id);
        data.zp_id = usercheckbox.dataset.zp_id;
        data.regim = "bids_check";
        if (usercheckbox.checked) {
            data.workbids = 1;
        } else {
            data.workbids = 0;
        }

        $.ajax({
            url: '/bids/bids/',
            type: 'POST',
            data: data,
            success: function (data) {
            },
            error: function (xhr, status, error) {
                alert('Возникла ошибка: ' + +xhr.responseText);
            }
        })

    });

    $(".my_checkbox").on("click", function (e) {
        e = e || window.event;
        // e.preventDefault();
        // let data = {};
        let rowtable, cur_class;
        let my_url;
        // data.csrfmiddlewaretoken = getCookie('csrftoken');
        usercheckbox = document.getElementById(e.target.id);
        data.userdsi = usercheckbox.dataset.check_username;
        data.server_name = usercheckbox.dataset.check_servname;
        data.name = usercheckbox.dataset.check_name;
        data.info = usercheckbox.dataset.check_info;
        data.regim = usercheckbox.dataset.check_regim;
        data.workid = usercheckbox.dataset.check_workid;
        rowtable = usercheckbox.parentElement.parentElement;

        switch (data.regim) {
            case "dsi":
                my_url = 'dsi/';
                cur_class = 'odd';
                break;
            case "query":
                my_url = 'query/';
                cur_class = 'even';
                break;
            case "partition":
                my_url = 'partition/';
                cur_class = 'even';
                break;
        }

        if (usercheckbox.checked) {
            data.workdsi = 1;
            rowtable.className = 'info';
            rowtable.cells[0].innerText = data.userdsi;
        } else {
            data.workdsi = 0;
            rowtable.className = cur_class;
            rowtable.cells[0].innerText = "";

        }

        $.ajax({
            url: my_url,
            type: 'POST',
            data: data,
            success: function (data) {

                // console.log(data.success);

                // $('#name_query').find('option:not(:first)').remove();
                // // $('#name_query').append('<option value="0">Выберите очередь</option>');
                // $.each(data.query_list, function () {
                //     $('#name_query').append('<option value="' + this + '">' + this + '</option>');
                // });
                // $('#name_query')[0].selected = true;

                // $('#graph').remove();
            },
            error: function (xhr, status, error) {
                alert('Возникла ошибка: ' + +xhr.responseText);
            }
        });

    });
    // $(document).on('dblclick', '.servername', function (e) {
    //     e = e || window.event;
    //     // e.preventDefault();
    //     // let cur_id = e.target.attributes.id.value;
    //     // let test_id = e.target.id;
    //     // let myselect = document.getElementById(e.target.id);
    //     // showgraph(myselect.id)
    //     showgraph(e.target.id)
    // });
});


$('parent_element').on('change', '.qty', function () {
});