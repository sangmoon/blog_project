function markdownPreview() {
    var pb = document.getElementById('preview_button');
    var target = document.getElementById('id_content');
    pb.addEventListener("click", function(){
        //alert('Hello world');
        target.style.display = 'none';
    })
}

function recover2WritingForm() {
    var wb = document.getElementById('write_button');
    var target = document.getElementById('id_content');
    wb.addEventListener("click", function() {
        target.style.display = 'inline';
    })
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
