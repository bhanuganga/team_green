function getCookie(name) {                                // to get csrf-token
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

$.ajaxSetup({
            beforeSend: function(xhr) {
                if (!this.crossDomain) {                // crossDomain is bool type
                    xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));//get cookie from getCookie(...) func
                }
            }
            });

$("#add_button").click(function() {                     // Onclick add button with ajax calls
        var name = $('#name').val();
        var date = $('#date').val();
        var info = $('#info').val();
        var cities = $('#cities').val();
        var other_city = $('#other_city').val();
        var re = /^[a-z.A-Z ]+[a-z.A-Z.0-9]+[ .]*$/;

        if(re.test(name) && date != "" && re.test(info)  && /^\w+$/.test(cities)) {
            $.ajax({
                type:'POST',
                url:"api/add",
                data:{
                    'name':name, 'date':date, 'info':info, 'cities':cities, 'other_city': other_city
                },
                success:function (response_data) {
                    alert(response_data);
                    $('#add_form')[0].reset();
                },
                error:function () {
                    alert("Something wrong")
                }
            });


        }
        else{
            alert("One or more invalid fields.");

        }
    });

$("#other_city").hide();
$("#cities").change(function(){          //#TODO task 1--DONE
 var new_city=$('#other_city');
 if($("#cities").val()!="Other")
   new_city.hide();
 else
   new_city.show();
});


$("#search_button").click(function() {                             //search_script
        var event_is = $('#event_is').val();
        var search_result_div = $("#search_result");
        $.post("api/search",
            {'event_is':event_is},
            function (data) {
                if (data == "please select a name from the list!") {
                    search_result_div.html(data).addClass("large-2");
                } else {
                    search_result_div.html(data).removeClass("large-2");
                }
            });
       });

// For elements(forms|btn|any_tag|result of ajax call ) populated as a result of an action normal onclick doesn't work,
// use following syntax: $('body').on('click', '#selector", handler|handler(){});
$('body').on('click', "#update_btn", function() {      //# TODO task 2--DONE update_script
    var event_id = $("#event_id").val();
    var upd_name = $("#upd_name").val();
    var upd_date = $("#upd_date").val();
    var upd_info = $("#upd_info").val();
    var upd_city = $("#upd_city").val();
    var re = /^[a-z.A-Z ]+[a-z.A-Z.0-9]+[ .]*$/;

    if(re.test(upd_name) && upd_date != "" && re.test(upd_info)  && /^\w+$/.test(upd_city)){
        $.post("api/update",
            {'id': event_id, 'upd_name':upd_name, 'upd_date':upd_date, 'upd_city':upd_city, 'upd_info':upd_info},
                function (response) {
                        location.reload();
                        alert(response);

                });

    }
    else{
        alert("One or more fields invalid");
    }
});


$('body').on("click","#delete_btn", function() {      //# TODO task 3--DONE delete_script
        var event_id = $('#event_id').val();
        $.post("api/delete",
            {'id':event_id},
        function (response) {
            location.reload();
            alert(response);

        });
});




$("#by_date_btn").click(function(){                  //# TODO task 4--DONE by_date_script
    var date=$('#date1').val();
    var message_div = $("#message");

    if( date != "") {

        $.ajax({
            type: "POST",
            url: "api/by_date",
            data: {'date': date},
            success: function (response) {
                if (response == []) {
                    location.reload();
                    alert("No events on selected date!");
                    }
                else {
                    message_div.html(response);
                    message_div.slideDown();
                }
            },
            error: function () {
                alert("Something wrong")
            }

        });
    }
        else{
        alert("One or more invalid fields.");

    }
});


$("#by_city_btn").click(function(){              //#TODO task 5--DONE by_city_script
    var city=$('#city').val();
    var message_div = $("#message");
    $.ajax({
        type: "POST",
        url: "api/by_city",
        data: {'city': city},
        success: function (data) {
            if (data == []) {
                alert("No events in selected city");
                location.reload();
            }
            else {
                message_div.html(data);
                message_div.slideDown();
            }
        },
            error:function () {
                alert("Something wrong")
            }
    });
});


$("#date_city_btn").click(function(){               //# TODO task 6--DONE date_city_script
    var date=$('#date_in_date_city').val();
    var city=$('#city_in_date_city').val();
    if( date != "") {
        $.ajax({
        type: "POST",
        url: "api/by_date_and_city",
        data: {'date': date, 'city': city},
        success: function (data) {
            if (data == []) {
                alert("Please try another choice");
                location.reload();
            }
            else {
                $("#message").html(data).slideDown();
            }
        },
        error: function () {
            alert("Something wrong")
        }

    });
}
    else{
        alert("One or more invalid fields.");

    }
});


$("#by_date_range_btn").click(function(){            //# TODO task 7--DONE date_range_script
    var from_date = $('#from_date').val();
    var to_date = $('#to_date').val();
    var message_div = $("#message");
   if (from_date!="" && to_date!="") {
       $.ajax({
           type: "POST",
           url: "api/by_date_range",
           data: {'from_date': from_date, 'to_date': to_date},
           success: function (data) {
               if (data == []) {
                   location.reload();
                   alert("No Events found");

               }
               else {
                   message_div.html(data);
                   message_div.slideDown();
               }
           },
           error: function () {
               alert("Something wrong");
           }

       });
   }
    else{
        alert("One or more invalid fields.");

    }
});

var current_url_path = $(location).attr('pathname');
switch (current_url_path) {
    case "/":
        $('#header-about').addClass("is-active");
        break;

    case "/add_event_html":
        $("#header-add-event").addClass("is-active");
        break;
    case "/search_modify_html" :
        $("#header-search-modify").addClass("is-active");
        break;

    case "/by_date_html":
    case "/by_city_html":
    case "/by_city_date_html":
    case "/by_date_range_html":
    case "/up_and_past":
        $("#header-filter").addClass("is-active");
        break;

}

$('body').on('click', '#sign_in',function () {
    var user_email = $("#user_email");
    var user_password = $("#user_pwd");
    $.ajax({url:"user/login",
        data:{"user_email":user_email, "user_password":user_password},
    success:function (response) {
        $.get("/", {'user_name':response});
    }
    });
});

$('body').on('click', "#register", function () {
    var register_name = $('#register_name').val();
    var register_email = $('#register_email').val();
    var register_phone = $('#register_phone').val();
    var register_password = $('#register_password').val();
    $.post("user/register",
        {'register_name':register_name, 'register_email':register_email, 'register_phone':register_phone, 'register_password':register_password},
    function (response) {
            $("#registered_msg").html(response);
            $('#registration_fields')[0].reset();
            $("#user_email").focus();
    });
});