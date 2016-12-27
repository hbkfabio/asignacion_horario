
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


$(document).on("click", ".accion", function(event){

  var val = $(this).text();
  var row = $(this).closest("tr").children('td');
  // var profesor = $(this).closest("tr").find(".profesor").text();
  // var modulo = $(this).closest("tr").find(".modulo").text();
  // var plan = $(this).closest("tr").find(".plan").text();

  if (val == ""){
    $(this).text("C");
  }else if(val == "C"){
    $(this).text("A");
  }else if(val == "A"){
    $(this).text("L");
  }else if( val == "L"){
    $(this).text("");
  }


  dic = {}
  row.each(function(){
    dic[$(this).attr("class")] = $(this).text();
  })

  console.log(dic);

  dic = JSON.stringify(dic)

  var parametros = {"diccionario":dic}
  //             "valor":val,
  //             "profesor":profesor,
  //             "modulo":modulo,
              // "bloque":cabecera,
  //             "plan":plan}

   $.ajax({
       type: "POST",
       url: "/horario/save/",
       data: parametros,
      })
      .done();

});


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
