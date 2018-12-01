// $('btnLogin').click(function(){
//     $.post("Hello",
//         {
//             username:"Shantam",
//             password:"password"
//         },
//         function(data,status){
//             alert("Data: " +  data + "\nStatus" + status);
//         });
// });

function Login(){
    console.log("here")
    $.post("Hello",
        {
            username:"Shantam",
            password:"password"
        },
        function(data,status){
            alert("Data: " +  data + "\nStatus" + status);
        });
}

// $('#btnLogin').click(function(){
//     $.post("Hello",
//         {
//             username:"Shantam",
//             password:"password"
//         },
//         function(data,status){
//             alert("Data: " +  data + "\nStatus" + status);
//         });
// });

$(document).ready(function(){
    alert("Hello");
});

alert("hello")
// $(document).ready(function(){
//     $(".table").hover(function(){
//         alert("Hovering");
//     },
//     function(){
//         alert("Hovering done");
//     });
// });

$("#username").click(function(){
    $("#username").hide();
});
alert("hello")