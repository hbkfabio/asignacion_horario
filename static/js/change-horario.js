$(document).on("click", ".change", function(event){

  event.preventDefault();
  event.stopPropagation();

  console.log("click")

  var celda = $(this);
  var valor = celda.text();


  if(valor == " "){

    celda.text("X");

  }else{

    celda.text(" ");

  }

  valor = celda.text();

  // var dia_semana = $(this).find('td:first');
  // var dia_semana = $(table).find('td:first').text() //
  // console.log(dia_semana);

  // var titulo_bloque = celda.closest('table').find('th').eq(celda.index());
  // titulo_bloque = titulo_bloque.text();
  // console.log(titulo_bloque);

  // var dia_semana = $(this).parents('tr:first').find('td:first').text();

  // console.log(dia_semana);

  //indice de columnas
  var col = $(this).parent().children().index($(this));
  var row = $(this).parent().parent().children().index($(this).parent());
  console.log('Row: ' + row + ', Column: ' + col);

  var param = {"colum": col,
              "row": row,
              "value": valor,

              }

  $.ajax({
     type: "POST",
     url: "/horario/save/",
     data: param,
     //async: false,
  })
    .done(function( data ){
      console.log(data);
  });


});
