$(document).on("click", ".change", function(event){

  event.preventDefault();
  event.stopPropagation();

  console.log("click")

  var celda = $(this);
  var valor = celda.text();

  create_combo_selected(celda);
  celda.attr("class","");
  

 // if(valor == " "){

//    celda.text("X");

//  }else{

 //   celda.text(" ");

 // }


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

function create_combo_selected(celda){
  var valor = celda.text();
  celda.text("");
console.log(valor);

  var url = '/horario/param/get_actividad/';
  var diccionario = {};
 console.log("HOLA1");

   $.ajax({
         type: "POST",
         url: url,
         data: diccionario,
         async: false,
        })
        .done(function(data){
          data = $.parseJSON(data);
          load_select_actividad(celda, data, valor)
        });

//html ='<select class="combo-option">';
 // html += '<option value=""> </option>';
 // html += '<option value="C" selected>C</option>';
 // html += '<option value="A">A</option>';
 // html += '<option value="L">L</option>';
 // html += '<option value="S">S</option>';
 // html += '</select>';
  
 // celda.append(html);
  

}

function load_select_actividad(widget, data, valor){

  var name = widget.attr("name");
  var txt = 'Seleccione un(a)  ${name}';
  var html = "";

  console.log("HOLA");

  //$(widget).append(
  //    $('<option></option>').val("").html(txt)
 //   );
    html +='<select class="combo-option">';
    html+= ('<option value=" "></option>');

  $.each(data, function(i, val){
    //console.log(val);
    //pk = val["pk"]
    txt = val["fields"]["identificador"]

   if(valor == txt){

      html+= ('<option value='+txt+' selected>'+txt+'</option>');

   }
    else{
    html+= ('<option value='+txt+'>'+txt+'</option>');
    }
    
    });
  html += '</select>';

  widget.append(html);


}

$(document).on("change", ".combo-option", function(event){

  event.preventDefault();

  var combo = $(this);
  var valor = combo.val();

  console.log(combo);

  td = $(this).parent();
  td.html(valor);
  td.attr('class', 'change');

  titulo_bloque = td.closest('table').find('th').eq(td.index());
  console.log(titulo_bloque.text());

  event.stopPropagation();

});
