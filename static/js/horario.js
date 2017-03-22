$(document).ready(function(){

  $(".get_plan").attr("disabled", true);
  $(".get_periodo").attr("disabled", true);
  $(".get_profesor").attr("disabled", true);
  $(".get_modulo").attr("disabled", true);

});


function load_select_data(widget, data){

  var name = widget.attr("name");
  var txt = `Seleccione un(a)  ${name}`;

  $(widget).append(
      $('<option></option>').val("").html(txt)
    );

  $.each(data, function(i, val){
    pk = val["pk"]
    txt = val["fields"]["nombre"]

    $(widget).append(
      $('<option></option>').val(pk).html(txt)
    )
    });


}

function get_data_model(widget, value){

  var diccionario = {'codigo' : value}

  var name = widget.attr("name");
  var url = `/horario/param/get_${name}/`;


  $.ajax({
         type: "POST",
         url: url,
         data: diccionario,
         //async: false,
        })
        .done(function(data){
          data = $.parseJSON(data);
          load_select_data(widget, data)
        });

}


function disable_widget(widget, value){

  if (value != ""){
    widget.attr("disabled", false);
    widget.find('option').remove()
    get_data_model(widget, value)
  } else {
    widget.attr("disabled", true);
  }
}


$(document).on("change", ".get_carrera", function(event){

  var widget = $(".get_plan");
  var value = $(this).val();

  disable_widget(widget, value);

});


$(document).on("change", ".get_plan", function(event){

  var widget = $(".get_periodo");
  var value = $(this).val();

  disable_widget(widget, value);

});


$(document).on("change", ".get_periodo", function(event){

  var widget = $(".get_profesor");
  var value = $(this).val();

  disable_widget(widget, value);

});


$(document).on("change", ".get_modulo", function(event){

  var widget = $(".get_modulo");
  var value = $(this).val();

  disable_widget(widget, value);

});


$(document).on("change", ".get_modulo", function(event){

  var widget = $(".get_modulo");
  var value = $(this).val();

  disable_widget(widget, value);

});

