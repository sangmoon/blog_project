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

                $("#id_content").after(data.md_js);
            }
        })
    });
}


function recover2WritingForm() {
    var wb = document.getElementById('write_button');
    var target = document.getElementById('id_content');
    wb.addEventListener("click", function() {
        target.style.display = 'inline';
        $(".highlight").remove();
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
