$(document).ready(function() {

  //FIXME
  idTable = [$('#1'), $('#2'), $('#3'), $('#4'), $('#5')]

  $.each(idTable, function(index, value){
    var table = value;

    a = index+1;
    var semestre = '.semestre-header-'+a;
    var modulo = '.modulo-header-'+a;

    // $('#facility_header, #city_header')
    $(modulo + ', ' + semestre)
      .wrapInner('<span title="sort this column"/>')
      .each(function(){

        var th = $(this),
            thIndex = th.index(),
            inverse = false;

        th.click(function(){
            table.find('td').filter(function(){
                  return $(this).index() === thIndex;
              }).sortElements(function(a, b){
                  return $.text([a]) > $.text([b]) ?
                      inverse ? -1 : 1
                      : inverse ? 1 : -1;

              }, function(){

                  // parentNode is the element we want to move
                  return this.parentNode;

              });

              inverse = !inverse;

          });
      });

  });

  //cargo datos de periodo en select <periodo>
  var periodo = $("#periodo")
  var codigo = getUrlParameter("periodo");
  get_data_model(periodo, codigo);
  //cargo datos de carrera en select <carrera>
  var carrera = $("#carrera");
  var codigo = getUrlParameter("carrera");
  get_data_model(carrera, codigo);


});

var getUrlParameter = function getUrlParameter(sParam) {
    var sPageURL = decodeURIComponent(window.location.search.substring(1)),
        sURLVariables = sPageURL.split('&'),
        sParameterName,
        i;

    for (i = 0; i < sURLVariables.length; i++) {
        sParameterName = sURLVariables[i].split('=');

        if (sParameterName[0] === sParam) {
            return sParameterName[1] === undefined ? true : sParameterName[1];
        }
    }
};


function load_select_data(widget, data, value){

  var name = widget.attr("name");
  var txt = `Seleccione un(a) ${name}`;

  $(widget).append(
      $('<option></option>').val("").html(txt)
    );

  $.each(data, function(i, val){
    pk = val["pk"]
    txt = val["fields"]["nombre"]

    if (value == pk){

      $(widget).append(
        $('<option selected></option>').val(pk).html(txt)
      )

    }else{

      $(widget).append(
        $('<option></option>').val(pk).html(txt)
      )

    }

  });

  return false;

}

function get_data_model(widget, value){

  var diccionario = {'codigo' : value}
  var name = widget.attr("name");

  if (name == null){

        return false;

  }

  var url = `/horario/param/get_${name}/`;


  $.ajax({
         type: "POST",
         url: url,
         data: diccionario,
         async: false,
        })
        .done(function(data){
          data = $.parseJSON(data);
          load_select_data(widget, data, value)
        });

}



$(document).on("click", ".edit-listado-horario", function(event){

 event.preventDefault();

  var pathname = window.location.pathname;
  var file = $(this).parents("tr");

  var carrera = file.find("td:eq(0)");
  carrera = carrera.attr("name");

  var periodo = file.find("td:eq(2)");
  periodo = periodo.attr("name");

  pathname +="edit/?periodo="+periodo;
  pathname +="&carrera="+carrera;

  window.location.href = pathname;

  event.stopPropagation();

});


$(document).on("change", "#carrera", function(event){

  event.preventDefault();

  var carrera = $(this).val();
  var periodo = $("#periodo").val();
  if (periodo == ""){

    url ="?carrera="+carrera;

  }else{

    var url = "?periodo="+periodo+"&carrera="+carrera

  }

  window.location.href = url;

  event.stopPropagation();

});


$(document).on("change", "#periodo", function(event){

  event.preventDefault();

  var periodo = $(this).val();
  var carrera = $("#carrera").val();

  if (periodo==""){

    return false;

  }

  if (carrera == ""){

    url ="?periodo="+periodo;

  }else{

    var url = "?periodo="+periodo+"&carrera="+carrera

  }

  window.location.href = url;

  event.stopPropagation();

});

