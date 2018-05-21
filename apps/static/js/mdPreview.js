function markdownPreview() {
    var pb = document.getElementById('preview_button');
    var wb = document.getElementById('write_button');
    var target = document.getElementById('id_content');
    pb.addEventListener("click", function(){

        target.style.display = 'none';
        content = $("#id_content").val();

        $.ajax({
            type: 'get',
            url: '/markdown',
            data: {
                'content': content
            },
            timeout: 5000,
            dataType: 'json',
            success: function (data, status) {
              var cover = document.createElement('div');
              cover.className = "mdPreview";
              $(cover).append($.parseHTML(data.md_js));
              $("#id_content").after(cover);
              pb.disabled = true;
              wb.disabled = false;
            },
            error: function (xhr, status, error) {
              var cover = document.createElement('div');
              cover.className = "mdPreview";
              $(cover).append($.parseHTML(xhr.responseText));
              $("#id_content").after(cover);
              pb.disabled = true;
              wb.disabled = false;

            }
        })
    });
}

function recover2WritingForm() {
    var pb = document.getElementById('preview_button');
    var wb = document.getElementById('write_button');
    var target = document.getElementById('id_content');
    wb.addEventListener("click", function() {
        target.style.display = 'inline';
        $(".mdPreview").remove();
        pb.disabled= false;
        wb.disabled = true;
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
