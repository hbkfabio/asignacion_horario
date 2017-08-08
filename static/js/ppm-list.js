//FIXME the document ready
$(document).ready(function() {
    // $('#dataTables-example').DataTable({
    //       responsive: true,
    //       "order": []

    // });

  $('form:not(.filter) :input:visible:enabled:first').focus()

  $('.input-sm').focus();

  var pathname = window.location.href.split("?");

  if (pathname.length > 1){

    pathname = pathname.pop();

    pathname = pathname.split("&");

    $.each(pathname, function(i, j){
      temp = j.split("=");
      $("#"+temp[0]).val(temp[1]);
    });

  }else{

    $("#periodo").attr("disabled", true);
    $("#plan").attr("disabled", true);

  }

});

function redirect(url, path){

    window.location.href = url + path

}


$(document).on("change", "#plan", function(event){

  event.preventDefault();

  var plan = $(this).find('option:selected').val();
  var periodo = $("#periodo").val();
  var carrera = $("#carrera").val();
  var url = window.location.pathname;

  if(plan != 0){

    if(periodo == 0){

      path = "?carrera="+carrera+"&plan="+plan;

    }else{

      path = "?carrera="+carrera+"&periodo="+periodo;
      path += "&plan="+plan;

    }


  }else{

    path = "?carrera="+carrera+"&periodo="+periodo;

  }

  redirect(url, path);

  event.stopPropagation();

});


$(document).on("change", "#periodo", function(event){

  event.preventDefault();

  var periodo = $(this).find('option:selected').val();
  var carrera = $("#carrera").val();
  var plan = $("#plan").val();
  var url = window.location.pathname;

  if(periodo != 0){

    path = "?carrera="+carrera+"&periodo="+periodo;

    if(plan !=0 && plan != null){

      path += "&plan="+plan;

    }

  }else{

    path = "?carrera="+carrera;

    if(plan !=0){

      path += "&plan="+plan;

    }

  }

  redirect(url, path)
  event.stopPropagation();

});

$(document).on("change", "#carrera", function(event){

  event.preventDefault();

  var carrera = $(this).find('option:selected').val();
  var periodo = $("#periodo").val();

  var url = window.location.pathname;

  if(carrera == 0){

    $("#periodo").attr("disabled", true);
    $("#plan").attr("disabled", true);
    path = "";

  }else{

    path = "?carrera="+carrera;

  }

  redirect(url, path)
  event.stopPropagation();

});
