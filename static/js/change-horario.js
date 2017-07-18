$(document).on("click", ".change", function(event){

  event.preventDefault();
  event.stopPropagation();

  console.log("click")

  var celda = $(this);
  var valor = celda.text();
  var col = $(this).parent().children().index($(this));
  var row = $(this).parent().parent().children().index($(this).parent());

    valor = celda.text();
  create_combo_selected(celda);
  celda.attr("class","");
  // var dia_semana = $(this).find('td:first');
  // var dia_semana = $(table).find('td:first').text() //
  // console.log(dia_semana);

  

  // var dia_semana = $(this).parents('tr:first').find('td:first').text();

  // console.log(dia_semana);

  //indice de columnas
  
  console.log('Row: ' + row + ', Column: ' + col + ' Valor: '+ valor);

  


});

function save_combo_selected(celda, row, colum){
}

function create_combo_selected(celda){
  var valor = celda.text();
  celda.text("");

  //console.log('dato: '+valor);

  var url = '/horario/param/get_actividad/';
  var diccionario = {};


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
}

function load_select_actividad(widget, data, valor){

  var name = widget.attr("name");
  var txt = 'Seleccione un(a)  ${name}';
  var html = "";

    html +='<select class="combo-option">';
    html+= ('<option value=" "></option>');

  $.each(data, function(i, val){
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

  var col = $(td).parent().children().index($(td));
  var row = $(td).parent().parent().children().index($(td).parent());

  console.log("row: "+(row+1));

  //se coloca +1 porque los dias de la semana empiezan de 0
  row = (row+1)


  var periodo = $("#id_periodo").val();
  var carrera = $("#id_carrera").val();
  var plan = $("#id_plan").val();
  var modulo = $("#id_modulo").val();
  var profesor = $("#id_profesor").val();
  titulo_bloque = titulo_bloque.text();

  console.log("per: "+ periodo);
  console.log("car: "+ carrera);
  console.log("plan: "+ plan);
  console.log("mod: "+ modulo);
  console.log("prof: "+ profesor);
  console.log("bloque: "+titulo_bloque)

  var param = {"colum": col,
              "row": row,
              "value": valor,
              "periodo": periodo,
              "carrera": carrera,
              "plan": plan,
              "modulo": modulo,
              "profesor": profesor,
              "bloque": titulo_bloque,
              }

  console.log('datos: '+param);
  console.log('enviando datos');


    $.ajax({
     type: "POST",
     url: "/horario/save/",
     data: param,

     
  })
    .done(function(data){
      //console.log(data);
  });
  //console.log(titulo_bloque.text());


console.log('datos enviados');

  event.stopPropagation();

});
