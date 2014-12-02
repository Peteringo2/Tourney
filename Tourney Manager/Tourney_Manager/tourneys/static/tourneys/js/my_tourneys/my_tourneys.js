//LOAD THE DATETIMEPICKER
$(document).ready(function() {
	$('#datetimepicker').datetimepicker();
});

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

//LOAD THE CREATE TOURNEY VIEW
$("#menu_create_tourney").click(function(){

	if($("#form_new_tourney").hasClass("hide"))
		$("#form_new_tourney").removeClass("hide");

	$("#tournaments").addClass("hide");

});

$(".tournaments").click(function(){

	if($(this).hasClass("hide"))
		$(this).removeClass("hide");

	$("#form_new_tourney").addClass("hide");

});

//SAVE USER INFORMATION
$("#add_tourney_btn").click(function(){

    //AJAX CALL TO THE SAVE PROFILE METHOD
    $.ajax({
        url : "../add_tourney/", // the endpoint
        type : "POST", // http method
        data : { name : $('#name').val(), game :  $('#game').val(), max_participants : $("#max_participants").val(), console : $("#sel-console").val(), start_date : $("#datetimepicker").data("DateTimePicker").getDate()._d }, // data sent with the post request
        success : function(response) {
            displayAlert("success_alert", " Tourney created successfully.");
        },
        error : function(xhr,errmsg,err) {
            displayAlert("error_alert", " An error occurred while creating the tournament");
        }
    });

});

function displayAlert(id, message){
    $("#" + id + " #content").empty().append(message);
    $("#" + id).css("display", "block");
}