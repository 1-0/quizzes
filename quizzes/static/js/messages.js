document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.modal');
    var instances = M.Modal.init(elems, 1);
    document.getElementById('msg_btn').click(); // ;-)
});
