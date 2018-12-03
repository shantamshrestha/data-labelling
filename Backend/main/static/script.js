// alert("Here")
var url = 'http://127.0.0.1:5000'
function Login(){
    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;
    var d = {
        username: username,
        password : password,
    }
    $.ajax({
        type: 'POST',
        url:  url +'/auth/',
        data: JSON.stringify(d), // or JSON.stringify ({name: 'jonas'}),
        success: function(data) {
            console.log(data); 
            localStorage.setItem('token',data)
            window.location.replace(url+'/main/');
         },
        error : function(data,textStatus) { console.log(textStatus);
                alert('response: ' + data.responseText); 
        },
        contentType: "application/json",
        // dataType: 'json'
    });

}

