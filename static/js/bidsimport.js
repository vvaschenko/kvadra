jQuery(document).ready(function () {
    // let file_input = '';

    // $('#close_import').click(function () {
    //     $('#myModal').modal('hide');
    //     // document.location.reload
    //     document.location.href;
    // });
    $("#groupbids").on('change',function () {
        let migration_bids = document.getElementById('migration_bids');
        migration_bids.disabled = false;
    });

    $('#import_bt').click(function () {
        $('#myModal').modal('hide');
        // document.getElementById(id).disabled = false;
        document.getElementById('nextimport').disabled = true;
        let file_input = document.getElementById('import_file').files[0].name;
        $("input[name='import_file']").val(file_input);
        let form_imp = document.forms['fileinfo'];
        let data_imp = new FormData(form_imp);
        data_imp.append('csrfmiddlewaretoken', getCookie('csrftoken'));
        data_imp.append('regim','import');
        // data_imp.append('user','');
        $('#import_file')[0].value = "";
        // let list_table = [];
        let list_table = new Object();
        // let list_table3 = [];
        let ind = 0;
        $.each($('#vtran')[0].rows,function () {
            if (ind>0){
                prom1 = this.cells[0].dataset.poledb;
                prom2 = this.cells[1].childNodes[0].children[0].selectedOptions[0].innerText;
                list_table[prom1]=prom2;
            }
            ind++
        });

        data_imp.append('list_table',JSON.stringify(list_table));
        data_imp.append('idgroup',$("#groupview :selected").val());

        $.ajax({
            url: '/bids/bidsimport/',
            type: 'POST',
            data: data_imp,
            processData: false,
            contentType: false,
            success: function (otvet, textStatus, XHR) {
                if (otvet['success']) {
                    // if (parseFloat(otvet.count_dubl) > 0) {
                    alert('Импорт завершен!!! ' +
                        '\n'+ 'Количество дублей - ' + otvet.count_dubl);
                    // }
                    // alert('Импорт завершен');
                    var current_host = document.location.host;
                    var current_protokol = document.location.protocol;
                    document.location.href = current_protokol + '//' + current_host+'/bids/bids/';
                    // document.location.reload;
                }else {
                    alert('Ошибка импорта!!! '+'\n' + otvet['error']);
                    document.location.assign(document.location.href)
                }

            },
            error: function (xhr, status, error) {
                alert('Возникла ошибка: Ошибка получения данных -' + xhr.responseText);
                $("#importview").remove();
            }
        });
    });
    $('#import_file').change(function (d) {
        document.getElementById('nextimport').disabled = false;
    })
});

function viewfilds(id) {
    let regim = 'viewfieldimport';
    // let data = {};
    let currentelement = document.getElementById(id);
    let file_input = document.getElementById('import_file').files[0].name;
    let submin_btn = document.getElementById('import_file');
    let form = $('form').get(0);
    let data = new FormData(form);
    // let data1 = new FormData(form);

    data.append('csrfmiddlewaretoken', getCookie('csrftoken'));
    data.append('regim','readfields');
    document.getElementById(id).disabled = true;
    $('#myModal').modal('show');
    $.ajax(
        {
            url: '/bids/bidsimport/',
            type: 'POST',
            data: data,
            processData: false,
            contentType: false,
            success: function (otvet, textStatus, XHR) {
                let data_detail = otvet;
                $('#importview').html(
                    '<form action="" method="POST" id="import" enctype="multipart/form-data">\n'+
                    '<div class="col-md-12" id="viewtran">' +
                    '<table class="table table-bordered" id="vtran">' +
                    '<thead>' +
                    '<tr role="row">' +
                    '<th><h4 align="center">Поле БД</h4></th>' +
                    '<th><h4 align="center">Солбец Excel</h4></th>' +
                    // '<th><h4 align="center">Поле БД</h4></th>' +
                    // '<th><h4 align="center">Солбец Excel</h4></th>' +
                    '</tr>' +
                    '</thead>' +
                    '<tbody id="trandetail">' +
                    '</tbody>' +
                    ' </table>' +
                    '</div>' +
                    '</form>'
                );
                var table = document.getElementById("vtran").tBodies[0];
                var ind = 0;
                // var sort_fields_name_db = sortMapByValue(otvet.fields_name_db);
                $.each(otvet.fields_name_db, function () {
                    row = table.insertRow(ind);
                    cell1 = row.insertCell(0);
                    cell2 = row.insertCell(1);

                    cell1.innerHTML = this[0];
                    cell1.dataset.poledb = this[1];
                    let my_id = 'instance_' + ind;
                    cell2.innerHTML = "<div id=\"repagnet\">\n" +
                        "<select name='instance' class='form-control' id='" + my_id + "' \n" +
                        "</select></div>";
                    let ind2 = 1;
                    // let my_id='instance_'+ind;
                    let my_select = document.getElementById(my_id).options;
                    my_select[my_select.length] = new Option('Выберите поле', true);
                    $.each(otvet.fields_name, function () {
                        my_select[my_select.length] = new Option(this, true);
                        ind2++;
                    });
                    ind++;
                });
            },
            error: function (xhr, status, error) {
                alert('Возникла ошибка: Ошибка получения данных -' + xhr.responseText);
                $("#importview").remove();
            }
        });

    $('#myModal').on('hide.bs.modal', function (e) {
        // $('#import_file')[0].value = "";
        // document.getElementById(id).disabled = false;
        // document.getElementById('nextimport').disabled = true;
        // document.location.assign(document.location.href)
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

function inputchange(ee) {
    document.getElementById('nextimport').disabled = false;
}

function sortMapByValue(map)
{
    var tupleArray = [];
    for (var key in map) tupleArray.push([key, map[key]]);
    tupleArray.sort(function (a, b) { return a[1] - b[1] });
    return tupleArray;
}
