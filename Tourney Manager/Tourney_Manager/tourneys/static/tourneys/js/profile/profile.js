// invoke the carousel
$('#myCarousel').carousel({
  interval: 3000
});

/* SLIDE ON CLICK */ 

$('.carousel-linked-nav > li > a').click(function() {

    // grab href, remove pound sign, convert to number
    var item = Number($(this).attr('href').substring(1));

    // slide to number -1 (account for zero indexing)
    $('#myCarousel').carousel(item - 1);

    // remove current active class
    $('.carousel-linked-nav .active').removeClass('active');

    // add active class to just clicked on item
    $(this).parent().addClass('active');

    // don't follow the link
    return false;
});

/* AUTOPLAY NAV HIGHLIGHT */

// bind 'slid' function
$('#myCarousel').bind('slid', function() {

    // remove active class
    $('.carousel-linked-nav .active').removeClass('active');

    // get index of currently active item
    var idx = $('#myCarousel .item.active').index();

    // select currently active item and add active class
    $('.carousel-linked-nav li:eq(' + idx + ')').addClass('active');

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
//--------------------------------

function displayAlert(id, message){
    $("#" + id + " #content").empty().append(message);
    $("#" + id).css("display", "block");
}

//SAVE USER INFORMATION
$("#save_btn").click(function(){
    //AJAX CALL TO THE SAVE PROFILE METHOD
    $.ajax({
        url : "../save_profile/", // the endpoint
        type : "POST", // http method
        data : { user : "{{request.user}}", country : $('#country').val() }, // data sent with the post request
        success : function(response) {
            displayAlert("success_alert", " Update on User information was successful.");
        },
        error : function(xhr,errmsg,err) {
            displayAlert("error_alert", " An error occurred while adding the code");
        }
    });

});

//ADD CONSOLE
$("#add_code_btn").click(function(){

    //AJAX CALL TO THE ADD CODE METHOD
    $.ajax({
        url : "../add_console/", // the endpoint
        type : "POST", // http method
        data : { friendcode : $('#friendcode').val(), nickname : $('#nickname').val(), console : $("#sel-console").val() },
        success : function(response) {
            displayAlert("success_alert", " Update on User information was successful.");
            location.reload();
            //CLEAR THE INPUT VALUES
        },
        error : function(xhr,errmsg,err) {
           displayAlert("error_alert", " An error occurred while adding the code");
        }
    });

});


//EDIT CONSOLE DATA
$("#code_btn").click(function(){

    var nickname_array = [];
    var friendcode_array = [];
    var console_array = [];

    $(".carousel-inner .item").each(function(i) {
        nickname_array.push( $( this ).find("#nickname").val() );
        friendcode_array.push( $( this ).find("#friendcode").val() );
    });

    $(".carousel-linked-nav li").each(function(i) {
        console_array.push( $(this).find("a").text() );
    });             
       
    //AJAX CALL TO THE EDIT CODE METHOD
    $.ajax({
        url : "../edit_console/", // the endpoint
        type : "POST", // http method
        data : { consoles : console_array, friendcodes : friendcode_array, nicknames :  nickname_array},
        success : function(response) {
            displayAlert("success_alert", " Update on Code information was successful.");
            console.log(response);
        },
        error : function(xhr,errmsg,err) {
           displayAlert("error_alert", " An error occurred while updating the code");
        }
    });
});

//CHECK IF USER HAS ALREADY ADD ALL OF THEIR CODES
if( $("#sel-console").has('option').length <= 0){
    $("#nickname").prop( "disabled", true );
    $("#friendcode").prop( "disabled", true );
    $("#sel-console").prop( "disabled", true );
    $("#add_code_btn").prop( "disabled", true );
}

