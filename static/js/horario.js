$(document).ready(function(){


  periodo = $("select[name = 'periodo']");

  if (periodo.val() == ""){
    disable_all();
  }


});


function disable_all(){
  //Se deshabilitan todos los widget menos periodo.

    w = [
    carrera = $("select[name = 'carrera']"),
    plan = $("select[name = 'plan']"),
    //periodo = $("select[name = 'periodo']"),
    profesor = $("select[name = 'profesor']"),
    modulo = $("select[name = 'modulo']"),
    ]

    $.each(w, function(i){

      w[i].attr("disabled", true);
      w[i].val("");
    });

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
         async: false,
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
    widget.val("")

  }
}


$(document).on("change", "select[name = 'periodo']", function(event){

  event.preventDefault();

  //var widget = $("select[name = 'periodo']");
  var value = $(this).val();
  //disable_widget(widget, value);

  //var widget = $("select[name = 'profesor']");
  //disable_widget(widget, value);

  var widget = $("select[name = 'carrera']");
  disable_widget(widget, value);

   event.stopPropagation();

});

$(document).on("change", "select[name = 'carrera']", function(event){

  event.preventDefault();

  var carrera = $(this);
  console.log(carrera.val());

  value = carrera.val()

  if (value == ""){

     // disable_all();
    var widget = $("select[name = 'modulo']");
    disable_widget(widget, value);

    var widget = $("select[name = 'profesor']");
    disable_widget(widget, value);

    var widget = $("select[name = 'plan']");
    disable_widget(widget, value);

  } else {

    var widget = $("select[name = 'plan']");
    disable_widget(widget, value);

  }

  event.stopPropagation();

});


$(document).on("change", "select[name = 'plan']", function(event){

  event.preventDefault();

  var value = $(this).val();

  var widget = $("select[name = 'modulo']");
  disable_widget(widget, value);

  var widget = $("select[name = 'profesor']");
  disable_widget(widget, value);

  event.stopPropagation();

});
