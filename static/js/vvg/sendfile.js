/**
 * Created by dn111171vvg on 07.07.17.
 */
jQuery(document).ready(function (e) {
    e = e || window.event;
    $(".append-small-btn").on('change',function (e) {
        e.preventDefault();

        // if (window.File && window.FileReader && window.FileList && window.Blob) {
        //     alert('File API поддерживается данным браузером');
        // } else {
        //     alert('File API не поддерживается данным браузером');
        // }
        let photo_prof = document.getElementById('img_profileuser')
        let file_input = document.getElementById('avatar_file').files[0];
        let filename = file_input.name;
        // if(file_input){
        //      alert('Файл: '+filename);
        // }
        let contents;
        let filesize = file_input.size;
        // let filepath = file_input.path();
        let submin_btn = document.getElementById('append-small-btn');

        let fReader = new FileReader();

        fReader.onload = function(event) {
            contents = event.target.result;
            };

        fReader.onerror = function(event) {
            console.error("Файл не может быть прочитан! код " + event.target.error.code);
            alert("Файл не может быть прочитан! код " + event.target.error.code);
               };
        fReader.readAsArrayBuffer(file_input);

        // photo_prof.src = contents;

        submin_btn.value = filename;
    })
});
