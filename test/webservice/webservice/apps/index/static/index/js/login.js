$("#login-button").click(function(event){
    event.preventDefault();
    var url = "/index/menu";
    user = $("#Usuario").val()
    pass = $("#Contrasena").val()
    if(user == "admin" && pass == "admin"){
        $('form').fadeOut(500);
        $('.wrapper').addClass('form-success');    
        setTimeout(
            function() 
            {
                document.location.href = url;
            }, 2500);
    }
});