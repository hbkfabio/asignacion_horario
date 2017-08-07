$(document).on("click", ".change", function(event){

  event.preventDefault();
  event.stopPropagation();

  var celda = $(this);
  var valor = celda.text();

  if (valor == "X"){

    return false;

  }

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

    Si es nulo es que el cambio se realiza desde el módulo de Horario.
  */
  if (periodo == null){



  }else{

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
  }


});

$(document).on("click", ".change-horario", function(event){

  event.preventDefault();

  var celda = $(this);
  var valor = celda.text();

  if (valor == "X"){

    return false;

  }

  create_combo_selected(celda);
  celda.attr("class","");

  event.stopPropagation();

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


function save_horario(param, td){

  $.ajax({
      type: "POST",
      dataType: "json",
      url: "/horario/save/",
      data: param,
    })
    .done(function(data){
      if (!data.success){
         alert(data.msj);
         td.text("");
      }

  });

}


$(document).on("change", ".combo-option-horario", function(event){

  event.preventDefault();

  var combo = $(this);
  var valor = combo.val();


  var td = combo.parent();

  titulo_bloque = td.closest('table').find('th').eq(td.index());
  titulo_bloque = titulo_bloque.text();

  table = td.parent().parent().parent();
  dia_semana = table.attr("id");

  file = td.parents("tr");
  profesor = file.find("td:eq(0)");
  profesor = profesor.attr("name");

  modulo = file.find("td:eq(1)");
  modulo = modulo.attr("name");

  plan = file.find("td:eq(0)");
  plan = plan.attr("name");

  carrera = $("#carrera").val();
  periodo = $("#periodo").val();

  // var col = "";
  td.html(valor);
  td.attr('class', 'change-horario');


  var param = {
              "row": dia_semana,
              "value": valor,
              "periodo": periodo,
              "carrera": carrera,
              "plan": plan,
              "modulo": modulo,
              "profesor": profesor,
              "bloque": titulo_bloque,
              }

  save_horario(param, td);



  event.stopPropagation();

});


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

  //se coloca +1 porque los dias de la semana empiezan de 0
  row = (row+1)

  var periodo = $("#id_periodo").val();
  var carrera = $("#id_carrera").val();
  var plan = $("#id_plan").val();
  var modulo = $("#id_modulo").val();
  var profesor = $("#id_profesor").val();
  titulo_bloque = titulo_bloque.text();

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


  save_horario(param, td);

  event.stopPropagation();

});


function load_select_actividad(widget, data, valor){

  var name = widget.attr("name");
  //var txt = 'Seleccione un(a)  ${name}';
  var html = "";
  var url = window.location.pathname;
  url = url.split("/")[1];

  if (url == "periodoprofesormodulo"){

    html +='<select class="combo-option">';

  }else if(url == "horario"){

    html +='<select class="combo-option-horario">';

  }

  html+= ('<option value=""></option>');

  $.each(data, function(i, val){

    txt = val["fields"]["identificador"]

   if(valor == txt){

      html+= ('<option value='+txt+' selected>'+txt+'</option>');

   }else{

    html+= ('<option value='+txt+'>'+txt+'</option>');

    }
  });

  html += '</select>';

  widget.append(html);

}
