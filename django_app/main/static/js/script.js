$(document).ready(function(){
    $('#loginButton').click(function(){
        username = $('#loginUsername').val()
        password =  $('#loginPassword').val()
        
        if (username == "admin" && password == "admin"){
            window.open("admin.html");
            console.log('Successfully Login');
        }
        else{
            console.log('Not Admin');
        }
    })
    console.log("Successfully linked!");
})