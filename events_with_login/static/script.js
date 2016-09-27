
 callback='';

 // get csrf-token , this method is used before every ajax call
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !=='') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function ajaxsetup() {
    var csrftoken = getCookie('csrftoken');
    $.ajaxSetup({
        beforeSend: function (xhr) {
            if (!this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });
}

function ajax(url,data) {
    ajaxsetup();
    $.ajax({
        type: "POST",
        url: url,
        data: data,
        success: function (response) {
            if (response == 'no event found') {
                $("#message").text("No Events found").slideDown();
            }
            else {
                $("#message").html(response).slideDown();
            }
        },
        error: function () {
            var alertBox = '<div data-alert class="alert-box alert">Something wrong  <a href="#" class="close">&times;</a></div>';
            $("#error").empty().append(alertBox).foundation().fadeOut(6000);
        }
     });
}

function account(){
    if(!$(".registerDetails").submit().find(".error").is(":visible")) {
        var username = $('#username').val();
        var email = $('#email').val();
        var mobile = $('#mobile').val();
        var password = $('#password').val();
        ajaxsetup();
        $.ajax({
            type: 'POST',
            url: "/createaccount",
            data: {'username': username, 'email': email, 'mobile': mobile, 'password': password},
            success: function (response_data) {
                $('#signin').foundation('reveal', 'open');
                $("#accountmsg").html(response_data).fadeOut(5000);
                refreshforms();
            },
            error: function () {
                $("#accounterror").html('Something went wrong').fadeOut(5000);
            }
        });
    }
}

function login() {
    if(!$(".loginDetailsForm").submit().find(".error").is(":visible")) {
        var email = $('#emailaddress').val();
        var password = $('#password_login').val();
        ajaxsetup();
        $.ajax({
            type: 'POST',
            url: "/login",
            data: {'email': email, 'password': password},
            success: function (response_data) {
                if(response_data=='logged in') {
                    refreshforms();
                    callback();
                    setTimeout(function (){
                        window.location.reload();
                    },500);
                }
                else if(response_data !="Please Register"){
                    var alertBox = '<div data-alert class="alert-box warning">Your username and password doesnot match! <a href="#" class="close">&times;</a></div>';
                $("#accounterror").empty().append(alertBox).foundation().fadeOut(5000);

                }
                else {
                     var alertBox = '<div data-alert class="alert-box warning">Please Register! <a href="#" class="close">&times;</a></div>';
                    $("#accounterror").empty().append(alertBox).foundation().fadeOut(5000);
                }
            }
        });
    }
}

function refreshforms(){
    $(".loginFormInput").val("");
    $(".registerFormInput").val("");
    $(".loginDetailsForm div").removeClass("error");
    $(".loginDetailsForm label").removeClass("error");
    $(".registerDetails div").removeClass("error");
    $(".registerDetails label").removeClass("error");
}

 // Onclick add button with ajax calls
function add() {
    var name = $('#name').val();
    var date = $('#date').val();
    var info = $('#info').val();
    var cities = $('#cities').val();
    var city_other = $('#city1').val();
    var re = /^[a-z.A-Z ]+[a-z.A-Z.0-9]+[ .]*$/;
    if(re.test(name) && date != "" && re.test(info)  && /^\w+$/.test(cities)) {
        ajaxsetup();
        $.ajax({
            type:'POST',
            url:"/add",
            data:{'name':name, 'date':date, 'info':info, 'cities':cities, 'city1': city_other},
            success:function (response_data) {

                if(response_data=='Event added!') {
                    $("#success").html(response_data).fadeOut(2000);
                    $('#add_form')[0].reset();
                    setTimeout(function () {
                        location.reload()
                    },1000);
                }
                else{
                    callback=add();
                    $('#signin').foundation('reveal', 'open');


                }
            },
            error:function () {
                var alertBox = '<div data-alert class="alert-box alert">Something wrong! <a href="#" class="close">&times;</a></div>';
                $("#error").empty().append(alertBox).foundation().fadeOut(5000);
                setTimeout(function(){ location.reload(); }, 2500);
            }
        });
     }
     else{
         var alertBox = '<div data-alert class="alert-box warning">One or more invalid fields.  <a href="#" class="close">&times;</a></div>';
         $("#regexerror").empty().append(alertBox).foundation().fadeOut(5000);
         setTimeout(function(){ location.reload(); }, 2500);
     }
}

function Check(val){
    if(val=='other')
        $('#city1').show();
    else
        $('#city1').hide();
}

      //search_script
function search() {
    var event_is = $('#event_name').val();
    ajaxsetup();
    $.ajax({
        type:'POST',
        url:"/search",
        data:{'event_name':event_is},
        success:function (data) {
            if (data == "please select a name from list!") {
                $('#search_result').slideUp();
                $("#error").html(data).fadeOut(5000);
            }
            else {
                $('#search_result').html(data).slideDown();
            }
        }
    });
}


function update_event() {
    var event_id = $('#event_id').val();
    var upd_name = $('#upd_name').val();
    var upd_date = $('#upd_date').val();
    var upd_info = $('#upd_info').val();
    var email=$('#user_id').val();
    var city = $('#city').val();
    var re = /^[a-z.A-Z ]+[a-zA-Z0-9]+[ .]*$/;

    if(re.test(upd_name) && upd_date != "" && re.test(upd_info)  && /^\w+$/.test(city)){
        ajaxsetup();
        $.post("/update",
            {'id': event_id,'email':email, 'upd_name':upd_name, 'upd_date':upd_date, 'upd_city':city, 'upd_info':upd_info},
            function (response) {
                if(response=='EVENT UPDATED') {
                    $.when($("#search_result").html(response)).then(
                    setTimeout(function () {
                         window.location.reload();
                    },1500))
                }
                else{
                     callback=update_event();
                     $('#signin').foundation('reveal', 'open');
                }
            });
    }
    else{
        var alertBox = '<div data-alert class="alert-box warning">One or more invalid fields.  <a href="#" class="close">&times;</a></div>';
        $("#regexerror").empty().append(alertBox).foundation().fadeOut(5000);
    }
}


function delete_event() {
    var event_id = $('#event_id').val();
    ajaxsetup();
    $.post("/delete",
        {'id':event_id},
        function (response) {
            if(response=='EVENT DELETED') {
                $("#search_result").html(response);
                setTimeout(function () {
                    location.reload();
                }, 1000);
            }
            else {
                callback=delete_event();
                $('#signin').foundation('reveal', 'open');


          }
        });
}

function bydate(){
    var date=$('#date1').val();
    if( date != "") {
        var url="/by_date";
        var data={'date':date};
        ajax(url,data);
    }
     else{
        var alertBox = '<div data-alert class="alert-box warning">One or more invalid fields.  <a href="#" class="close">&times;</a></div>';
        $("#regexerror").empty().append(alertBox).foundation().fadeOut(6000);
        setTimeout(function(){ location.reload(); }, 1500);

    }

}

function bycity(){
    var city=$('#city').val();
    var url="/by_city";
    var data={'city':city};
    ajax(url,data);
}

function date_city(){
    var date=$('#date1').val();
    var city=$('#city1').val();
    if( date != "") {
        var url= "/by_date_and_city";
        var data={'date': date, 'city': city};
        ajax(url,data);
    }
    else{
        var alertBox = '<div data-alert class="alert-box warning">One or more invalid fields.  <a href="#" class="close">&times;</a></div>';
        $("#regexerror").empty().append(alertBox).foundation().fadeOut(5000);
        setTimeout(function(){ location.reload(); }, 1500);
    }
}

function by_date_range(){
    var fromdate = $('#from_date').val();
    var todate = $('#to_date').val();
    if (fromdate!=""&&todate!='') {
        var url= "/by_date_range";
        var data={'fromdate': fromdate, 'todate': todate};
        ajax(url,data);
    }
    else{
        var alertBox = '<div data-alert class="alert-box warning">One or more invalid fields.  <a href="#" class="close">&times;</a></div>';
        $("#regexerror").empty().append(alertBox).foundation().fadeOut(5000);
        setTimeout(function(){ location.reload(); }, 5000);
     }
}