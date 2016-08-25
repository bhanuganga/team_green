function getCookie(name) {                                // get csrf-token , this method is used before every ajax call
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
                if (!this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));//get cookie from getCookie(...) func
                }
            }
            });

$("#add_button").click(function() {                                    // Onclick add button with ajax calls
        var name = $('#name').val();
        var date = $('#date').val();
        var info = $('#info').val();
        var cities = $('#cities').val();
        var city_other = $('#city1').val();
        var re = /^[a-z.A-Z ]+[a-z.A-Z.0-9]+[ .]*$/;

        if(re.test(name) && date != "" && re.test(info)  && /^\w+$/.test(cities)) {
            $.ajax({
                type:'POST',
                url:"api/add",
                data:{
                    'name':name, 'date':date, 'info':info, 'cities':cities, 'city1': city_other
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

$("#cities").change(function(){          //#TODO task 1
 var element=$('#city1');
 if(this.val()=="Other")
   element.show();
 else
   element.hide();
});


$("#search_button").click(function() {                             //search_script
        var event_is = $('#event_is').val();
        $.post("api/search",
            {'event_is':event_is},
            function (data) {
                if (data == "please select a name from list!") {
                    $('#search_result').html(data);
                    $('#search_result').addClass("large-2");
                } else {
                    $('#search_result').html(data);
                    $('#search_result').removeClass("large-2");
                }
            });
       });


$("#update_btn").click(function() {                          //# TODO task 2 update_script
    var event_id = $("#event_id").val();
    var upd_name = $("#upd_name").val();
    var upd_date = $("#upd_date").val();
    var upd_info = $("#upd_info").val();
    var upd_city = $("#city").val();
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
        alert("One or more fields invalid")
    }
});


$("#delete_btn").click(function() {                                //# TODO task 3 delete_script
        var event_id = $('#event_id').val();
        $.post("api/delete",
            {'id':event_id},
        function (response) {
            location.reload();
            alert(response);

        });
});

function setSelectedIndex(s, v) {               // For pre-selecting the city

    for ( var i = 0; i < s.options.length; i++ ) {

        if ( s.options[i].text == v ) {

            s.options[i].selected = true;

            return;

        }

    }

}

function by_date(){                  //# TODO task 4 by_date_script
    var date=$('#date1').val();

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
                    $("#message").html(response);
                    $("#message").slideDown();
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
}


function by_city(){              //#TODO task 5 by_city_script
    var city=$('#city').val();
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
                $("#message").html(data);
                $("#message").slideDown();
            }
        },
            error:function () {
                alert("Something wrong")
            }
    });
}


function date_city(){               //# TODO task 6  date_city_script
    var date=$('#date1').val();
    var city=$('#city1').val();
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
}


function by_date_range(){            //# TODO task 7date_range_script
   var date1 = $('#date3').val();
   var date2 = $('#date2').val();

   if (date1!=""&&date2!='') {
       $.ajax({
           type: "POST",
           url: "api/by_date_range",
           data: {'date1': date1, 'date2': date2},
           success: function (data) {
               if (data == []) {
                   location.reload();
                   alert("No Events found");

               }
               else {
                   $("#message").html(data);
                   $("#message").slideDown();
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
}
