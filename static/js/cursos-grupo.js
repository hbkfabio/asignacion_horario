$(document).ready(function(){

  carrera = $("select[name = 'carrera-cg']");
  get_data_model(carrera, null);

});

$(document).on("click", ".expand-cursos-grupo", function(event){

  $(this).find('span').toggleClass('glyphicon-collapse-up').toggleClass('glyphicon-collapse-down');

});


$(document).on("click", ".add-cursos-grupo", function(event){

  event.preventDefault();
  
  add_row();  
  
  event.stopPropagation();

});

function add_row(){

 var row=$("<tr>"+
        "<td></td>"+
        "<td></td>"+
        "<td></td>"+
        "<td width=10%>"+
          "<center>"+
          "<button class='btn btn-primary btn-sm add-cursos-grupo'>"+
          "<span class='glyphicon glyphicon-plus'></span></button>"+
          "</center>"+
        "</td>"+
        "<td width=10%>"+
          "<center>"+
          "<button class='btn btn-danger btn-sm delete-cursos-grupo'>"+
          "<span class='glyphicon glyphicon-minus'></span></button>"+
          "</center>"+
        "</td>"+
        "</tr>");
  $('#table-cursos-grupo > tbody:last-child').append(row);

}


$(document).on("click", ".delete-cursos-grupo", function(event){

  event.preventDefault();
  
  var tr = $(this).closest('tr');
  tr.css("background-color","#FF3700");
  tr.fadeOut(300, function(){
    tr.remove();
    var rowCount = $('#table-cursos-grupo tr').length;
    console.log(rowCount);
    if(rowCount == 1){
      add_row();
    }
  });
  
  event.stopPropagation();

})
