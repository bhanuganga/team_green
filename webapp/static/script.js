

        //bycity_script
    function bycity(){
        $.post("/by_city",$("form").serializeArray(),function(data){
            if(data=='no event found'){
                alert(data);
                }
            else{
                $("#message").html(data);
                }
        });
    }

    //bydate_script
    function bydate(){
        $.post("/by_date",$("form").serializeArray(),function(data){
            if(data=='no event found'){
                alert(data);
                }
            else{
                $("#message").html(data);
                }
        });
    }


    //date_city_script
    function date_city(){
        $.post("/by_date_and_city",$("form").serializeArray(),function(data){
            if(data=='no event found'){
                alert(data);
                }
            else{
                $("#message").html(data);
                }
        });
    }

    //daterange_script
   function bydate_range(){
        $.post("/by_daterange",$('form').serializeArray(),function(data){
            if(data=='no event found'){
                alert(data);
                }
            else{
                $('#ermsg').html(data);
                }
        });
    }

      //search_script

    function search() {
            $.post("/search", $('form').serializeArray(), function (data) {
                   if(data=="please select a name from list!"){
                        alert(data);
                   }
                   else{
                        $('#ermsg').html(data);
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

 function Check(val){
 var element=document.getElementById('city');
 if(val=='other')
   element.style.display='block';
 else
   element.style.display='none';
}

function add() {
        var name = $('#name').val();
        var date = $('#date').val();
        var info = $('#info').val();
        var cities = $('#cities').val();
        var re = /^[a-z.A-Z ]+[a-z.A-Z.0-9]+[ .]*$/

        if(re.test(name) && date != "" && re.test(info)  && /^\w+$/.test(cities)) {


            $.post("/add", $("#add_form").serializeArray(), function (response_data) {
                alert(response_data);
                $('#add_form')[0].reset();
            });

        }
        else{
            alert("One or more invalid fields.");

        }
    }