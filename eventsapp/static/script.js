function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
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


function setup(csrftoken) {
    $.ajaxSetup({
        beforeSend: function(xhr) {
            if (!this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });
}

function refreshLoginForm() {
    $(".loginFormInput").val(""),
    $(".registerFormInput").val(""),
    $(".loginDetailsForm div").removeClass("error"),
    $(".loginDetailsForm label").removeClass("error"),
    $(".registerDetails div").removeClass("error"),
    $(".registerDetails label").removeClass("error")
}

function login() {
    var email_id = $('#login_emailid').val();
    var password = $('#login_password').val();
    
    if (email_id != '' && password != '') {
        var csrftoken = getCookie('csrftoken');
        setup(csrftoken);

        $.ajax({
            type: 'POST',
            url: "/logged_in",
            data: {
                'email_id': email_id, 'password': password
            },
            success: function (response_data) {
                $("#onsuccess").html(response_data);
            }
        });
    }
    else{
        var alertBox = '<div data-alert class="alert-box warning radius"> One or more invalid fields.  <a href="#" class="close">&times;</a></div>';
        $("#message").append(alertBox).foundation().fadeOut(5000);
    }
}

function signup() {
    var username = $('#username').val();
    var email_id = $('#email_id').val();
    var ph_no = $('#ph_no').val();
    var password = $('#password').val();
    var re = /^[a-zA_Z]+[a-zA-Z0-9]+[ .]*$/;

    if (re.test(username) && re.test(password) && ph_no != '' && email_id != '') {
        var csrftoken = getCookie('csrftoken');
        setup(csrftoken);

        $.ajax({
            type: 'POST',
            url: "/signed",
            data: {
                'username': username, 'email_id': email_id, 'ph_no':ph_no, 'password': password
            },
            success: function (response_data) {
                $("#onsuccess").html(response_data);
                $('#myModal').modal({
                    backdrop: 'static',
                    keyboard: false  // to prevent closing with Esc button (if you want this too)
                })
            }

        });
    }

    else{
        var alertBox = '<div data-alert class="alert-box warning radius"> One or more invalid fields.  <a href="#" class="close">&times;</a></div>';
        $("#message").append(alertBox).foundation().fadeOut(5000);
    }
}



function add() {
    var name = $('#name').val();
    var date = $('#date').val();
    var info = $('#info').val();
    var cities = $('#cities').val();
    var city_other = $('#city1').val();
    var re = /^[a-z.A-Z ]+[a-z.A-Z.0-9]+[ .]*$/;

    if(re.test(name) && date != "" && re.test(info)  && /^\w+$/.test(cities)) {

        var csrftoken = getCookie('csrftoken');
        setup(csrftoken);

        $.ajax({
            type:'POST',
            url:"/add",
            data:{
                'name':name, 'date':date, 'info':info, 'cities':cities, 'city1': city_other
            },
            success:function (response_data) {
                var alertBox = '<div data-alert class="alert-box success radius"> Event added successfully.  <a href="#" class="close">&times;</a></div>';
                $("#onsuccess").append(alertBox).foundation().fadeOut(5000);
                $('#add_form')[0].reset();
            },
            error:function () {
                var alertBox = '<div data-alert class="alert-box alert radius"> Something wrong.  <a href="#" class="close">&times;</a></div>';
                $("#message").append(alertBox).foundation().fadeOut(5000);
            }
        });
    }

    else{
        var alertBox = '<div data-alert class="alert-box warning radius"> One or more invalid fields.  <a href="#" class="close">&times;</a></div>';
        $("#message").append(alertBox).foundation().fadeOut(5000);
    }
}


function Check(val){
    var element=$('#city1');
    if(val=='other')
        element.show();
    else
        element.hide();
}



function search() {
    var event_id = $('#event_name').val();

    var csrftoken = getCookie('csrftoken');
    setup(csrftoken);

    $.ajax({
        type: "POST",
        url: "/search",
        data: {'event_name': event_id},
        success: function (data) {
            if (data == "please select a name from list!") {
                var alertBox = '<div data-alert class="alert-box success radius"> Select a name.  <a href="#" class="close">&times;</a></div>';
                $("#message").append(alertBox).foundation().fadeOut(5000);
            }
            else {
                $('#onsuccess').html(data);
            }
        },
        error:function () {
            var alertBox = '<div data-alert class="alert-box alert radius"> Something wrong.  <a href="#" class="close">&times;</a></div>';
            $("#message").append(alertBox).foundation().fadeOut(5000);
        }

    });
}


function updat() {
    var event_id = $('#event_id').val();
    var upd_name = $('#upd_name').val();
    var upd_date = $('#upd_date').val();
    var upd_info = $('#upd_info').val();
    var city = $('#city').val();
    var re = /^[a-z.A-Z ]+[a-z.A-Z.0-9]+[ .]*$/;

    if(re.test(upd_name) && upd_date != "" && re.test(upd_info)  && /^\w+$/.test(city)) {

        var csrftoken = getCookie('csrftoken');
        setup(csrftoken);

        $.ajax({
            type: "POST",
            url: "/update",
            data: {'id': event_id, 'upd_name': upd_name, 'upd_date': upd_date, 'upd_city': city, 'upd_info': upd_info},
            success: function (response) {
                    setTimeout(function () {
                        location.reload();
                    }, 5000);
                    var alertBox = '<div data-alert class="alert-box success radius"> Event updated.  <a href="#" class="close">&times;</a></div>';
                    $("#message").append(alertBox).foundation().fadeOut(5000);
                },
            error: function() {
                var alertBox = '<div data-alert class="alert-box alert radius"> Something wrong.  <a href="#" class="close">&times;</a></div>';
                $("#message").append(alertBox).foundation().fadeOut(5000);
            }
        });
    }

    else{
        var alertBox = '<div data-alert class="alert-box warning radius"> One or more invalid fields.  <a href="#" class="close">&times;</a></div>';
        $("#message").append(alertBox).foundation().fadeOut(5000);
    }
}


function del() {
    var event_id = $('#event_id').val();

    var csrftoken = getCookie('csrftoken');
    setup(csrftoken);

    $.ajax({
        type: "POST",
        url: "/delete",
        data: {'id': event_id},
        success: function (response) {
            setTimeout(function () {
                location.reload();
            },5000);
            var alertBox = '<div data-alert class="alert-box success radius"> Event deleted.  <a href="#" class="close">&times;</a></div>';
            $("#message").append(alertBox).foundation().fadeOut(5000);
        }
    });
}


function setSelectedIndex(s, v) {
    for ( var i = 0; i < s.options.length; i++ ) {
        if ( s.options[i].text == v ) {
            s.options[i].selected = true;
            return;
        }
    }
}


function bycity(){
    var city=$('#city').val();

    var csrftoken = getCookie('csrftoken');
    setup(csrftoken);

    $.ajax({
        type: "POST",
        url: "/by_city",
        data: {'city': city},
        success: function (data) {
            if (data == 'no event found') {
                var alertBox = '<div data-alert class="alert-box success radius"> No event found.  <a href="#" class="close">&times;</a></div>';
                $("#message").append(alertBox).foundation().fadeOut(5000);
                setTimeout(function () {
                    location.reload();
                },1000);
            }
            else {
                $("#onsuccess").html(data);
            }
        },
        error:function () {
            var alertBox = '<div data-alert class="alert-box alert radius"> Something wrong.  <a href="#" class="close">&times;</a></div>';
            $("#message").append(alertBox).foundation().fadeOut(5000);
            setTimeout(function () {
                location.reload();
            },1000);
        }
    });
}


function bydate(){
    var date=$('#date1').val();

    if(date != "") {

        var csrftoken = getCookie('csrftoken');
        setup(csrftoken);

        $.ajax({
            type: "POST",
            url: "/by_date",
            data: {'date': date},
            success: function (data) {
                if (data == 'no event found') {
                    var alertBox = '<div data-alert class="alert-box success radius"> No event found.  <a href="#" class="close">&times;</a></div>';
                    $("#message").append(alertBox).foundation().fadeOut(5000);
                    setTimeout(function () {
                        location.reload();
                    },1000);
                }
                else {
                    $("#onsuccess").html(data);
                }
            },
            error:function () {
                var alertBox = '<div data-alert class="alert-box alert radius"> Something wrong.  <a href="#" class="close">&times;</a></div>';
                $("#message").append(alertBox).foundation().fadeOut(5000);
                setTimeout(function () {
                    location.reload();
                },1000);
            }
        });
    }

    else{
        var alertBox = '<div data-alert class="alert-box warning radius"> One or more invalid fields.  <a href="#" class="close">&times;</a></div>';
        $("#message").append(alertBox).foundation().fadeOut(5000);
        setTimeout(function () {
            location.reload();
        },1000);
    }
}


function date_city(){
    var date=$('#date1').val();
    var city=$('#city').val();

    if(date != "") {

        var csrftoken = getCookie('csrftoken');
        setup(csrftoken);

        $.ajax({
            type: "POST",
            url: "/by_date_and_city",
            data: {'date': date, 'city':city},
            success: function (data) {
                if (data == 'no event found') {
                    var alertBox = '<div data-alert class="alert-box success radius"> No event found.  <a href="#" class="close">&times;</a></div>';
                    $("#message").append(alertBox).foundation().fadeOut(5000);
                    setTimeout(function () {
                        location.reload();
                    },1000);
                }
                else {
                    $("#onsuccess").html(data);
                }
            },
            error:function () {
                var alertBox = '<div data-alert class="alert-box alert radius"> Something wrong.  <a href="#" class="close">&times;</a></div>';
                $("#message").append(alertBox).foundation().fadeOut(5000);
                setTimeout(function () {
                    location.reload();
                },1000);
            }
        });
    }

    else{
        var alertBox = '<div data-alert class="alert-box warning radius"> One or more invalid fields.  <a href="#" class="close">&times;</a></div>';
        $("#message").append(alertBox).foundation().fadeOut(5000);
        setTimeout(function () {
            location.reload();
        },1000);
    }
}


function by_date_range(){
    var fromdate = $('#from').val();
    var todate = $('#to').val();

    if(fromdate != "" && todate != "") {
       
        var csrftoken = getCookie('csrftoken');
        setup(csrftoken);

        $.ajax({
            type: "POST",
            url: "/by_date_range",
            data: {'fromdate': fromdate, 'todate':todate},
            success: function (data) {
                if (data == 'no event found') {
                    var alertBox = '<div data-alert class="alert-box success radius"> No event found.  <a href="#" class="close">&times;</a></div>';
                    $("#message").append(alertBox).foundation().fadeOut(5000);
                    setTimeout(function () {
                        location.reload();
                    },1000);
                }
                else {
                    $("#onsuccess").html(data);
                }
            },
            error:function () {
                var alertBox = '<div data-alert class="alert-box alert radius"> Something wrong.  <a href="#" class="close">&times;</a></div>';
                $("#message").append(alertBox).foundation().fadeOut(5000);
                setTimeout(function () {
                    location.reload();
                },1000);
            }
        });
    }

    else{
        var alertBox = '<div data-alert class="alert-box warning radius"> One or more invalid fields.  <a href="#" class="close">&times;</a></div>';
        $("#message").append(alertBox).foundation().fadeOut(5000);
        setTimeout(function () {
            location.reload();
        },1000);
    }
}
