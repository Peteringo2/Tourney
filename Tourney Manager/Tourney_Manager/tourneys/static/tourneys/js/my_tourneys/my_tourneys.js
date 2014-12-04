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

    var check_in = 'false';
    if ($('#check_in').is(":checked"))
        check_in = 'true';

    var error = false;

    if( $('#name').val() == "" ){
        displayAlert("error_alert", " Please enter a name for the tournament");
        error = true;
    }

    if( $('#game').val() == "" ){
        displayAlert("error_alert", " Please enter a game for the tournament");
        error = true;
    }

    if (!$.isNumeric($("#max_participants").val())) {
        displayAlert("error_alert", " Please enter a number for the Max Participants field");
        error = true;
    }

    var n_par = parseInt($("#max_participants").val());

    if( n_par < 2 || n_par > 256 ){
        displayAlert("error_alert", " Please enter a number between 2 and 256 for the Max Participants field");
        error = true;
    }

    if ( ! $..isNumeric($("#periodicity").val() ) ) {
        displayAlert("error_alert", " Please enter a number for the Periodicity field");
        error = true;
    }

    var n_periodicity = parseInt($("#periodicity").val());

    if(n_periodicity % 15 != 0){
        displayAlert("error_alert", " Periodicity must be a multiple of 15");
        error = true;
    }

    if(error)
        return;
    
    //AJAX CALL TO THE SAVE PROFILE METHOD
    $.ajax({
        url : "../add_tourney/", // the endpoint
        type : "POST", // http method
        data : { name : $('#name').val(), game :  $('#game').val(), max_participants : $("#max_participants").val(), console : $("#sel-console").val(), start_date : $("#datetimepicker").data("DateTimePicker").getDate()._d, periodicity : $("#periodicity").val(), check_in : check_in }, // data sent with the post request
        success : function(response) {
            //displayAlert("success_alert", " Tourney created successfully.");
            window.location.href = "http://mytourney.com:8000/tourneys/" + response + "/";
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