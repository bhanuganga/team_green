/**
 * Created by cfit005 on 14/9/16.
 */
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

function searching() {
    var hotel_name=$('#hotel_name').val();
    ajaxsetup();
    $.ajax({
        type:'POST',
        url:'/hotels_result',
        data:{'hotel_name':hotel_name},
        success:function (data) {
            if (data == "please select a hotel from list!") {
                $('#hotel_result').slideUp();
                $("#error").html(data).fadeOut(5000);
            }
            else {
                $('#hotel_result').html(data).slideDown();
            }

        }
    })
}

function booking(){
    var name=$('#name').val();
    var rent=$('#rent').val();
    var persons=$('#persons').val();
    var fromdate=$('#fromdate').val();
    var todate=$('#todate').val();
    ajaxsetup();
    $.ajax({
        type:'POST',
        url:'/booking',
        data:{'name':name,'rent':rent,'persons':persons,'fromdate':fromdate,'todate':todate},
        success: function (data) {
            $('#amount').text(data);
            setTimeout(function () {
                $('#hotel_result').slideUp('slow')
            },2500);
            setTimeout(function () {
                location.reload()
            },5000);

        }

    })
}
function cleardata() {
    ajaxsetup();
    $.ajax({
        type:'POST',
        url:'/clear',
        success:function (data) {
            location.reload()
        }

    })

}

function check(val) {
    if(val=='other'){
        $("#hotel_result").slideUp();
        $('#search_button').hide();
        $('#para').hide();
        $('#newhotel').show();
    }
    else{
        $('#search_button').show();
        $('#newhotel').hide();
    }

}

function addnewhotel() {
    var newhotel=$('#newhotelname').val();
    var newrent=$('#newrent').val();
    ajaxsetup();
    $.ajax({
        type:'POST',
        url:'/add_hotel',
        data:{'newhotel':newhotel,'newrent':newrent},
        success:function (data) {
            $('#newhotel').slideUp('slow');
            $('#hotel_result').html(data);
            setTimeout(function () {
                location.reload()
            },2000)
        }
    })

}

