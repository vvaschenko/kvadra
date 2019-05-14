// klick = 0;
function viewlogall() {
    let data_all = {};
    data_all.zero = 0;
    data_all.query = "";
    data_all.name_rs = submit_btn.value;
    name_rs = submit_btn.value;
    data_all.reg_log = 'logrs';
    data_all.limit = 0;
    data_all.csrfmiddlewaretoken = getCookie('csrftoken');
    data_all.log = '';
    $.ajax({
        url: 'logrsall/',
        type: 'POST',
        data: data_all,
        beforeSend: function () {
            $('#spinerview').html('<div align="center"><p>Чтение полного лога</p><img id="imgcode" src="' + static_url + 'ajax-loader.gif" ></div>');
        },

        success: function (data_all) {
            // alert("Выбран сервер: "+name_rs);
            $('#spinerview').html('<p>Файл лога вычитан</p>');
            $('#spinerview').html('<p></p>');
            $("#logview").remove();
            drawhtml();
            $("#container").remove();
            $("#logview").html('<div class="row"><div class="col-md-12" id="mini"></div></div>');
            $.each(data_all.log, function () {
                if ((this[0] === 'E' && this[1] === '.') || (this[0] === 'H' && this[1] === '.') || (this.substr(24, 15) === 'SySAM: WARNING:') || (this.substr(24, 12) === 'Still trying')) {
                    mystr = '<span style="color:red">' + this + '</span>';
                    $('#mini').append('<span>' + mystr + '<br><span>');
                }
                else {
                    mystr = this;
                    $('#mini').append('<span>' + ekran(mystr) + '<br><span>');
                }
            });
            scroll_to_bottom(1);
            // document.getElementById('graph').scrollIntoView(true);

        },
        error: function (xhr, status, error) {
            alert('Возникла ошибка: Ошибка чтения лог файла -' + xhr.responseText);
            $("#logview").remove();
        }
    });
}


function scroll_to_bottom(speed) {
    // let $jscroll = jQuery.noConflict();
    var height = $("body").height();
    $("html,body").animate({"scrollTop": height}, speed);
}

function scrollmoadl_to_bottom_log(speed) {
    let height = $("#mini").height();
    $("#myModallog").animate({"scrollTop": height}, speed);
}

function scroll_to_bottom_log(speed) {
    let height = $("#otvet_log").height();
    $("#myModallog").animate({"scrollTop": height}, speed);
}

function scroll_to_bottom_viewtran(speed) {

    let height = $("#trandetail").height();
    let height1 = $("#vtran").height();
    let height2 = $("#viewtran").height();

    $("#myModalViewTran").animate({"scrollTop": height2}, speed);
}

function scroll_to_bottom_pubsub(speed) {
    // let height = $("#trandetail").height();
    // let height1 = $("#vpubsub").height();
    // let height2 = $("#pubsub_view").height();
    let height3 = $("#viewpubsub").height();
    $('#ModalViewPubSub').animate({"scrollTop": height3}, speed);
}


function ekran(string) {

    let pos = 0;
    while (true) {
        let foundPos = string.indexOf("<", pos);
        if (foundPos == -1) break;
        start_str = string.substring(0, foundPos);
        end_str = string.substring(foundPos + 1);
        string = start_str + "&lt;" + end_str
        pos = foundPos + 1;
    }
    pos = 0;
    while (true) {
        let foundPos = string.indexOf(">", pos);
        if (foundPos == -1) break;
        start_str = string.substring(0, foundPos);
        end_str = string.substring(foundPos + 1);
        string = start_str + "&gt;" + end_str
        pos = foundPos + 1;
    }

    return string;
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

function link_rs(id) {
    let data = {};
    let currentelement = document.getElementById(id);
    data.linkrs = currentelement.dataset.linkrs;
    data.csrfmiddlewaretoken = getCookie('csrftoken');
    $.ajax({
        url: 'settings/',
        type: 'POST',
        data: data,
        success: function (data) {
            if (data.otvet === 1) {
                alert("связи получены");
            } else {
                alert(data.otvet);
            }
        },
        error: function (xhr, status, error) {
            alert('Возникла ошибка: Ошибка получения связей репсерверов -' + xhr.responseText);
            $("#logview").remove();
        }
    });
}

function clear_cach(id) {
    let data = {};
    let currentelement = document.getElementById(id);
    data.cach = currentelement.dataset.cach;
    data.csrfmiddlewaretoken = getCookie('csrftoken');
    $.ajax({
        url: 'settings/',
        type: 'POST',
        data: data,
        success: function (data) {
            if (data.otvet === '1') {
                alert("Кэш очишен");
            }
            else {
                alert(data.otvet);
            }
        },
        error: function (xhr, status, error) {
            alert('Возникла ошибка: Ошибка очистки кэша -' + xhr.responseText);
            $("#logview").remove();
        }
    });
}

function testgraph(data, namegraph, kluch) {
    let mydata = data;
    // let td1 = new Date(mydata.grsize[0][0]);
    // let td2 = new Date(mydata.grsize[mydata.grsize.length-1][0]);
    // let datestart = new Date(mydata.grsize[0][0]);
    // let dataend = new Date(mydata.grsize[mydata.grsize.length - 1][0]);
    let datestart = new Date(mydata.str_start);
    let dataend = new Date(mydata.str_end);

    allsize = "";
    let kl = kluch;
    let name = namegraph;
    switch (kl) {
        case 'partition':
            allsize = 'Общий размер партиций ' + mydata.grsizeall.totalsize;
            name_osy = 'текущий размер в mb';
            name = name + ' (Mb)';
            utcuse = false;
            break;
        case 'query':
            name_osy = 'текущий размер в mb';
            name = name + ' (Mb)';
            utcuse = false;
            break;
        case 'detail':
            name_osy = 'текущая задержка в мин';
            name = name + ' (задержка в мин) <br> период c ' + datestart.toLocaleString() + ' по ' + dataend.toLocaleString();
            utcuse = false;
            break;
        case 'repagent':
            name_osy = 'Скорость B/s';
            // name = name + ' (задержка в мин) <br> период c ' + datestart.toLocaleString() + ' по ' + dataend.toLocaleString();
            name = name + ' <br> скорость B/s ';
            utcuse = false;
            break;
    }

    Highcharts.setOptions({
        global: {
            useUTC: utcuse
        }
    });

    Highcharts.stockChart('container', {
        title: {
            text: name
        },

        subtitle: {
            text: allsize
        },

        rangeSelector: {
            buttons: [{
                type: 'hour',
                count: 1,
                text: '1h'
            }, {
                type: 'day',
                count: 1,
                text: '1D'
            }, {
                type: 'month',
                count: 1,
                text: '1m'
            }, {
                type: 'all',
                count: 1,
                text: 'All'
            }
            ],
            selected: 1,
            inputEnabled: false

        },
        yAxis: {
            min: 0,
            // max: 0.9,
            // startOnTick: false,
            // endOnTick: false
        },
        series: [{
            name: name_osy,
            type: 'area',
            data: mydata.grsize,
            // gapSize: 5,
            tooltip: {
                valueDecimals: 2
            },
            fillColor: {
                linearGradient: {
                    x1: 0,
                    y1: 0,
                    x2: 0,
                    y2: 1
                },
                stops: [
                    [0, Highcharts.getOptions().colors[0]],
                    [1, Highcharts.Color(Highcharts.getOptions().colors[0]).setOpacity(0).get('rgba')]
                ]
            },
            threshold: null
        }]
    });
}

function testgraph2(data, namegraph, kluch) {
    let mydata = data;
    // let td1 = new Date(mydata.grsize[0][0]);
    // let td2 = new Date(mydata.grsize[mydata.grsize.length-1][0]);
    // let datestart = new Date(mydata.grsize[0][0]);
    // let dataend = new Date(mydata.grsize[mydata.grsize.length - 1][0]);
    let datestart = new Date(mydata.str_start);
    let dataend = new Date(mydata.str_end);

    allsize = "";
    let kl = kluch;
    let name = namegraph;
    switch (kl) {
        case 'partition':
            allsize = 'Общий размер партиций ' + mydata.grsizeall.totalsize;
            name_osy = 'текущий размер в mb';
            name = name + ' (Mb)';
            utcuse = false;
            break;
        case 'query':
            name_osy = 'текущий размер в mb';
            name = name + ' (Mb)';
            utcuse = false;
            break;
        case 'detail':
            name_osy = 'текущая задержка в мин';
            name = name + ' (задержка в мин) <br> период c ' + datestart.toLocaleString() + ' по ' + dataend.toLocaleString();
            utcuse = false;
            break;
        case 'repagent':
            name_osy = 'Скорость B/s';
            // name = name + ' (задержка в мин) <br> период c ' + datestart.toLocaleString() + ' по ' + dataend.toLocaleString();
            name = name + ' <br> скорость B/s ';
            utcuse = false;
            break;
    }

    Highcharts.setOptions({
        global: {
            useUTC: utcuse
        }
    });

    Highcharts.stockChart('container', {
        title: {
            text: name
        },

        subtitle: {
            text: allsize
        },

        rangeSelector: {
            buttons: [{
                type: 'hour',
                count: 1,
                text: '1h'
            }, {
                type: 'day',
                count: 1,
                text: '1D'
            }, {
                type: 'month',
                count: 1,
                text: '1m'
            }, {
                type: 'all',
                count: 1,
                text: 'All'
            }
            ],
            selected: 1,
            inputEnabled: false

        },
        yAxis: {
            min: 0,
            // max: 0.9,
            // startOnTick: false,
            // endOnTick: false
        },
        legend: {
            enabled: true
        },
        series: [{
            name: "REP AGENT",
            type: 'area',
            data: mydata.grsize,
            // gapSize: 5,
            tooltip: {
                valueDecimals: 2
            },
            fillColor: {
                linearGradient: {
                    x1: 0,
                    y1: 0,
                    x2: 0,
                    y2: 1
                },
                stops: [
                    [0, Highcharts.getOptions().colors[0]],
                    [1, Highcharts.Color(Highcharts.getOptions().colors[0]).setOpacity(0).get('rgba')]
                ]
            },
            threshold: null
        },
            {
                name: "DSI EXEC",
                type: 'area',
                data: mydata.grsize2,
                // gapSize: 5,
                tooltip: {
                    valueDecimals: 2
                },
                fillColor: {
                    linearGradient: {
                        x1: 0,
                        y1: 0,
                        x2: 0,
                        y2: 1
                    },
                    stops: [
                        [0, Highcharts.getOptions().colors[0]],
                        [1, Highcharts.Color(Highcharts.getOptions().colors[0]).setOpacity(0).get('rgba')]
                    ]
                },
                threshold: null
            }
        ]
    });
}

function testgraph1(data, name_rs, kl) {
    let mydata = data;
    allsize = "";
    switch (kl) {
        case 'partition':
            allsize = 'Общий размер партиций ' + mydata.grsizeall.totalsize + 'Mb';
            name_osy = 'размер партиций';
            break;
        case 'query':
            name_osy = 'размер очереди';
            break;
    }

    // console.log(data);
    // Create the chart
    Highcharts.setOptions({
        global: {
            useUTC: false
        }
    });

    Highcharts.stockChart('container', {

        rangeSelector: {
            selected: 1
        },

        title: {
            text: name_rs
        },
        subtitle: {
            text: allsize
        },
        xAxis: {
            min: 0
        },
        series: [{
            name: name_osy,
            data: mydata.grsize,
            type: 'area',
            threshold: null,
            tooltip: {
                valueDecimals: 2
            },
            fillColor: {
                linearGradient: {
                    x1: 0,
                    y1: 0,
                    x2: 0,
                    y2: 1
                },
                stops: [
                    [0, Highcharts.getOptions().colors[0]],
                    [1, Highcharts.Color(Highcharts.getOptions().colors[0]).setOpacity(0).get('rgba')]
                ]
            }
        }]
    });
}

function drawhtml() {
    // let $jsdrawhtml = jQuery.noConflict();
    $("#graph").html(
        '<div class="col-md-12">' +
        '<div class="widget-wrap">' +
        '<div class="widget-container">' +
        '<div class="widget-content" id="logview">' +
        '<div class="nvd3-chart" id="container">' +

        '</div>' +
        '</div>' +
        '</div>' +
        '</div>' +
        '</div>'
    );
}

function drawhtml_graph() {
    // let $jsdrawhtml = jQuery.noConflict();
    $("#graph_graph").html(
        '<div class="col-md-12">' +
        '<div class="widget-wrap">' +
        '<div class="widget-container">' +
        '<div class="widget-content" id="logview_graph">' +
        '<div class="nvd3-chart" id="container">' +

        '</div>' +
        '</div>' +
        '</div>' +
        '</div>' +
        '</div>'
    );
}
function tablehtml() {
    $("#graph").html(
        '<div class="col-md-12">' +
        '<div class="widget-wrap">' +
        '<div class="widget-container">' +
        '<div class="widget-content" id="logview">' +
        '<table class="table data-tbl-logtable" id="logtable">' +
        '<tbody id="logstring">' +

        '</tbody>' +
        '</table>' +
        '</div>' +
        '</div>' +
        '</div>' +
        '</div>'
    );
}

function include(url) {
    let script = document.createElement('script');
    script.src = url;
    document.getElementsByTagName('head')[0].appendChild(script);
}

function filterbiglog() {
    // $('#filterlog').remove();
    // $('#poisk').html(
    //     '<label> Поиск: <input type="text"  id="poisklog"  ></label>'
    // );
    document.getElementById('poisk').style.visibility = "hidden";
    document.getElementById('search_block').style.visibility = "visible";
    // url = "/static/js/vvg/poisktext.js";
    // include(url);
}

function filtersmalllog() {
    // if ($("input").is("#poisklog")){
    //     $('#poisklog').remove();
    //     $('#poisk').html(
    //         '<label> Фильтр: <input type="text"  id="filterlog"  ></label>'
    //     );
    // }
    document.getElementById('poisk').style.visibility = "visible";
    document.getElementById('search_block').style.visibility = "hidden";
}

function showgraph(id) {
    // let $myjs = jQuery.noConflict();
    let data = {};
    let name_graph = "";
    let kluch_graph = "";
    let currentelement = document.getElementById(id);
    data.csrfmiddlewaretoken = getCookie('csrftoken');
    if (id.indexOf("server") === 0) {
        data.viewpartition = 1;
        data.viewquery = 0;
        data.server_name = currentelement.textContent;
        name_graph = data.server_name;
        kluch_graph = "partition";
    }
    if (id.indexOf("query") === 0) {
        data.viewpartition = 0;
        data.viewquery = 1;
        data.query = currentelement.textContent;
        data.server_name = currentelement.previousElementSibling.previousElementSibling.textContent;
        name_graph = data.query;
        kluch_graph = "query";
    }
    let mywindmodalold = document.getElementById('myModalquery');
    let mywindmodal = document.getElementById('myModalgraph');
    $(mywindmodalold).modal('hide');
    $(mywindmodal).modal('show');
    $.ajax(
        {
            url: 'graph/',
            type: 'POST',
            data: data,
            beforeSend: function () {
                $('#logview_graph').html('<div align="center"><p>Получение данных для графика  <span>' + name_graph + ' </span> </p><img id="imgcode" src="' + static_url + 'ajax-loader.gif" ></div>');
            },
        }
    ).success(function (data, textStatus, XHR) {
        if (name_graph === XHR.responseJSON.nameobj) {
            let data_partition = data;
            $('#logview_graph').html('<div align="center"><p>Данные получены</p></div>');
            $("#logview_graph").remove();
            drawhtml_graph();
            testgraph(data_partition, name_graph, kluch_graph);
            name_graph = "";
        }
    })
        .error(function (xhr, status, error) {
            alert('Возникла ошибка: Ошибка получения данных -' + xhr.responseText);
            $("#logview_graph").remove();
        });
    // $(mywindmodal).on('shown.bs.modal', function (e) {
    //     // $('.row').remove();
    //     // $('#').html('<div class="row" id="graph"><div class="widget-content" id="logview"></div></div>');
    //     $('#logview_graph').html('<div align="center"><p>Получение данных для графика  <span>' + name_graph + ' </span> </p><img id="imgcode" src="' + static_url + 'ajax-loader.gif" ></div>');
    //
    // });
    $(mywindmodal).on('hide.bs.modal', function (e) {
        $("#container").remove();
        $(mywindmodalold).modal('show');
    });

}

function showlog(id) {
    let data = {};
    let currentelement = document.getElementById(id);
    data.csrfmiddlewaretoken = getCookie('csrftoken');
    data.server_name = currentelement.textContent;
    let name_log = currentelement.textContent;
    data.regim = 'logrs';
    data.limit = 1;
    data.limit_strok = 300;
    let regim = data.regim;
    $("#ol_mini").remove();
    $("#otvet").remove();
    let mywindmodal = document.getElementById('myModallog');
    $(mywindmodal).modal('show');
    $(mywindmodal).on('shown.bs.modal', function (e) {
        if (regim === 'logrs') {
            $.ajax(
                {
                    url: 'logrsall/',
                    type: 'POST',
                    data: data,
                    beforeSend: function () {
                        // $(".modal-title").html('<h4 class="modal-title">Error log</h4>');
                        $('#logview_log').html('<div class="row" align="center" id="spiner"><p>Чтение лога</p><img id="imgcode" src="' + static_url + 'ajax-loader.gif" ></div>');
                    },
                    success: function (data, textStatus, XHR) {
                        if (regim === XHR.responseJSON.nameobj) {
                            $("#logview_log").html('<div class="row"><div class="col-md-12" id="otvet"></div></div>');
                            $("#otvet").html('<div class="row"><div class="col-md-12" id="mini"><ol id="ol_mini"></ol></div></div>');
                            $.each(data.log, function () {
                                if ((this[0] === 'E' && this[1] === '.') || (this[0] === 'H' && this[1] === '.') || (this.substr(24, 15) === 'SySAM: WARNING:')) {
                                    mystr = '<li style="color:red">' + this + '</li>';
                                    $('#ol_mini').append(mystr);
                                }
                                else {
                                    if (this[0] === 'W' && this[1] === '.') {
                                        mystr = '<li style="color:#ffc107">' + this + '</li>';
                                        $('#ol_mini').append(mystr);
                                    }
                                    else {
                                        mystr = this;
                                        $('#ol_mini').append('<li>' + ekran(mystr) + '</li>');
                                        // $('#mini').append('<span>' + ekran(mystr) + '<br></span>');
                                    }
                                }
                            });
                            scrollmoadl_to_bottom_log(1);
                            regim = "";
                        }
                    },
                    error: function (xhr, status, error) {
                        alert('Возникла ошибка: Ошибка получения данных -' + xhr.responseText);
                        $("#ol_mini").remove();
                        $("#otvet").remove();
                    }
                });
        }

    });
    $(mywindmodal).on('hide.bs.modal', function (e) {
        $("#ol_mini").remove();
        $("#otvet").remove();
    });
}


function scroll_bottom(speed) {
    var height = $("#otvet").height();
    $("#myModal").animate({"scrollTop": height}, speed);
}

function showquery(id) {
    let data = {};
    let otvetjson = "";
    let host_kl = "";
    var host = "";
    let currentelement = document.getElementById(id);
    data.csrfmiddlewaretoken = getCookie('csrftoken');
    data.info = currentelement.textContent;
    data.name = currentelement.dataset.name;
    data.source = currentelement.dataset.source;
    data.destin = currentelement.dataset.destin;
    data.destin_id = currentelement.dataset.destin_id;
    data.source_id = currentelement.dataset.source_id;
    data.server_name = currentelement.dataset.server_name;
    data.regim = 'showquery';
    data.delay = currentelement.dataset.delay;
    let query = data.info;
    let regim = data.regim;
    let mywindmodal = document.getElementById('myModalquery');
    if (regim === 'showquery') {
        $.ajax(
            {
                url: 'showquery/',
                type: 'POST',
                data: data,
                success: function (data, textStatus, XHR) {
                    if (regim === XHR.responseJSON.nameobj) {
                        if (data.queryname !== null) {
                            host = location.origin + "/mon/mon_query/" + data.queryname + "/";
                            $(mywindmodal).modal('show');
                            let arr = $('.modal-content');
                            for (let i = 0; i < arr.length; ++i) {
                                if (arr[i].parentElement.parentElement.id === 'myModalquery') {
                                    arr[i].style.width = '1200px';
                                    break;
                                }
                            }
                            $.get(host).done(function (response, textStatus, xhr) {
                                otvetjson = response;
                            });
                            $(mywindmodal).on('shown.bs.modal', function (e) {
                                $('#logview_query').html(otvetjson);
                            });
                            regim = "";
                        }
                        else {
                            alert('Не найдена связка для ' + query);
                        }
                    }
                },
                error: function (xhr, status, error) {
                    alert('Возникла ошибка: Ошибка получения данных -' + xhr.responseText);
                }
            }
        );
        $(mywindmodal).on('hide.bs.modal', function (e) {
            $('#logview_query').html('<div></div>');
            // mywindmodal.
        });
    }
}

function bids_del(id, regim) {
    let data = {};
    let currentelement = document.getElementById(id);
    data.csrfmiddlewaretoken = getCookie('csrftoken');
    let mywindmodal = document.getElementById('bids_del');
    $(mywindmodal).modal('show');
    document.querySelector('#delbidsyes').onclick = function () {
        // $(mywindmodal).modal.close();

        data.id = id;
        data.delite = 1;
        data.regim = regim;
        switch (regim) {
            case 'add':
                $.ajax(
                    {
                        url: 'bids/',
                        type: 'POST',
                        data: data,
                        success: function (data, textStatus, XHR) {
                            // console.log("запрос DELETE отработал")
                            location.reload();
                        },
                        error: function (xhr, status, error) {
                            alert('Возникла ошибка: Ошибка получения данных -' + xhr.responseText);
                        }
                    }
                );
                break;
            case 'double':
                $.ajax(
                    {
                        url: 'bidsdouble/',
                        type: 'POST',
                        data: data,
                        success: function (data, textStatus, XHR) {
                            // console.log("запрос DELETE отработал")
                            location.reload();
                        },
                        error: function (xhr, status, error) {
                            alert('Возникла ошибка: Ошибка получения данных -' + xhr.responseText);
                        }
                    }
                );
        }


        // alert("Нажата кнопка ДА")
    };
    // document.querySelector('#delno').onclick = function() {
    //
    // };

}

function showalertdel(id) {
    let data = {};
    let currentelement = document.getElementById(id);
    data.csrfmiddlewaretoken = getCookie('csrftoken');
    let mywindmodal = document.getElementById('deldelayalert');
    $(mywindmodal).modal('show');
    document.querySelector('#delyes').onclick = function () {
        // $(mywindmodal).modal.close();
        data.id = id;
        data.delite = 1;
        $.ajax(
            {
                url: 'delay/',
                type: 'POST',
                data: data,
                success: function (data, textStatus, XHR) {
                    // console.log("запрос DELETE отработал")
                    location.reload();
                },
                error: function (xhr, status, error) {
                    alert('Возникла ошибка: Ошибка получения данных -' + xhr.responseText);
                }
            }
        );

        // alert("Нажата кнопка ДА")
    };
    // document.querySelector('#delno').onclick = function() {
    //
    // };

}

function showbidsedit(id, regim) {
    let data = {};
    let currentelement = document.getElementById(id);
    data.csrfmiddlewaretoken = getCookie('csrftoken');
    data.edit_id = currentelement.dataset.edit_id;
    data.regim = regim;
    switch (regim) {
        case 'add':
            host = location.origin + "/bids/bidsedit/" + data.edit_id + "/";
            $.get(host).done(function (response, textStatus, xhr) {
                                otvetjson = response;
                            });
            // $.ajax(
            //     {
            //         // host = location.origin + "/mon/mon_query/" + data.queryname + "/";
            //         url: '/bids/bidsedit/'+ data.edit_id + "/",
            //         type: 'GET',
            //         data: data,
            //         success: function (data, textStatus, XHR) {
            //             console.log("запрос DELETE отработал")
            //             // location.reload();
            //         },
            //         error: function (xhr, status, error) {
            //             alert('Возникла ошибка: Ошибка получения данных -' + xhr.responseText);
            //         }
            //     }
            // );
            break;
        case 'double':
            $.ajax(
                {
                    url: '/bids/doubleedit/',
                    type: 'POST',
                    data: data,
                    success: function (data, textStatus, XHR) {
                        console.log("запрос DELETE отработал")
                        // location.reload();
                    },
                    error: function (xhr, status, error) {
                        alert('Возникла ошибка: Ошибка получения данных -' + xhr.responseText);
                    }
                }
            );
            break;

    }
}

function showalertedit(id) {
    var err_upd = 0;
    var txt_err = '';
    var formValid = true;
    var poleValid = true;
    let data = {};
    let currentelement = document.getElementById(id);
    data.csrfmiddlewaretoken = getCookie('csrftoken');
    let mywindmodaledit = document.getElementById('editdelayalert');
    $(mywindmodaledit).on('shown.bs.modal', function (e) {
        $('#id_source').val(currentelement.dataset.source);
        $('#id_destination').val(currentelement.dataset.destination);
        $('#id_email').val(currentelement.dataset.email);
        $('#err_response').html('<p></p>');
    });
    $(mywindmodaledit).modal('show');

    $('#id_source').on('change', function () {
        data.id = id;
        data.source = $('#id_source')[0].value;
        data.destination = $('#id_destination')[0].value;
        data.pole = '1';
        $.ajax(
            {
                url: '/incident/editalert/',
                type: 'POST',
                data: data,
                beforeSend: function () {
                    $('#err_source').html('<p></p>');
                },
                success: function (data, textStatus, XHR) {
                    if (data.success) {
                        $(this).addClass('not_error');
                        formValid = true;
                    }
                    else {
                        $(this).removeClass('not_error').addClass('error');
                        $('#err_source').html('<p>' + data.err_mes + '</p>');
                        formValid = false;
                    }
                    // console.log("запрос EDIT отработал")
                },
                error: function (xhr, status, error) {
                    alert('Возникла ошибка: Ошибка получения данных -' + xhr.responseText);
                }
            }
        );

    });
    $('#id_destination').on('change', function () {
        data.id = id;
        data.destination = $('#id_destination')[0].value;
        data.source = $('#id_source')[0].value;
        data.pole = '2';
        $.ajax(
            {
                url: '/incident/editalert/',
                type: 'POST',
                data: data,
                beforeSend: function () {
                    $('#err_destination').html('<p></p>');
                },
                success: function (data, textStatus, XHR) {
                    if (data.success) {
                        $(this).addClass('not_error');
                        formValid = true;
                    }
                    else {
                        $(this).removeClass('not_error').addClass('error');
                        $('#err_destination').html('<p>' + data.err_mes + '</p>');
                        formValid = false;
                    }
                    // console.log("запрос EDIT отработал")
                },
                error: function (xhr, status, error) {
                    alert('Возникла ошибка: Ошибка получения данных -' + xhr.responseText);
                }
            }
        );

    });

    $('#id_email').on('change', function () {
        var list_email = [];
        var rv_email = /^([a-zA-Z0-9_.-])+@([a-zA-Z0-9_.-])+\.([a-zA-Z])+([a-zA-Z])+/;
        var check_email = $('#id_email')[0].value;
        if (check_email !== '') {
            if (check_email.indexOf(',') + 1) {
                list_email = check_email.split(',');
                for (i = 0; i < list_email.length; i++) {
                    if (rv_email.test(list_email[i].trimLeft())) {
                        poleValid = true;
                    }
                    else {
                        poleValid = false;
                        break;
                    }
                }
            }
            else {
                if (rv_email.test(check_email)) {
                    poleValid = true;
                }
                else {
                    poleValid = false;
                }
            }
            if (poleValid) {
                $('#err_email').html('<p></p>');
                $(this).addClass('not_error');
                formValid = true;
            }
            else {
                formValid = false;
                $(this).removeClass('not_error').addClass('error');
                $('#err_email').html('<p>Поле должно содержать правильный email-адрес</p>');
            }
        }
        else {
            formValid = false;
            $(this).removeClass('not_error').addClass('error');
            $('#err_email').html('<p>Поле должно содержать правильный email-адрес</p>');

        }
    });


    // document.querySelector('#edityes').onclick = function () {
    $('#edityes').on('click', function () {

        //если форма валидна, то
        if (formValid) {
            data.id = id;
            data.source = $('#id_source')[0].value;
            data.destination = $('#id_destination')[0].value;
            data.email = $('#id_email')[0].value;
            data.pole = 'all';

            $.ajax(
                {
                    url: '/incident/editalert/',
                    type: 'POST',
                    data: data,
                    success: function (data, textStatus, XHR) {
                        if (data.success) {
                            location.reload();
                        }
                    },
                    error: function (xhr, status, error) {
                        alert('Возникла ошибка: Ошибка получения данных -' + xhr.responseText);
                    }
                }
            );

            //сркыть модальное окно
            $(mywindmodaledit).modal('hide');
            //отобразить сообщение об успехе

        }
        else {
            return false;
        }

    });

    $(mywindmodaledit).on('hide.bs.modal', function (e) {
        // $('#err_response').html('<p></p>');
        // if (err_upd ===1){
        //     alert(txt_err)
        // }
    });

}

function showqueryalertdel(id) {
    let data = {};
    let currentelement = document.getElementById(id);
    data.csrfmiddlewaretoken = getCookie('csrftoken');
    let mywindmodal = document.getElementById('delqueryalert');

    $(mywindmodal).modal('show');

    document.querySelector('#delyes').onclick = function () {
        // $(mywindmodal).modal.close();
        data.id = id;
        data.delite = 1;
        $.ajax(
            {
                url: 'query/',
                type: 'POST',
                data: data,
                success: function (data, textStatus, XHR) {
                    // console.log("запрос DELETE отработал")
                    location.reload();
                },
                error: function (xhr, status, error) {
                    alert('Возникла ошибка: Ошибка получения данных -' + xhr.responseText);
                }
            }
        );

        // alert("Нажата кнопка ДА")
    };
    // document.querySelector('#delno').onclick = function() {
    //
    // };

}

function showqueryalert(id) {
    let data = {};
    let currentelement = document.getElementById(id);
    data.csrfmiddlewaretoken = getCookie('csrftoken');
    data.server_name = currentelement.value;
    data.regim = 'repserver';
    $.ajax(
        {
            url: 'showqueryalert/',
            type: 'POST',
            data: data,
            success: function (data) {
                let options = '';
                $('#id_name_query_alert').find('option:not(:first)').remove();
                // $('#name_query').append('<option value="0">Выберите очередь</option>');
                $.each(data.query_alert, function () {
                    $('#id_name_query_alert').append('<option value="' + this[0] + '">' + this[0] + '</option>');
                });
                $('#id_name_query_alert')[0].selected = true;
                $('#id_name_query_alert').enable();
                // $('#graph').remove();
            },
            error: function (xhr, status, error) {
                alert('Возникла ошибка: Ошибка получения данных -' + xhr.responseText);
            }
        }
    );
}

function showqueryalertedit(id) {
    var formValid = true;
    var poleValid = true;
    let data = {};
    let currentelement = document.getElementById(id);
    data.csrfmiddlewaretoken = getCookie('csrftoken');
    let mywindmodal = document.getElementById('editqueryalert');

    $(mywindmodal).on('shown.bs.modal', function (e) {
        $('#id_query_alert').val(parseFloat(currentelement.dataset.query_alert));
        $('#id_email').val(currentelement.dataset.email);

        data.server_name = currentelement.dataset.server_name;
        data.name_query_alert = currentelement.dataset.name_query_alert;
        data.regim = "repserver";
        $.ajax(
            {
                url: '/incident/editquery/',
                type: 'POST',
                data: data,
                success: function (data) {
                    let options = '';
                    let sindex = 0;
                    $('#id_server_name').find('option:not(:first)').remove();
                    $.each(data.poolrs, function () {
                        if (this[0]=== data.server_name)
                        {
                            sindex = $('#id_server_name')[0].options.length
                        }

                        $('#id_server_name').append('<option value="' + this[0] + '">' + this[0] + '</option>');
                    });
                    $('#id_server_name')[0].options.selectedIndex = sindex;
                    sindex = 0;
                    $('#id_name_query_alert').find('option:not(:first)').remove();
                    $.each(data.poolquery, function () {
                        if (this[0]=== data.name_query_alert)
                        {
                            sindex = $('#id_name_query_alert')[0].options.length
                        }
                        $('#id_name_query_alert').append('<option value="' + this[0] + '">' + this[0] + '</option>');
                    });
                    $('#id_name_query_alert')[0].options.selectedIndex = sindex;
                    },

                error: function (xhr, status, error) {
                    alert('Возникла ошибка: Ошибка получения данных -' + xhr.responseText);
                }
            }
        );
    });

    $(mywindmodal).modal('show');

    $('#id_server_name').on('change', function () {
        data.server_name = $('#id_server_name')[0].value;
        data.csrfmiddlewaretoken = getCookie('csrftoken');
        data.regim = "querychange";
        $.ajax(
            {
                url: '/incident/editquery/',
                type: 'POST',
                data: data,
                success: function (data) {
                    $('#id_name_query_alert').find('option:not(:first)').remove();
                    $('#id_name_query_alert').append('<option value="0">Выберите очередь</option>');
                    $('#id_name_query_alert')[0].selected = true;

                    $.each(data.poolquery, function () {
                        $('#id_name_query_alert').append('<option value="' + this[0] + '">' + this[0] + '</option>');
                    });

                },
                error: function (xhr, status, error) {
                    alert('Возникла ошибка: Ошибка получения данных -' + xhr.responseText);
                }

            }
        );
    });

    $('#id_query_alert').on('change', function () {
        var check_queryalert = $('#id_query_alert')[0].value;
        if (check_queryalert < 0) {
            formValid = false;
            $(this).removeClass('not_error').addClass('error');
            $('#err_query_alert').html('<p>Поле должно содержать число больше или равное 0</p>');
        }
        else {
            $('#err_query_alert').html('<p></p>');
            $(this).addClass('not_error');
            formValid = true;
        }
    });

    $('#id_email').on('change', function () {
        var list_email = [];
        var rv_email = /^([a-zA-Z0-9_.-])+@([a-zA-Z0-9_.-])+\.([a-zA-Z])+([a-zA-Z])+/;
        var check_email = $('#id_email')[0].value;
        if (check_email !== '') {
            if (check_email.indexOf(',') + 1) {
                list_email = check_email.split(',');
                for (i = 0; i < list_email.length; i++) {
                    if (rv_email.test(list_email[i].trimLeft())) {
                        poleValid = true;
                    }
                    else {
                        poleValid = false;
                        break;
                    }
                }
            }
            else {
                if (rv_email.test(check_email)) {
                    poleValid = true;
                }
                else {
                    poleValid = false;
                }
            }
            if (poleValid) {
                $('#err_email').html('<p></p>');
                $(this).addClass('not_error');
                formValid = true;
            }
            else {
                formValid = false;
                $(this).removeClass('not_error').addClass('error');
                $('#err_email').html('<p>Поле должно содержать правильный email-адрес</p>');
            }
        }
        else {
            formValid = false;
            $(this).removeClass('not_error').addClass('error');
            $('#err_email').html('<p>Поле должно содержать правильный email-адрес</p>');

        }
    });


    $('#edityes').on('click', function () {
        //если форма валидна, то
        if (formValid) {
            data.id = id;
            data.server_name = $('#id_server_name')[0].value;
            data.name_query_alert = $('#id_name_query_alert')[0].value;
            data.query_alert = $('#id_query_alert')[0].value;
            data.email = $('#id_email')[0].value;
            data.pole = 'all';
            data.regim = 'edityes';

            $.ajax(
                {
                    url: '/incident/editquery/',
                    type: 'POST',
                    data: data,
                    success: function (data, textStatus, XHR) {
                        if (data.success) {
                            location.reload();
                        }
                    },
                    error: function (xhr, status, error) {
                        alert('Возникла ошибка: Ошибка получения данных -' + xhr.responseText);
                    }
                }
            );

            //сркыть модальное окно
            $(mywindmodal).modal('hide');
            //отобразить сообщение об успехе

        }
        else {
            return false;
        }

    });

    $(mywindmodal).on('hide.bs.modal', function (e) {
        // $('#show_edit').remove();
    });

}

$(function () {
    // $('#datetimepicker1').datetimepicker();
    // $('#datetimepicker2').datetimepicker();
    my_startdt = "";
    my_enddt = "";
    $('#datetimepicker1').datetimepicker(
        {
            locale: 'ru'
        });
    $('#datetimepicker2').datetimepicker({
        locale: 'ru',
        useCurrent: false

    });
    $('#datetimepicker1').on('dp.change', function (e) {
        $('#datetimepicker2').data("DateTimePicker").minDate(e.date);
        let button_graph = document.getElementById('show_graph_detail');
        button_graph.disabled = true;

        my_startdt = $('#datetimepicker1').data("DateTimePicker").date().format();
    });
    $('#datetimepicker2').on('dp.change', function (e) {
        $('#datetimepicker1').data("DateTimePicker").maxDate(e.date);
        let button_graph = document.getElementById('show_graph_detail');
        button_graph.disabled = true;
        my_enddt = $('#datetimepicker2').data("DateTimePicker").date().format();
        // var now = moment();
    });

/** **/
    $('#birthday').datetimepicker(
        {
            locale: 'ru',
            format: 'L'
        }
    );
    $('#date_of_issue').datetimepicker(
        {
            locale: 'ru',
            format: 'L'
        }
    );


});

function detaildelay() {
    let data_d = {};
    data_d.csrfmiddlewaretoken = getCookie('csrftoken');
    data_d.source = document.getElementById('id_source').value;
    data_d.destination = document.getElementById('id_destination').value;
    data_d.starttime = my_startdt;
    data_d.endtime = my_enddt;
    data_d.listshow = 1;
    data_d.listdest = 0;
    // || data.startdate==="" || data.enddate===""
    if (data_d.source === "" || data_d.destination === "" || data_d.starttime === "" || data_d.endtime === "") {
        alert("Не все поля заполнены !!!");
        return false;
    }


    var table = document.getElementById("detail").tBodies[0];
    // var dateFormat = require('dateformat');
    // var now = moment();
    $.ajax(
        {
            url: '/delay/detail/',
            type: 'POST',
            data: data_d,
            beforeSend: function () {
                // row = table.insertRow(0);
                $('#delaydetail').html('<img align="center" id="imgcode" src="' + static_url + 'ajax-loader.gif" >');

            },
            success: function (data_d, textStatus, XHR) {
                {/*<div align="center"><p>Данные получены</p></div>*/
                }
                $('#delaydetail').html('');
                var ind = 0;
                let button_graph = document.getElementById('show_graph_detail');
                if (data_d.ldelay.length === 0) {
                    button_graph.disabled = true;
                }
                else {
                    $.each(data_d.ldelay, function () {
                        row = table.insertRow(ind);
                        if (this["difference"] !== "00:00:00") {
                            row.style.backgroundColor = "#f0f0f0";
                        }
                        cell1 = row.insertCell(0);
                        cell2 = row.insertCell(1);
                        cell3 = row.insertCell(2);
                        cell4 = row.insertCell(3);
                        cell5 = row.insertCell(4);
                        cell6 = row.insertCell(5);
                        d_tek = new Date(this["timeobr"]);
                        cell1.innerHTML = d_tek.toLocaleDateString() + " " + d_tek.toLocaleTimeString();
                        // cell1.innerHTML = dateFormat(this["timeobr"], "yyyy-mm-dd HH:MM:ss");
                        cell2.innerHTML = this["recdelay"];
                        cell2.style.textAlign = "center";
                        cell3.innerHTML = this["realrepdelay"];
                        cell3.style.color = "red";
                        cell3.style.textAlign = "center";
                        cell4.innerHTML = this["difference"];
                        cell4.style.textAlign = "center";
                        cell5.innerHTML = this["starttime"];
                        cell5.style.textAlign = "center";
                        cell6.innerHTML = this["committime"];
                        cell6.style.textAlign = "center";
                        ind++;
                    });

                    button_graph.disabled = false;
                }
            },
            error: function (xhr, status, error) {
                alert('Возникла ошибка: Ошибка получения данных -' + xhr.responseText);
            }
        }
    )
}

function destinationchange() {
    var button_graph = document.getElementById('show_graph_detail');
    button_graph.disabled = true;
}

function sourcechange() {
    let data = {};
    data.csrfmiddlewaretoken = getCookie('csrftoken');
    data.source = document.getElementById('id_source').value;
    data.listdest = 1;
    data.listshow = 0;
    data.showgraph = 0;
    let button_graph = document.getElementById('show_graph_detail');
    button_graph.disabled = true;
    var pole_dest = document.getElementById('id_destination');
    var pole = document.getElementById('destination_list');

    function remove() {
        // let value = pole.childElementCount;
        // var childArray = pole.childNodes;
        var childArray = pole.children;
        let value = childArray.length;
        for (i = 0; i < value; i++) {
            pole.removeChild(childArray[0]);
        }
    }

    if (data.source === "") {
        pole_dest.disabled = true;
        data.listdest = 0;
    }
    else {
        pole_dest.disabled = false;
        pole_dest.value = '';


        // var pole = document.getElementById('destination_list');
        // addOption(pole, "", "Не выбрано", true);

        $.ajax(
            {
                url: '/delay/detail/',
                type: 'POST',
                data: data,
                success: function (data, textStatus, XHR) {

                    remove();
                    var i = 1;
                    // pole.options.length = 0;
                    $.each(data.destination, function () {
                        addOption(pole, "", this["destination"], false);
                    });

                    kk = 0;
                }
            }
        )

    }
}

function addOption(oListbox, text, value, isDefaultSelected, isSelected) {
    var oOption = document.createElement("option");
    oOption.appendChild(document.createTextNode(text));
    oOption.setAttribute("value", value);

    if (isDefaultSelected) oOption.defaultSelected = true;
    else if (isSelected) oOption.selected = true;

    oListbox.appendChild(oOption);
}


function show_detail_graph() {
    let data = {};
    data.csrfmiddlewaretoken = getCookie('csrftoken');
    data.source = document.getElementById('id_source').value;
    data.destination = document.getElementById('id_destination').value;
    data.starttime = my_startdt;
    data.endtime = my_enddt;
    data.showgraph = 1;
    data.listshow = 1;
    let namegraph = data.source + '->' + data.destination;
    let mywindmodal = document.getElementById('myModalgraph');


    $(mywindmodal).modal('show');
    // $(mywindmodal).on('shown.bs.modal', function (e) {
    //     $('#logview_graph').html('<div align="center"><p>Получение данных для графика <span>' + namegraph + '</span> </p><img id="imgcode" src="' + static_url + 'ajax-loader.gif" ></div>');
    // });
    $.ajax(
        {
            url: '/delay/detail/',
            type: 'POST',
            data: data,
            beforeSend: function () {
                $('#logview_graph').html('<div align="center"><p>Получение данных для графика <span>' + namegraph + '</span> </p><img id="imgcode" src="' + static_url + 'ajax-loader.gif" ></div>');
            },
        }
    ).success(function (data, textStatus, XHR) {
        if (namegraph === XHR.responseJSON.nameobj) {
            let data_detail = data;
            $('#logview_graph').html('<div align="center"><p>Данные получены</p></div>');
            $("#logview_graph").remove();
            drawhtml_graph();
            testgraph(data_detail, namegraph, 'detail');
            namegraph = "";
        }
    })
        .error(function (xhr, status, error) {
            alert('Возникла ошибка: Ошибка получения данных -' + xhr.responseText);
            $("#logview_graph").remove();
        });

    $(mywindmodal).on('hide.bs.modal', function (e) {
        $("#container").remove();

    });

}

function showviewtrannext(id) {
    let regim = 'viewtrannext';
    let data = {};
    let currentelement = document.getElementById(id);
    data.viewtrannext = 1;
    data.csrfmiddlewaretoken = getCookie('csrftoken');
    data.server_name = document.getElementById(id).attributes.servername.value;
    data.numquery = document.getElementById(id).attributes.numquery.value;
    data.lqid_end = document.getElementById(id).attributes.lqid_end.value;
    data.info = document.getElementById(id).attributes.info.value;
    document.getElementById(id).disabled = true;
    $('#myModalViewTran').modal('show');
    $.ajax(
        {
            url: 'viewtrannext',
            type: 'POST',
            data: data,
            beforeSend: function () {
                $("#logview_tran").html('<div align="center"><p>Тут будет показана транзакция с очереди </p><p>' + data.server_name + '</p><p>' + data.info + '</p><p><img id="imgcode" src="' + static_url + 'ajax-loader.gif" ></p></div>');
            },
            success: function (data, textStatus, XHR) {
                if (regim === XHR.responseJSON.nameobj) {
                    if (data.success) {
                        // let changestring = textpars(data.otvet_raw);
                        // $("#logview_tran").html('<p>Source: <span style="font-weight: bold">' + data.source + '</span> Origin Commit Time: <span style="font-weight: bold">' + data.cur_sourcetime + '</span> </p><p>' + textpars(data.otvet_raw) + '</p>');
                        let arr = $('.modal-content');
                        for (let i = 0; i < arr.length; ++i) {
                            if (arr[i].parentElement.parentElement.id === 'myModalViewTran') {
                                arr[i].style.width = '1300px';
                                break;
                            }
                        }
                        $("#logview_tran").html('' +
                            '<div class="col-md-12" id="viewtran">' +
                            '<table class="table table-bordered" id="vtran">' +
                            '<thead>' +
                            '<tr role="row">' +
                            '<th><h4 align="center">Orgn Siteid</h4></th>' +
                            '<th><h4 align="center">Orgn Time</h4></th>' +
                            '<th><h4 align="center">Orgn User</h4></th>' +
                            '<th><h4 align="center">Tran Name</h4></th>' +
                            '<th><h4 align="center">Command</h4></th>' +
                            '</tr>' +
                            '</thead>' +
                            '<tbody id="trandetail">' +
                            '</tbody>' +
                            ' </table>' +
                            '</div>');
                        $('#trandetail').html('');
                        var table = document.getElementById("vtran").tBodies[0];
                        var ind = 0;
                        $.each(data.otvet, function () {
                            row = table.insertRow(ind);
                            if (this[0] !== "Orgn Siteid") {
                                cell1 = row.insertCell(0);
                                cell2 = row.insertCell(1);
                                cell3 = row.insertCell(2);
                                cell4 = row.insertCell(3);
                                cell5 = row.insertCell(4);
                                // cell1.innerHTML = data.source;
                                cell1.innerHTML = this[0];
                                if (this[1] !== "Jan  1 1900 12:00AM") {
                                    cell2.innerHTML = this[1];
                                    cell2.style.width = '160px';
                                }
                                cell2.style.textAlign = "center";
                                if ("None" !== this[2]) {
                                    cell3.innerHTML = this[2];
                                    cell3.style.width = '100px';
                                }
                                if ("None" !== this[3]) {
                                    cell4.innerHTML = this[3];
                                    cell4.style.width = '100px';
                                }
                                cell5.innerHTML = textpars(this[4]);
                            }
                            ind++;
                        });
                        document.getElementById("nexttran").setAttribute('LQID_END', data.lqid_end);
                        document.getElementById("nexttran").disabled = false;
                        // scroll_to_bottom_viewtran(1);
                    }
                    else {
                        if (data.busywait > 0) {
                            $("#logview_tran").html('<p align="center"> Сервер <span style="font-weight: bold">' + data.servname + '</span> занят,<br> повторите попытку позже (busy ' + data.busywait + ' cекунд)</p>');
                        }
                        else {
                            $("#logview_tran").html('<p align="center"> Не удалось получить ответ от репсервера <span style="font-weight: bold">' + data.servname + '</span></p>');
                        }

                    }
                    regim = "";

                }
            },
            error: function (xhr, status, error) {
                alert('Возникла ошибка: Ошибка получения данных -' + xhr.responseText);
            }
        }
    );


    $('#myModalViewTran').on('hide.bs.modal', function (e) {

        $("#logview_tran").html('<p></p>');
        // $('#myModalViewTran').style.width = '700px';
    });

}

function showviewlogsegment(id) {
    // var klick = id;
    var currentelement = document.getElementById(id);
    // if (+new Date() - Number(currentelement.dataset.klick) > 60000) {
    let regim = 'viewlogsegment';
    let data = {};

    // data.server_name = currentelement.dataset.servname;
    data.source = currentelement.dataset.source;
    data.regim = regim;
    // data.numberquery = currentelement.dataset.numberquery;
    // data.repagent = currentelement.dataset.repagent;
    data.csrfmiddlewaretoken = getCookie('csrftoken');
    $('#ModalViewLogSegment').modal('show');
    $.ajax(
        {
            url: 'viewlogsegment',
            type: 'POST',
            data: data,
            beforeSend: function () {
                $("#view_logsegment").html('<div align="center"><p>Тут будет показаны  данные по логсегменту </p><p>' + data.info + '</p><p><img id="imgcode" src="' + static_url + 'ajax-loader.gif" ></p></div>');
            },
            success: function (data, textStatus, XHR) {
                if (regim === XHR.responseJSON.nameobj) {
                    if (data.success) {
                        $("#view_logsegment").html('' +
                            '<div class="col-md-12" id="viewlogsegment">' +
                            '<h5 align="center">' + data.dsname + " " + data.viewcache + '</h5>' +
                            '<table class="table table-bordered" id="vlog">' +
                            '<thead>' +
                            '<tr role="row">' +
                            '<th><h4 align="center">total_size</h4></th>' +
                            '<th><h4 align="center">total_pages</h4></th>' +
                            '<th><h4 align="center">free_pages</h4></th>' +
                            '<th><h4 align="center">used_pages</h4></th>' +
                            '<th><h4 align="center">reserved_pages</h4></th>' +
                            '</tr>' +
                            '</thead>' +
                            '<tbody id="logsegmentdetail">' +
                            '<tr role="row">' +
                            '<th><h5 align="center">' + data.otvet[0] + '</h5></th>' +
                            '<th><h5 align="center">' + data.otvet[1] + '</h5></th>' +
                            '<th><h5 align="center">' + data.otvet[2] + '</h5></th>' +
                            '<th><h5 align="center">' + data.otvet[3] + '</h5></th>' +
                            '<th><h5 align="center">' + data.otvet[4] + '</h5></th>' +
                            '</tr>' +
                            '</tbody>' +
                            ' </table>' +
                            '</div>');

                    }
                    else {
                        $("#view_logsegment").html('<p>Ошибка получения данных</p>');
                    }
                    regim = "";
                }
            },
            error: function (xhr, status, error) {
                alert('Возникла ошибка: Ошибка получения данных -' + xhr.responseText);
            }
        }
    );

    $('#ModalViewLogSegment').on('hide.bs.modal', function (e) {

        $("#logsegment").html('<p></p>');
        // $('#myModalViewTran').style.width = '700px';
    });
    //     currentelement.dataset.klick = +new Date();
    // }
    // else{
    //     alert('Не кликай так часто');
    //     currentelement.dataset.klick = +new Date();
    // }

}

function showviewpubsub(id) {
    // let klick = +new Date();

    let regim = 'viewpubsub';
    let data = {};
    let currentelement = document.getElementById(id);
    data.server_name = currentelement.dataset.servname;
    data.info = currentelement.dataset.info;
    data.numberquery = currentelement.dataset.numberquery;
    data.repagent = currentelement.dataset.repagent;
    data.regimwork = regim;
    data.csrfmiddlewaretoken = getCookie('csrftoken');

    $('#ModalViewPubSub').modal('show');
    $.ajax(
        {
            url: 'viewpubsub',
            type: 'POST',
            data: data,
            beforeSend: function () {
                $("#view_pubsub").html('<div align="center"><p>Тут будет показаны  подписки или публикации </p><p>' + data.server_name + '</p><p>' + data.info + '</p><p><img id="imgcode" src="' + static_url + 'ajax-loader.gif" ></p></div>');
            },
            success: function (data, textStatus, XHR) {
                if (regim === XHR.responseJSON.nameobj) {
                    if (data.success) {
                        $("#view_pubsub").html('' +
                            '<div class="col-md-12" id="pubsub_view">' +
                            '<table class="table" id="vpubsub">' +
                            '<tbody id="pubsubdetail"></tbody>' +
                            ' </table>' +
                            '</div>');
                        // $('#pubsubdetail').html('');
                        // var table = document.getElementById("vpubsub").tBodies[0];
                        // var ind = 0;
                        // row = table.insertRow(ind);
                        // cell1 = row.insertCell(0);
                        // cell2 = row.insertCell(1);
                        // cell1.style.width = '10px';
                        // // cell1.innerHTML = " ";
                        // cell2.innerHTML = data.otvet;
                        $('#pubsubdetail').append(data.otvet);
                        scroll_to_bottom_pubsub(1);
                    }
                    else {
                        $("#view_pubsub").html('<p>Ошибка получения данных</p>');
                    }
                    regim = "";
                }
            },
            error: function (xhr, status, error) {
                alert('Возникла ошибка: Ошибка получения данных -' + xhr.responseText);
            }
        }
    );

    $('#ModalViewPubSub').on('hide.bs.modal', function (e) {

        $("#view_pubsub").html('<p></p>');
        // $('#myModalViewTran').style.width = '700px';
    });
}
function showviewtran(id) {
    let regim = 'viewtran';
    let data = {};
    let currentelement = document.getElementById(id);
    data.server_name = currentelement.dataset.servname;
    data.info = currentelement.dataset.info;
    data.numquery = data.info.substr(0, data.info.indexOf(" "));
    data.viewtran = 1;
    data.csrfmiddlewaretoken = getCookie('csrftoken');

    document.getElementById("nexttran").setAttribute('servername', data.server_name);
    document.getElementById("nexttran").setAttribute('numquery', data.numquery);
    document.getElementById("nexttran").setAttribute('info', data.info);

    document.getElementById("nexttran").disabled = true;
    // $('#myModalViewTran').on('shown.bs.modal', function (e) {
    //
    //     $("#logview_tran").html('<div align="center"><p>Тут будет показана транзакция с очереди </p><p>' + data.server_name + '</p><p>' + data.info + '</p><p>' + data.numquery + '</p><p><img id="imgcode" src="' + static_url + 'ajax-loader.gif" ></p></div>');
    // });
    $('#myModalViewTran').modal('show');
    $.ajax(
        {
            url: 'viewtran',
            type: 'POST',
            data: data,
            beforeSend: function () {
                $("#logview_tran").html('<div align="center"><p>Тут будет показана транзакция с очереди </p><p>' + data.server_name + '</p><p>' + data.info + '</p><p><img id="imgcode" src="' + static_url + 'ajax-loader.gif" ></p></div>');
            },
            success: function (data, textStatus, XHR) {
                if (regim === XHR.responseJSON.nameobj) {
                    if (data.success) {
                        // let changestring = textpars(data.otvet_raw);
                        // $("#logview_tran").html('<p>Source: <span style="font-weight: bold">' + data.source + '</span> Origin Commit Time: <span style="font-weight: bold">' + data.cur_sourcetime + '</span> </p><p>' + textpars(data.otvet_raw) + '</p>');
                        let arr = $('.modal-content');
                        for (let i = 0; i < arr.length; ++i) {
                            if (arr[i].parentElement.parentElement.id === 'myModalViewTran') {
                                arr[i].style.width = '1300px';
                                break;
                            }
                        }
                        $("#logview_tran").html('' +
                            '<div class="col-md-12" id="viewtran">' +
                            '<table class="table table-bordered" id="vtran">' +
                            '<thead>' +
                            '<tr role="row">' +
                            '<th><h4 align="center">Orgn Siteid</h4></th>' +
                            '<th><h4 align="center">Orgn Time</h4></th>' +
                            '<th><h4 align="center">Orgn User</h4></th>' +
                            '<th><h4 align="center">Tran Name</h4></th>' +
                            '<th><h4 align="center">Command</h4></th>' +
                            '</tr>' +
                            '</thead>' +
                            '<tbody id="trandetail">' +
                            '</tbody>' +
                            ' </table>' +
                            '</div>');
                        $('#trandetail').html('');
                        var table = document.getElementById("vtran").tBodies[0];
                        var ind = 0;
                        $.each(data.otvet, function () {
                            row = table.insertRow(ind);
                            if (this[0] !== "Orgn Siteid") {
                                cell1 = row.insertCell(0);
                                cell2 = row.insertCell(1);
                                cell3 = row.insertCell(2);
                                cell4 = row.insertCell(3);
                                cell5 = row.insertCell(4);
                                // cell1.innerHTML = data.source;
                                cell1.innerHTML = this[0];
                                if (this[1] !== "Jan  1 1900 12:00AM") {
                                    cell2.innerHTML = this[1];
                                    cell2.style.width = '160px';
                                }
                                cell2.style.textAlign = "center";
                                if ("None" !== this[2]) {
                                    cell3.innerHTML = this[2];
                                    cell3.style.width = '100px';
                                }
                                if ("None" !== this[3]) {
                                    cell4.innerHTML = this[3];
                                    cell4.style.width = '100px';
                                }
                                cell5.innerHTML = textpars(this[4]);
                            }
                            ind++;
                        });
                        document.getElementById("nexttran").setAttribute('LQID_END', data.lqid_end);
                        document.getElementById("nexttran").disabled = false;
                        // scroll_to_bottom_viewtran(1);
                    }
                    else {
                        if (data.busywait > 0) {
                            $("#logview_tran").html('<p align="center"> Сервер <span style="font-weight: bold">' + data.servname + '</span> занят,<br> повторите попытку позже (busy ' + data.busywait + ' cекунд)</p>');
                        }
                        else {
                            $("#logview_tran").html('<p align="center"> Не удалось получить ответ от репсервера <span style="font-weight: bold">' + data.servname + '</span></p>');
                        }

                    }
                    regim = "";

                }
            },
            error: function (xhr, status, error) {
                alert('Возникла ошибка: Ошибка получения данных -' + xhr.responseText);
            }
        }
    );


    $('#myModalViewTran').on('hide.bs.modal', function (e) {

        $("#logview_tran").html('<p></p>');
        // $('#myModalViewTran').style.width = '700px';
    });

}

function resumeclick(id) {
    // e = e || window.event;
    // e.preventDefault();

    // let data = {};
    let data = {};
    data.csrfmiddlewaretoken = getCookie('csrftoken');
    let submit_btn = document.getElementById(id);

    data.server_name = submit_btn.dataset.server_name;
    data.name = submit_btn.dataset.name;
    data.info = submit_btn.dataset.info;
    data.rs_locale = submit_btn.dataset.locale;
    data.regim = submit_btn.dataset.regim;
    // data.username = submit_btn.dataset.user;
    let regimr = data.regim;
    $("#otvet").remove();

    $.ajax({
        url: 'dsi/',
        type: 'POST',
        data: data,
        success: function (data, textStatus, XHR) {
            if (regimr === XHR.responseJSON.nameobj) {
                // $(".modal-body").html('<h4 id = "otvet">' + data.otvet + '</h4>');
                $("#logview").html('<h4 id = "otvet">' + data.otvet + '</h4>');
                // $(".modal-body").append('<p>'+ data.otvet + '</p>');
                regimr = '';
            }
        },
        error: function (xhr, status, error) {
            alert('Возникла ошибка: ' + +xhr.responseText);
        }
    });
    $('#myModal').on('hide.bs.modal', function (e) {
        $("#ol_mini").remove();
        $("#otvet").remove();
    });
}


function textpars(stroka) {
    let otvet = "Пусто!!!!";
    let result;
    let str_rec = '(\\W|^)(insert|update|delete|begin\\stransaction|commit\\stransaction|--\\slimited)(\\W|$)';
    let re = new RegExp(str_rec, 'g');
    let prelement = '';
    if (stroka.search(re) !== -1) {
        result = stroka.match(re);

        for (i = 0; i < result.length; i++) {
            // let pn = 0;
            // 	do {
            //         var x = stroka.indexOf(result[i],pn);
            //         console.log(x);
            //         console.log('Длина '+ result[i] + ' - ' + result[i].length);
            //         pn=x+1;
            //        } while (x!=-1)
            if (result[i] !== prelement) {
                var re1 = new RegExp(result[i], 'g');
                stroka = stroka.replace(re1, '<br><span style="font-weight: bold"> ' + result[i] + ' </span>');
                prelement = result[i];
            }

        }

    }
    else {
        result = ''
    }
    // otvet = stroka;
    return stroka
}