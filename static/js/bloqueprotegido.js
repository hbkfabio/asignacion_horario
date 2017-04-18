$(document).on("click", ".put-x", function(event){

  event.preventDefault();

  cell = $(this);

  if (cell.text() == ""){

    value = cell.text("X");

  }else{

    value = cell.text("");

  }

  var bloque = cell.closest('table').find('th').eq(cell.index());

  var parametros = {"bloque":bloque.text(),
                    "value":value.text(),
                    };

  $.ajax({
      type: "POST",
      url: "/reservabloqueprotegido/save/",
      data: parametros,
      //async: false,
  })
    .done(function( data ){

    });

  event.stopPropagation();

});
