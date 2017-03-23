$(document).ready(function(){


  carrera = $("select[name = 'carrera']");
  if (carrera.val() == ""){
    disable_all();
  }

});


function disable_all(){

    plan = $("select[name = 'plan']");
    periodo = $("select[name = 'periodo']");
    profesor = $("select[name = 'profesor']");
    modulo = $("select[name = 'modulo']");

    plan.attr("disabled", true);
    periodo.attr("disabled", true);
    profesor.attr("disabled", true);
    modulo.attr("disabled", true);

}

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


$(document).on("change", "select[name = 'carrera']", function(event){

  var carrera = $(this);
  console.log(carrera.val());

  if (carrera.val() == ""){

    disable_all();

  } else {
    var widget = $("select[name = 'plan']");
    var value = $(this).val();

    disable_widget(widget, value);
  }
});


$(document).on("change", "select[name = 'plan']", function(event){
  var widget = $("select[name = 'periodo']");
  var value = $(this).val();
  disable_widget(widget, value);

  var widget = $("select[name = 'profesor']");
  disable_widget(widget, value);

  var widget = $("select[name = 'modulo']");
  disable_widget(widget, value);

});
