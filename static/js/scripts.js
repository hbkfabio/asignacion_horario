//FIXME the document ready
$(document).ready(function() {
    $('#dataTables-example').DataTable({
          responsive: true,
          "order": []

    });

  $('form:not(.filter) :input:visible:enabled:first').focus()

  $('.input-sm').focus();

  // var pathname = window.location.href.split("?");

  // if (pathname.length >= 1){

  //   pathname = pathname.pop();
  //   console.log(pathname);

  //   pathname = pathname.split("&");
  //   console.log(pathname);

  //   $.each(pathname, function(i, j){
  //     temp = j.split("=");
  //     $("#"+temp[0]).val(temp[1]);
  //     console.log(temp[0]);
  //     console.log(temp[1]);
  //   });

  // }


  //$("#periodo").val(pathname);
  //$("#carrera").val(pathname);

});


$(document).on("click", ".edit", function(event){

  event.preventDefault();

  var pathname = window.location.pathname;
  var id = $(this).val();
  window.location.href = pathname+"edit/"+id;

  event.stopPropagation();

});


$(document).on("click", ".edit-listado-horario", function(event){

  event.preventDefault();
  var pathname = window.location.pathname;
  var id = $(this).val();
  window.location.href = pathname+"edit/?periodo="+id;

  event.stopPropagation();

});


$(document).on("click", ".confirm-delete", function(event){

  event.preventDefault();

  var pathname = window.location.pathname.split("/")[1];
  window.location.href = "/"+pathname+"/";

  event.stopPropagation();

});


$(document).on("click", ".delete", function(event){

  event.preventDefault();
  var pathname = window.location.pathname;
  var id = $(this).val();
  window.location.href = pathname+id+"/delete/";

  event.stopPropagation();

});


$(document).on("click", ".add", function(event){

  event.preventDefault();

  var pathname = window.location.pathname;
  var id = $(this).val();
  window.location.href = pathname+"add/";

  event.stopPropagation();

});


$(document).on("click", ".reset", function(event){

   event.preventDefault();

   var pathname = window.location.pathname.split("/")[1];
   pathname="/"+pathname+"/";
   window.location.href =pathname;

   event.stopPropagation();

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





// $(document).on("click", ".accion", function(event){

//   event.preventDefault();

//   var item = $(this);
//   var valor = item.text();

//   if (valor != "X"){
    //creo el combo
//     combo = change_to_select_item(item);
//     item.attr('class', '');
//     item.html(combo);
    //manipulo el combo creado en la celda de la tabla
//     combo = item.children();
//     combo.val(valor);
//   }


//   event.stopPropagation();
//   return false;

//   var cell = $(this);

//   var val = $(this).text();
  // if (val == "X"){
  //   return false
  // }

//   var row = $(this).closest("tr").children('td');
//   var dia_semana = $(this).closest('table').attr('id');
//   var dic = {};

//   var titulo_bloque = cell.closest('table').find('th').eq(cell.index());

//   if (val == ""){
//     $(this).text("C");
//   }else if(val == "C"){
//     $(this).text("A");
//   }else if(val == "A"){
//     $(this).text("S");
//   }else if(val == "S"){
//     $(this).text("L");
//   }else if( val == "L"){
//     $(this).text("T");
//   }else if(val=="T"){
//     $(this).text("");
//   }

//   val = $(this).text();
//   dic["dia_semana"] = dia_semana;
//   dic["titulo_bloque"] = titulo_bloque.text();
//   row.each(function(){
//     dic[$(this).attr("class")] = $(this).text().trim();
//   })

//   dic = JSON.stringify(dic);

  // console.log(dic);

//   var parametros = {"diccionario":dic,
//                     "valor":val,
//                     }

//      $.ajax({
//          type: "POST",
//          url: "/horario/save/",
//          data: parametros,
//          async: false,
//         })
//         .done(function( data ){
//           console.log(data);
//           if (data.slice(0, 100).length > 1){
//             if (data.length ==55){
//               cell.text("");
//             }
//             cell.css("background-color", "red");
//             alert(data.slice(0, 300));
//             cell.css("background-color", "");
//           }else{
//             cell.css("background-color", "");
//           }

//         });

// });
