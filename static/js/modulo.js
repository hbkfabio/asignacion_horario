$(document).ready(function(){

  disable_all(true);

});


function disable_all(value){

    w = [
    plan = $("select[name = 'plan']"),
    modulo = $("input[name = 'nombre']"),
    semestre = $("select[name = 'semestre']"),
    horas_clase = $("input[name = 'horas_clase']"),
    horas_seminario = $("input[name = 'horas_seminario']"),
    horas_laboratorio = $("input[name = 'horas_laboratorio']"),
    horas_taller = $("input[name = 'horas_taller']"),
    horas_ayudantia = $("input[name = 'horas_ayudantia']"),

    ];

    $.each(w, function(i){
      w[i].attr("disabled", value);
    });


}


$(document).on("change", "select[name = 'carrera']", function(event){

  widget = $(this);

  if (widget.val() != ""){

    disable_all(false);

  }


})
