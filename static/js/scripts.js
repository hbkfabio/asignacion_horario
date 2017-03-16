
//FIXME the document ready
$(document).ready(function() {
    $('#dataTables-example').DataTable({
          responsive: true,
          "order": []

    });


  $('.input-sm').focus();

    var pathname = window.location.href.split("=")[1];
    // console.log(pathname);
    $("#periodo").val(pathname);
});


$(document).on("click", ".edit", function(event){

    var pathname = window.location.pathname;
    var id = $(this).val();
    window.location.href = pathname+"edit/"+id;
});


$(document).on("click", ".edit-listado-horario", function(event){

    var pathname = window.location.pathname;
    var id = $(this).val();
    window.location.href = pathname+"edit/?periodo="+id;
});


$(document).on("click", ".confirm-delete", function(event){

  var pathname = window.location.pathname.split("/")[1];
  window.location.href = "/"+pathname+"/";
});


$(document).on("click", ".delete", function(event){

    var pathname = window.location.pathname;
    var id = $(this).val();
    window.location.href = pathname+id+"/delete/";
});


$(document).on("click", ".add", function(event){

    var pathname = window.location.pathname;
    var id = $(this).val();
    window.location.href = pathname+"add/";
});


$(document).on("click", "button[type='reset']", function(){

    var pathname = window.location.pathname.split("/")[1];
    pathname="/"+pathname+"/";
    window.location.href =pathname;
});


function change_to_select_item(item){

  html ='<select class="combo-option">';
  html += '<option value=""> </option>';
  html += '<option value="C">C</option>';
  html += '<option value="A">A</option>';
  html += '<option value="L">L</option>';
  html += '<option value="S">S</option>';
  html += '</select>';
  return html;
}


$(document).on("change", ".combo-option", function(event){

  var combo = $(this);
  var valor = combo.val();

  console.log(combo);

  td = $(this).parent();
  td.html(valor);
  td.attr('class', 'accion');

  titulo_bloque = td.closest('table').find('th').eq(td.index());
  console.log(titulo_bloque.text());

});


$(document).on("click", ".accion", function(event){

  var item = $(this);
  var valor = item.text();

  if (valor != "X"){
    //creo el combo
    combo = change_to_select_item(item);
    item.attr('class', '');
    item.html(combo);
    //manipulo el combo creado en la celda de la tabla
    combo = item.children();
    combo.val(valor);
  }


  return false;

  var cell = $(this);

  var val = $(this).text();
  // if (val == "X"){
  //   return false
  // }

  var row = $(this).closest("tr").children('td');
  var dia_semana = $(this).closest('table').attr('id');
  var dic = {};

  var titulo_bloque = cell.closest('table').find('th').eq(cell.index());

  if (val == ""){
    $(this).text("C");
  }else if(val == "C"){
    $(this).text("A");
  }else if(val == "A"){
    $(this).text("S");
  }else if(val == "S"){
    $(this).text("L");
  }else if( val == "L"){
    $(this).text("T");
  }else if(val=="T"){
    $(this).text("");
  }

  val = $(this).text();
  dic["dia_semana"] = dia_semana;
  dic["titulo_bloque"] = titulo_bloque.text();
  row.each(function(){
    dic[$(this).attr("class")] = $(this).text().trim();
  })

  dic = JSON.stringify(dic);

  // console.log(dic);

  var parametros = {"diccionario":dic,
                    "valor":val,
                    }

     $.ajax({
         type: "POST",
         url: "/horario/save/",
         data: parametros,
         async: false,
        })
        .done(function( data ){
          console.log(data);
          if (data.slice(0, 100).length > 1){
            if (data.length ==55){
              cell.text("");
            }
            cell.css("background-color", "red");
            alert(data.slice(0, 300));
            cell.css("background-color", "");
          }else{
            cell.css("background-color", "");
          }

        });

});


$(document).on("change", "#periodo", function(event){

    var combo = $(this).find('option:selected').val();
    var pathname = window.location.pathname;
    window.location.href = pathname + "?periodo="+combo;

});
