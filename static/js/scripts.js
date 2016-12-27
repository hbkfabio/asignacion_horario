
//FIXME the document ready
$(document).ready(function() {
    $('#dataTables-example').DataTable({
          responsive: true
    });


    var pathname = window.location.href.split("=")[1];
    console.log(pathname);
    $("#periodo").val(pathname);

});


$(document).on("click", ".edit", function(event){

    var pathname = window.location.pathname;
    var id = $(this).val();
    window.location.href = pathname+"edit/"+id;
});


$(document).on("click", ".delete", function(event){

    var pathname = window.location.pathname;
    var id = $(this).val();
    window.location.href = pathname+id+"/delete/";
});


$(document).on("click", ".add", function(event){

    var pathname = window.location.pathname;
    var id = $(this).val();
    window.location.href = pathname+"add/";
});


$(document).on("click", "button[type='reset']", function(){
    var pathname = window.location.pathname.split("/")[1];
    pathname="/"+pathname+"/";
    window.location.href =pathname;

});


$(document).on("click", ".save-addother", function(event){

    alert("hola");
     var pathname = window.location.pathname;
    // var id = $(this).val();
    window.location.href = pathname+"add/";
});


$(document).on("click", ".actividades", function(event){

  var val = $(this).text();
  var profesor = $(this).closest("tr").find(".profesor").text();
  var profesor = $(this).closest("tr").find(".modulo").text();
  var profesor = $(this).closest("tr").find(".plan").text();

  console.log(val);
  //console.log(profesor);

  if (val == ""){
    $(this).text("C");
  }else if(val == "C"){
    $(this).text("A");
  }else if(val == "A"){
    $(this).text("L");
  }else if( val == "L"){
    $(this).text("");
  }

  val = $(this).text();
  console.log(val);

});


// $(document).on("change", "#periodo", function(event){

//     var pathname = window.location.pathname;
    // console.log(pathname);

//     var combo = $(this).find('option:selected').val();

//     $.get({% url "HorarioTemplateView" %}, { periodo:combo }, function(event){})
//       .done(function( data ) {
        // window.location.href = pathname;
//       });

// });


$(document).on("change", "#periodo", function(event){

    var combo = $(this).find('option:selected').val();
    var pathname = window.location.pathname;
    window.location.href = pathname + "?periodo="+combo;

    //change_combo_periodo(combo);


    // $.ajax({
    //         type: "GET",
            //url: "/horario1/add",
    //         data: { 'periodo': combo }
    //     })
    //      .done(function(response) {
    //         $("#wrapper").empty();
    //         $('#wrapper').html(response);
    //         $("#periodo").val(combo);
    //     });

    // event.stopPropagation();
    // event.preventDefault();
});
