$(document).ready(function(){

  var rowCount = $('#table-cursos-grupo tr').length;
  if(rowCount == 1){
    add_row();
  }

});

$(document).on("click", ".expand-cursos-grupo", function(event){

  event.preventDefault();

  $(this).find('span').toggleClass('glyphicon-collapse-up').toggleClass('glyphicon-collapse-down');

  var rowCount = $('#table-cursos-grupo tr').length;
  if(rowCount == 1){
    add_row();
  }

  event.stopPropagation();

});


$(document).on("click", ".add-cursos-grupo", function(event){

  event.preventDefault();
  
  add_row();  
  
  event.stopPropagation();

});

function add_row(){

 var row=$("<tr>"+
        "<td width=30%><select class='form-control' name='carrera-cg'></select></td>"+
        "<td width=30%><select class='form-control' name='plan-cg'></select></td>"+
        "<td width=30%><select class='form-control' name='modulo-cg'></td>"+
        "<td width=10%>"+
          "<center>"+
          "<button class='btn btn-danger btn-sm delete-cursos-grupo'>"+
          "<span class='glyphicon glyphicon-minus'></span></button>"+
          "</center>"+
        "</td>"+
        "</tr>");
  $('#table-cursos-grupo > tbody:last-child').append(row);

  carrera = row.find("[name=carrera-cg]");
  get_data_model(carrera, null);

  plan = row.find("[name=plan-cg]");
  plan.attr("disabled", true);

  modulo = row.find("[name=modulo-cg]");
  modulo.attr("disabled", true);

}

$(document).on("change", "select[name=carrera-cg]", function(event){

  event.preventDefault();

  var carrera = $(this);
  var value = carrera.val();

  var plan = carrera.parent().parent().find("select[name=plan-cg]");
  disable_widget(plan, value);

  event.stopPropagation();

});


$(document).on("change", "select[name=plan-cg]", function(event){

  event.preventDefault();

  var plan = $(this);
  var value = plan.val();

  var modulo = carrera.parent().parent().find("select[name=modulo-cg]");
  disable_widget(modulo, value);

  event.stopPropagation();

})

$(document).on("click", ".delete-cursos-grupo", function(event){

  event.preventDefault();

  var tr = $(this).closest('tr');
  tr.css("background-color","#FF3700");
  tr.fadeOut(300, function(){
    tr.remove();
    var rowCount = $('#table-cursos-grupo tr').length;
    if(rowCount == 1){
      add_row();
    }
  });

  event.stopPropagation();

})
