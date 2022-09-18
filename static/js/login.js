var LoginLogic = {
    'url': `${location.origin}/api/token/`,

    fetchToken(username, password) {
        fetch(this.url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                'password': password,
                'username': username
            })
        }
        ).then(response => response.json()).then(data => {
            console.log(data);
            localStorage.setItem('data', data)
            if (data.access) {
                localStorage.setItem('token', data.access);
            }
            else {
                alert(data.detail);
            }
        })
    }
}

var submitLoginform = document.getElementById('send2');
var Loginform = document.getElementById('login-form');

submitLoginform.onclick = function() {
    const username = document.querySelector('#id_username').value;
    const password = document.querySelector('#id_password').value;
    LoginLogic.fetchToken(username, password);
    setTimeout(Loginform.submit(), 1000);
}