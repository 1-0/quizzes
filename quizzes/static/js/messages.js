document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.modal');
    var instances = M.Modal.init(elems, 1);
    var instance = M.Modal.getInstance(elems[0]);
    instance.open();
//    M.toast({html: 'Data saved'})
});
