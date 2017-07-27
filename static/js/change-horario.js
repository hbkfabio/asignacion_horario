$(document).on("click", ".change", function(event){

  event.preventDefault();
  event.stopPropagation();

  console.log("click")

  var celda = $(this);
  var valor = celda.text();
  var col = $(this).parent().children().index($(this));
  var row = $(this).parent().parent().children().index($(this).parent());

  valor = celda.text();

  var periodo = $("#id_periodo").val();
  var carrera = $("#id_carrera").val();
  var plan = $("#id_plan").val();
  var modulo = $("#id_modulo").val();
  var profesor = $("#id_profesor").val();

  /*
    Siempre el primer valor de un select (combo) es un texto en blanco ""
    Definido en la load_select_data de horario.js
  */
  if (periodo == ""){
    alert("Seleccione un campo de Periodo");
  }else if (carrera == ""){
    alert("Seleccione una Carrera");
  }else if (plan == ""){
    alert("Seleccione un Plan de Estudio");
  }else if (modulo == ""){
    alert("Seleccione un Módulo");
  }else if(profesor == ""){
    alert ("Seleccione un Profesor");
  }else{
    create_combo_selected(celda);
    celda.attr("class","");
  }



});


function create_combo_selected(celda){
  var valor = celda.text();

  celda.text("");

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


$(document).on("change", ".combo-option", function(event){

  event.preventDefault();

  var combo = $(this);
  var valor = combo.val();

  td = combo.parent();
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


function load_select_actividad(widget, data, valor){

  var name = widget.attr("name");
  //var txt = 'Seleccione un(a)  ${name}';
  var html = "";

  html +='<select class="combo-option">';
  html+= ('<option value=""></option>');

  $.each(data, function(i, val){
    //console.log(val);
    //pk = val["pk"]
    txt = val["fields"]["identificador"]
    console.log("txt: " + txt)
    console.log("valor: " + valor)

   if(valor == txt){

      html+= ('<option value='+txt+' selected>'+txt+'</option>');

   }else{

    html+= ('<option value='+txt+'>'+txt+'</option>');

    }
  });

  html += '</select>';

  widget.append(html);

}
