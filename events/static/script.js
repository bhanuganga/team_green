
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
                 if (response == []) {
                    $("#message").text("No Events found").slideDown();
                 }
                 else {
                     $("#message").html(response).slideDown();
                 }
             },
             error: function () {
                 var alertBox = '<div data-alert class="alert-box alert">Something wrong  <a href="#" class="close">&times;</a></div>';
                 $("#error").append(alertBox).foundation().fadeOut(6000);

             }

         });

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
                 var alertBox = '<div data-alert class="alert-box success">EVENT ADDED  <a href="#" class="close">&times;</a></div>';
                 $("#success").append(alertBox).foundation().fadeOut(5000);
                 $('#add_form')[0].reset();
             },
             error:function () {
                 var alertBox = '<div data-alert class="alert-box">Something wrong! <a href="#" class="close">&times;</a></div>';
                 $("#error").append(alertBox).foundation().fadeOut(5000);
                 setTimeout(function(){ location.reload(); }, 2500);
             }
         });

     }
     else{
        var alertBox = '<div data-alert class="alert-box warning">One or more invalid fields.  <a href="#" class="close">&times;</a></div>';
         $("#regexerror").append(alertBox).foundation().fadeOut(5000);
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
    $.post("/search",
        {'event_name':event_is},
        function (data) {
            if(data=="please select a name from list!"){
                $('#search_result').slideUp();
               var alertBox = '<div data-alert class="alert-box">please select a name from list! <a href="#" class="close">&times;</a></div>';
                 $("#error").append(alertBox).foundation().fadeOut(5000);
            }
            else{
                $('#search_result').html(data).slideDown();
            }
        });
}


function update() {
    var event_id = $('#event_id').val();
    var upd_name = $('#upd_name').val();
    var upd_date = $('#upd_date').val();
    var upd_info = $('#upd_info').val();
    var city = $('#city').val();
    var re = /^[a-z.A-Z ]+[a-z.A-Z.0-9]+[ .]*$/;

    if(re.test(upd_name) && upd_date != "" && re.test(upd_info)  && /^\w+$/.test(city)){
        ajaxsetup();
        $.post("/update",
            {'id': event_id, 'upd_name':upd_name, 'upd_date':upd_date, 'upd_city':city, 'upd_info':upd_info},
            function (response) {

                var alertBox = '<div data-alert class="alert-box success">EVENT UPDATED  <a href="#" class="close">&times;</a></div>';
                 $("#success").append(alertBox).foundation();
                setTimeout(function(){ location.reload(); }, 1500);

            });
    }
    else{
     var alertBox = '<div data-alert class="alert-box warning">One or more invalid fields.  <a href="#" class="close">&times;</a></div>';
         $("#regexerror").append(alertBox).foundation().fadeOut(5000);
    }
}


function del() {
    var event_id = $('#event_id').val();
     ajaxsetup();
    $.post("/delete",
        {'id':event_id},
        function () {
           var alertBox = '<div data-alert class="alert-box success">EVENT DELETED  <a href="#" class="close">&times;</a></div>';
                 $("#success").append(alertBox).foundation();
                setTimeout(function(){ location.reload(); }, 1500);
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
    //bydate_script
 function bydate(){
     var date=$('#date1').val();
     if( date != "") {
         var url="/by_date";
         var data={'date':date};
        ajax(url,data);

     }
     else{
         var alertBox = '<div data-alert class="alert-box warning">One or more invalid fields.  <a href="#" class="close">&times;</a></div>';
         $("#regexerror").append(alertBox).foundation().fadeOut(6000);
         setTimeout(function(){ location.reload(); }, 1500);

     }

 }

        //bycity_script
 function bycity(){
     var city=$('#city').val();
     var url="/by_city";
         var data={'city':city};
        ajax(url,data);
 }

    //date_city_script
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
         $("#regexerror").append(alertBox).foundation().fadeOut(5000);
         setTimeout(function(){ location.reload(); }, 1500);

     }
 }

    //daterange_script
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
           $("#regexerror").append(alertBox).foundation().fadeOut(5000);
           setTimeout(function(){ location.reload(); }, 1500);

        }
    }