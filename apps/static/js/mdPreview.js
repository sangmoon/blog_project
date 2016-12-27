function markdownPreview() {
    var pb = document.getElementById('preview_button');
    var target = document.getElementById('id_content');
    pb.addEventListener("click", function(){

        target.style.display = 'none';
        content = $("#id_content").val();

        $.ajax({
            type: 'get',
            url: '/markdown/',
            data: {
                'content': content
            },
            dataType: 'json',
            success: function (data) {
                //if(! document.body.contains()){
                    var cover = document.createElement('div');
                    cover.className = "mdPreview";
                    $(cover).append($.parseHTML(data.md_js));
                    $("#id_content").after(cover);

                //}
            }
        })
    });
}

function recover2WritingForm() {
    var wb = document.getElementById('write_button');
    var target = document.getElementById('id_content');
    wb.addEventListener("click", function() {
        target.style.display = 'inline';
        $(".mdPreview").remove();
    });
}

function addLoadEvent(func){
    var oldonload = window.onload;
    if(typeof window.onload != 'function') {
        window.onload = func;
    } else {
        window.onload = function() {
           if(oldonload) {
                oldonload();
            }
            func();
        }
    }
}

addLoadEvent(markdownPreview);
addLoadEvent(recover2WritingForm);
