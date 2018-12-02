// alert("Here")
function Login(){
    alert("here")
    var email = $('#username').text();
    var password = $('#password').text();
    alert("Her asdasde");
    $.post("http://127.0.0.1:5000/auth/",
        {
            "email":"Shantam",
            "password":"password"
        },
        function(data,status){
            alert("Data: " +  data + "\nStatus" + status);
        });
    // $.get('http://127.0.0.1:5000/auth/home/',
    //     function(data,status){
    //         alert(data);
    //     }
    // )
}

