alert("this")
function Login(){
        var data = {
            "email":"Shantam",
            "password":"password"
        };
    $.post("http://127.0.0.1:5000/auth/",data,
        function(data,status){
            alert("Data: " +  data + "\nStatus" + status);
        });
    // $.get('http://127.0.0.1:5000/auth/home/',
    //     function(data,status){
    //         alert(data);
    //     }
    // )
}

