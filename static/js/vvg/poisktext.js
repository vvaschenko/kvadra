jQuery(document).ready(function () {

    var search_number = 0;
    var search_count = 0;
    var count_text = 0;
    var srch_numb = 0;

    function scroll_to_word() {
        var pos = $('#logpage .selectHighlight').position();
        $(document).scrollTop(pos.top);

    }

    $('#search_text').bind('keyup oncnange', function () {
        $('#ol_mini').removeHighlight();
        txt = $('#search_text').val();
        if (txt == '') return;
        $('#ol_mini').highlight(txt);
        search_count = $('#ol_mini span.highlight').size() - 1;
        count_text = search_count + 1;
        search_number = 0;
        $('#ol_mini').selectHighlight(search_number);
        if (search_count >= 0) scroll_to_word();
        $('#count').html('Найдено: <b>' + count_text + '</b>');
    });

    $('#clear_button').click(function () {
        $('#ol_mini').removeHighlight();
        $('#search_text').val('поиск');
        $('#count').html('');
        jQuery.scrollTo(0, 500, {queue: true});
    });

    $('#prev_search').click(function () {
        if (search_number == 0) return;
        $('#ol_mini span.selectHighlight').removeClass('selectHighlight');
        search_number--;
        srch_numb = search_number + 1;
        $('#ol_mini').selectHighlight(search_number);
        if (search_count >= 0) {
            scroll_to_word();
            $('#count').html('Показано: <b>' + srch_numb + '</b> из ' + $('#ol_mini span.highlight').size());
        }
    });

    $('#next_search').click(function () {
        if (search_number == search_count) return;
        $('#ol_mini span.selectHighlight').removeClass('selectHighlight');
        search_number++;
        srch_numb = search_number + 1;
        $('#ol_mini').selectHighlight(search_number);
        if (search_count >= 0) {
            scroll_to_word();
            $('#count').html('Показано: <b>' + srch_numb + '</b> из ' + $('#ol_mini span.highlight').size());
        }
    });

});