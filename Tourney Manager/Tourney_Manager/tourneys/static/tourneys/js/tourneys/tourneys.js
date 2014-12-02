//LOAD THE TOKE TO MAKE AJAX CALLS
var csrftoken = $.cookie('csrftoken');

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
//--------------------------------

function displayAlert(id, message){
    $("#" + id + " #content").empty().append(message);
    $("#" + id).css("display", "block");
}

$("#sign_up").click(function(){

    //AJAX CALL TO THE EDIT CODE METHOD
    $.ajax({
        url : "../sign_up/", // the endpoint
        type : "POST", // http method
        data : { tourney_id : $("#tourney_id").text() },
        success : function(response) {
            if(response == "False")
                displayAlert("error_alert", " You do not have a registered code for the Tournament's console");
            else{
                displayAlert("success_alert", " Successfully sign up to the tournament");
                location.reload();
            }
            
        },
        error : function(xhr,errmsg,err) {
           displayAlert("error_alert", " An error occurred while trying to sign up for the tournament");
        }
    });

});