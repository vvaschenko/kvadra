/**
 * Created by dn111171vvg on 16.06.17.
 */

jQuery(document).ready(function () {


    let data = {};
    let dsirepbuttontimer = null
    let name_rs = "";
    let query = "";
    let allsize = "";
    let lstzero = 0;
    data.zero = 0;
    data.query = "";
    data.instance = "";
    data.name_instance = "";
    data.rate = "";
    data.limit_strok = "50";
    data.viewpartition = 0;
    data.viewquery = 0;
    var loganalyze_backdata;
    let submit_btn, kluch;
    $("#load_log").prop('disabled', true);
    $("#log_analyze_tab").addClass('hidden');


    $("#dsirepagentparams").on('click', function () {


        //instance = document.getElementById('instance');
        //name_rs = document.getElementById('name_rs');
        //name_instance = document.getElementById('name_instance');
        senddata = {}
        senddata.csrfmiddlewaretoken = getCookie('csrftoken');
        senddata.instance = document.getElementById('instance').value;
        senddata.name_rs = document.getElementById('name_rs').value;
        senddata.name_instance = document.getElementById('name_instance').value;
        $('#ModalViewDSIREPParams .modal-title').html('View ' + $.trim(senddata.instance) == "DSI EXEC" ? "REP AGENT" : "DSI"
            + senddata.name_instance + ' parameters')
        $('#ModalViewDSIREPParams').modal('show');
        $("#dsirepagentparams").prop('disabled', true);
        dsirepbuttontimer = setTimeout(function () {
            $("#dsirepagentparams").prop('disabled', false);
        }, 60000);

        $.ajax({
            url: '/graph/graph_repagent_params/',
            type: 'POST',
            data: senddata,
            beforeSend: function () {

                $("#view_dsirepparams").html('<div align="center"><p>Тут будут показаны параметры по </p><p>' +
                    senddata.instance + " " + senddata.name_instance + '</p><p><img id="imgcode" src="'
                    + static_url + 'ajax-loader.gif" ></p></div>');

            },
            success: function (data) {
                if (data != null && data.hasOwnProperty('html') && data.html != null) {
                    $("#view_dsirepparams").html(data.html);
                } else {
                    $("#view_dsirepparams").html('<div align="center"><p>Ошибка при нахождении параметров</p></div>');
                }
                //$("#dsirepagentparams").prop('disabled', false);
            },
            error: function (xhr, status, error) {
                alert('Возникла ошибка: Ошибка получения данных -' + xhr.responseText);
            }
        })
    })

    $("#repserverparams").on('click', function () {


        senddata = {}
        senddata.csrfmiddlewaretoken = getCookie('csrftoken');
        senddata.name_rs = document.getElementById('name_rs').value;
        $('#ModalViewDSIREPParams .modal-title').html('View ' +  senddata.name_rs + ' parameters')
        $('#ModalViewDSIREPParams').modal('show');
        $("#repserverparams").prop('disabled', true);
        dsirepbuttontimer = setTimeout(function () {
            $("#repserverparams").prop('disabled', false);
        }, 60000);

        $.ajax({
            url: '/graph/graph_repserver_params/',
            type: 'POST',
            data: senddata,
            beforeSend: function () {

                $("#view_dsirepparams").html('<div align="center"><p>Тут будут показаны параметры по </p><p>' +
                    senddata.instance + " " + senddata.name_instance + '</p><p><img id="imgcode" src="'
                    + static_url + 'ajax-loader.gif" ></p></div>');

            },
            success: function (data) {
                if (data != null && data.hasOwnProperty('html') && data.html != null) {
                    $("#view_dsirepparams").html(data.html);
                } else {
                    $("#view_dsirepparams").html('<div align="center"><p>Ошибка при нахождении параметров</p></div>');
                }
                //$("#dsirepagentparams").prop('disabled', false);
            },
            error: function (xhr, status, error) {
                alert('Возникла ошибка: Ошибка получения данных -' + xhr.responseText);
            }
        })
    })


    $("#name_rs_log").on('change', function (e) {
        submit_btn = document.getElementById(e.target.id);
        data.name_rs = submit_btn.value;

        $("#filterlog")[0].value = "";
        $("#mini").remove();
        $("#analyze_log").prop('disabled', true);
        $("#log_analyze_tab").addClass('hidden');

        $("#load_log").prop('disabled', false);
        loganalyze_backdata = null;
        $("#log_analyze_result").html("");

    });

    $("#limit_strok").on('change', function (e) {
        submit_btn = document.getElementById(e.target.id);
        data.limit_strok = submit_btn.value;

        $("#filterlog")[0].value = "";

        $("#mini").remove();
        $("#analyze_log").prop('disabled', true);
        $("#load_log").prop('disabled', false);
        loganalyze_backdata = null;
        $("#log_analyze_result").html("");
        $("#log_analyze_tab").addClass('hidden');


    });


    $("#load_log").on('click', function (e) {
        e = e || window.event;
        e.preventDefault();
        data.csrfmiddlewaretoken = getCookie('csrftoken');
        data.log = '';
        name_rs = submit_btn.value;
        data.reg_log = 'logrs';
        if (data.limit_strok === "all")
            data.limit = 0;
        else
            data.limit = 1;

        $("#filterlog")[0].value = "";

        $('#log_errorlog_tab [href="#tab1"]').tab('show');

        $.ajax({
            url: '/logrs/logrsall/',
            type: 'POST',
            data: data,
            beforeSend: function () {
                $('#logview').html('<div class="row mt-5"><div align="center"><p>Чтение лога </p><img id="imgcode" src="' + static_url + 'ajax-loader.gif" ></div></div>');
            },

            success: function (data) {
                $("#load_log").prop('disabled', true);
                loganalyze_backdata = data.log;

                $("#analyze_log").prop('disabled', false);

                // alert("Выбран сервер: "+name_rs);
                $('#logview').html('<p align="center">Файл лога вычитан</p>');
                $("#logview").remove();
                drawhtml();
                // tablehtml();
                $("#container").remove();
                $("#logview").html('<div class="row"><div class="col-md-12" id="mini"><ol id="ol_mini"></ol></div></div>');
                // $("#logtable").html('<tbody id="logstring"></tbody>');

                $.each(data.log, function () {
                    if ((this[0] === 'E' && this[1] === '.') || (this[0] === 'H' && this[1] === '.') || (this.substr(24, 15) === 'SySAM: WARNING:') || (this.substr(24, 12) === 'Still trying')) {
                        mystr = '<li style="color:red">' + this + '</li>';

                        // mystr = '<tr><td style="color:red">' + this + '</td></tr>';

                        $('#ol_mini').append(mystr);
                        // $('#mini').append(mystr + '<br>');
                    } else {
                        if (this[0] === 'W' && this[1] === '.') {
                            mystr = '<li style="color:#ffc107">' + this + '</li>';
                            $('#ol_mini').append(mystr);
                        } else {
                            mystr = this;
                            $('#ol_mini').append('<li>' + ekran(mystr) + '</li>');
                            // $('#mini').append('<span>' + ekran(mystr) + '<br></span>');
                        }
                    }
                });
                // if (data.log.length > 8000){
                if (data.log.length > 5000) {
                    filterbiglog();
                } else {
                    filtersmalllog();
                }


                scroll_to_bottom(1);
            },
            error: function (xhr, status, error) {
                alert('Возникла ошибка: Ошибка чтения лог файла -' + xhr);
                $("#load_log").prop('disabled', false);
                $("#logview").remove();
                $("#log_analyze_tab").addClass('hidden');

            }

        });

        // setTimeout(viewlogall, 2000);

    });

    $("#name_rs").on('change', function (e) {
            e = e || window.event;
            e.preventDefault();

            data.csrfmiddlewaretoken = getCookie('csrftoken');
            data.log = '';

            submit_btn = document.getElementById(e.target.id);
            kluch = submit_btn.dataset.regim;
            $("#container").remove();

            switch (kluch) {
                case "logrs":

                    break;
                case "partition":
                    data.name_rs = submit_btn.value;
                    name_rs = submit_btn.value;

                    $.ajax({
                        url: 'partition/',
                        type: 'POST',
                        data: data,
                        beforeSend: function () {
                            $('#logview_graph').html('<div align="center"><p>Получение данных для графика</p><img id="imgcode" src="' + static_url + 'ajax-loader.gif" ></div>');
                        },

                        success: function (data) {
                            $('#logview_graph').html('<div align="center"><p>Данные получены</p></div>');
                            $("#logview_graph").remove();
                            drawhtml_graph();

                            testgraph(data, name_rs, 'partition');
                            // graph(data, name_rs);
                            // $("#graph").load('graph/graph.html');
                        },
                        error: function (xhr, status, error) {
                            alert('Возникла ошибка: Ошибка получения данных -' + xhr.responseText);
                            $("#logview_graph").remove();
                        }
                    });
                    break;
                case "query":
                    data.name_rs = submit_btn.value;
                    name_rs = submit_btn.value;
                    delete data.query;
                    // $('#graph').remove();

                    $.ajax({
                        url: 'query/',
                        type: 'POST',
                        data: data,
                        success: function (data) {
                            let options = '';
                            $('#name_query').find('option:not(:first)').remove();
                            // $('#name_query').append('<option value="0">Выберите очередь</option>');
                            $.each(data.query_list, function () {
                                $('#name_query').append('<option value="' + this + '">' + this + '</option>');
                            });
                            $('#name_query')[0].selected = true;
                            // $('#graph').remove();
                        },
                        error: function (xhr, status, error) {
                            alert('Возникла ошибка: Ошибка получения данных -' + xhr.responseText);
                        }
                    });
                    break;
                case "repagent":
                    data.name_rs = submit_btn.value;
                    name_rs = submit_btn.value;
                    delete data.name_instance;
                    clearTimeout(dsirepbuttontimer);

                    // let options = '';
                    $('#instance').find('option:not(:first)').remove();
                    $('#instance').append('<option value="REP AGENT">REP AGENT</option>');
                    $('#instance').append('<option value="DSI EXEC">DSI EXEC</option>');
                    $('#instance')[0].selected = true;
                    $('#instance').enable();
                    // data.rate = submit_btn.value;
                    // name_rs = submit_btn.value;
                    // delete data.rate;
                    // $('#rate').find('option:not(:first)').remove();
                    // $('#rate').append('<option value="Obs">Obs</option>');
                    // $('#rate').append('<option value="Rate">Rate x/sec</option>');
                    // $('#rate')[0].selected = true;
                    // $('#rate')[0].disabled = true;
                    $('#name_instance')[0].disabled = true;
                    $('#name_instance').find('option:not(:first)').remove();

                    $("#dsirepagentparams").addClass('hidden');
                    $("#dsirepagentparams").prop('disabled', true);

                    break;
                case "repserver":
                    data.name_rs = submit_btn.value;
                    name_rs = submit_btn.value;
                    // delete data.name_instance;
                    // $('#repserverst').find('option:not(:first)').remove();
                    // $('#repserverst').append('<option value="REP AGENT">REP AGENT</option>');
                    // $('#repserverst').append('<option value="DSI EXEC">DSI EXEC</option>');
                    // $('#repserverst')[0].selected = true;
                    // $('#repserverst').enable();
                    data.csrfmiddlewaretoken = getCookie('csrftoken');
                    name_grph = data.name_rs;
                    $("#repserverparams").prop('disabled', true);
                    $.ajax({
                        url: 'graph_repagent/',
                        type: 'POST',
                        data: data,
                        beforeSend: function () {
                            $('#logview_graph').html('<div align="center"><p>Получение данных для графика</p><img id="imgcode" src="' + static_url + 'ajax-loader.gif" ></div>');
                        },
                        success: function (data) {
                            $('#logview_graph').html('<div align="center"><p>Данные получены</p></div>');
                            $("#logview_graph").remove();
                            $("#repserverparams").removeClass('hidden');
                            $("#repserverparams").prop('disabled', false);
                            drawhtml_graph();
                            // testgraph(data, name_grph, 'repagent');
                            testgraph2(data, name_grph, 'repagent');
                        },
                        error: function (xhr, status, error) {
                            alert('Возникла ошибка: Ошибка получения данных -' + xhr.responseText);
                            $("#logview_graph").remove();
                            $("#repserverparams").addClass('hidden');
                            $("#repserverparams").prop('disabled', true);
                        }
                    });

                    break;

            }
        }
    );
    // $('#repserverst').on('change', function (e2) {
    //     instans = document.getElementById(e2.target.id);
    //     data.instance = instans.value;
    //     data.csrfmiddlewaretoken = getCookie('csrftoken');
    //     instance = document.getElementById('name_rs');
    //     data.name_rs = instance.value;
    //     name_grph = instance.value + " - " + instans.value;
    //     // delete data.name_instance;
    //     $.ajax({
    //         url: 'graph_repagent/',
    //         type: 'POST',
    //         data: data,
    //         beforeSend: function () {
    //             $('#logview_graph').html('<div align="center"><p>Получение данных для графика</p><img id="imgcode" src="' + static_url + 'ajax-loader.gif" ></div>');
    //         },
    //         success: function (data) {
    //             $('#logview_graph').html('<div align="center"><p>Данные получены</p></div>');
    //             $("#logview_graph").remove();
    //             drawhtml_graph();
    //             // testgraph(data, name_grph, 'repagent');
    //             testgraph2(data, name_grph, 'repagent');
    //         },
    //         error: function (xhr, status, error) {
    //             alert('Возникла ошибка: Ошибка получения данных -' + xhr.responseText);
    //             $("#logview_graph").remove();
    //         }
    //     })
    //
    // });

    $('#instance').on('change', function (e2) {
        instans = document.getElementById(e2.target.id);
        data.instance = instans.value;
        data.csrfmiddlewaretoken = getCookie('csrftoken');
        delete data.name_instance;
        clearTimeout(dsirepbuttontimer);


        $("#dsirepagentparams").addClass('hidden');
        $("#dsirepagentparams").prop('disabled', true);

        $.ajax({
            url: 'graph_repagent/',
            type: 'POST',
            data: data,
            success: function (data) {

                let options = '';
                $('#name_instance').find('option:not(:first)').remove();
                // $('#name_query').append('<option value="0">Выберите очередь</option>');
                $.each(data.query_list, function () {
                    $('#name_instance').append('<option value="' + this + '">' + this + '</option>');
                });
                $('#name_instance')[0].selected = true;
                // $('#graph').remove();
                $('#name_instance').enable();
            },
            error: function (xhr, status, error) {
                alert('Возникла ошибка: Ошибка получения данных -' + xhr.responseText);
            }
        });
    });

    $("#graph").searcher({
        itemSelector: "li",
        textSelector: "", // the text is within the item element (li) itself
        inputSelector: "#filterlog"

    });


    $("input:checkbox").bind("change click", function () {
        if (this.checked)
            data.zero = 1;
        else
            data.zero = 0;

        if (name_rs !== "") {
            delete data.query;
            $.ajax({
                url: 'query/',
                type: 'POST',
                data: data,
                success: function (data) {
                    let options = '';
                    $('#name_query').find('option:not(:first)').remove();
                    // $('#name_query').append('<option value="0">Выберите очередь</option>');
                    $.each(data.query_list, function () {
                        $('#name_query').append('<option value="' + this + '">' + this + '</option>');
                    });
                    $('#name_query')[0].selected = true;

                    // $('#graph').remove();
                },
                error: function (xhr, status, error) {
                    alert('Возникла ошибка: Ошибка получения данных -' + xhr.responseText);
                }
            });
        }

        // console.log(data.zero);

        // do something
    });


    $('#name_instance').on('change', function (e_ins) {
        e_ins = e_ins || window.event;
        e_ins.preventDefault();
        clearTimeout(dsirepbuttontimer);
        // let data = {};
        // let name_rs = "";
        // let query = "";
        data.csrfmiddlewaretoken = getCookie('csrftoken');
        s_name_ins = document.getElementById(e_ins.target.id);
        // rate = document.getElementById('rate');
        // data.rate = rate.value;
        instance = document.getElementById('instance');
        data.instance = instance.value;
        data.name_instance = s_name_ins.value;
        name_grph = instance.value + " - " + s_name_ins.value;
        $.ajax({
            url: 'graph_repagent/',
            type: 'POST',
            data: data,
            beforeSend: function () {
                $('#logview_graph').html('<div align="center"><p>Получение данных для графика</p><img id="imgcode" src="' + static_url + 'ajax-loader.gif" ></div>');
                $("#dsirepagentparams").addClass('hidden');
                $("#dsirepagentparams").prop('disabled', true);
            },
            success: function (data) {
                $('#logview_graph').html('<div align="center"><p>Данные получены</p></div>');
                $("#logview_graph").remove();
                drawhtml_graph();
                testgraph(data, name_grph, 'repagent');
                // graph(data, name_rs);
                // $("#graph").load('graph/graph.html');
                $("#dsirepagentparams").removeClass('hidden');
                $("#dsirepagentparams").prop('disabled', false);
            },
            error: function (xhr, status, error) {
                alert('Возникла ошибка: Ошибка получения данных -' + xhr.responseText);
                $("#logview_graph").remove();
            }
        })


    });

    $('#name_query').on('change', function (ee) {
        ee = ee || window.event;
        ee.preventDefault();
        // let data = {};/logrs/logrsall/
        // let name_rs = "";
        // let query = "";
        data.csrfmiddlewaretoken = getCookie('csrftoken');

        let select2 = document.getElementById(ee.target.id);
        data.query = select2.value;
        query = select2.value;
        $.ajax({
            url: 'query/',
            type: 'POST',
            data: data,
            beforeSend: function () {
                $('#logview_graph').html('<div align="center"><p>Получение данных для графика</p><img id="imgcode" src="' + static_url + 'ajax-loader.gif" ></div>');
            },

            success: function (data) {
                $('#logview_graph').html('<div align="center"><p>Данные получены</p></div>');
                $("#logview_graph").remove();
                drawhtml_graph();
                testgraph(data, query, 'query');
                // graph(data, name_rs);
                // $("#graph").load('graph/graph.html');
            },
            error: function (xhr, status, error) {
                alert('Возникла ошибка: Ошибка получения данных -' + xhr.responseText);
                $("#logview_graph").remove();
            }
        });
    });

    $("#analyze_log").on('click', function (e) {
        e = e || window.event;
        e.preventDefault();
        data.csrfmiddlewaretoken = getCookie('csrftoken');
        if (loganalyze_backdata !== null) {
            data.loganalyze_backdata = loganalyze_backdata.join();
            ;
        } else {
            data.loganalyze_backdata = $('#logview #ol_mini').text();
        }
        data.reg_log = 'analyzelog';
        $("#log_analyze_tab").removeClass('hidden');
        $('#log_analyze_tab [href="#tab2"]').tab('show');

        $.ajax({
            url: '/logrs/analyzelog/',
            type: 'POST',
            data: data,
            beforeSend: function () {
                $('#log_analyze_result').html('<div class="row mt-5"><div align="center"><p>Анализ лога </p><img id="imgcode" src="' + static_url + 'ajax-loader.gif" ></div></div>');
            },

            success: function (data) {
                $('#log_analyze_result').html(data.log);
                $("#analyze_log").prop('disabled', true);
            },


            error: function (xhr, status, error) {
                alert('Возникла ошибка: Ошибка анализа лог файла -' + xhr);
                $("#analyze_log").prop('disabled', false);
                $("#log_analyze_result").html("");
            }

        });


    });

})
;


