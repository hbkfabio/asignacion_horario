
//FIXME the document ready
$(document).ready(function() {
    $('#dataTables-example').DataTable({
          responsive: true,
          "order": []

    });

    //make status editable
    // $(".accion").editable({
    //     type: 'select',
    //     title: 'Select status',
    //     placement: 'bottom',
    //     emptytext: '',


    //     source: [
    //         {value: "C", text: 'C'},
    //         {value: "A", text: 'A'},
    //         {value: "L", text: 'L'},
    //         {value: "S", text: 'S'},
    //     ]
    //  });



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


$(document).on("click", ".save-addother", function(event){

    alert("hola");
     var pathname = window.location.pathname;
    // var id = $(this).val();
    window.location.href = pathname+"add/";
});



// function change_to_select_item(item){

//   html ='<select class="custom-select accion1">';
//   html += '<option value=""> </option>';
//   html += '<option value="C" selected>C</option>';
//   html += '<option value="A">A</option>';
//   html += '<option value="L">L</option>';
//   html += '<option value="S">S</option>';
//   html += '</select>';
//   cell = item;
  // item.attr('class', 'Nuevo');

  // item.remove();
//   cell.html(html);


// }


// function popover_horario(cell){


//     a = $("#myModal").modal();

//     a.on('hide.bs.modal', function(){
//       c = $(".tipo-clase").val();
//       console.log(c);
// 		  cell.text(c);
// 		  console.log(cell);
// 		  a.remove();
// 		  save_horario(cell);

// 	});
// };


// function save_horario(cell){

//   var val = cell.text();
//   var row = cell.closest("tr").children('td');
//   var dia_semana = cell.closest('table').attr('id');
//   var dic = {};

//   dic["dia_semana"] = dia_semana;
//   row.each(function(){
//     dic[$(this).attr("class")] = $(this).text().trim();
//   })

//   dic = JSON.stringify(dic);

//   console.log(dic);

//   var parametros = {"diccionario":dic,
//                     "valor":val}


//      $.ajax({
//          type: "POST",
//          url: "/horario/save/",
//          data: parametros,
//          async: false,
//         })
//         .done(function( data ){
//           console.log(data);
//           if (data.slice(0, 100).length > 1){
//             alert(data.slice(0, 300));
//               cell.css("background-color", "red");
//               var myBackup = $('#myModal').clone();
//               var myClone = myBackup.clone();
//               $('body').append(myClone);
//               popover_horario(cell);
//           }else{
//             cell.css("background-color", "");
//           }
//         });

// }



$(document).on("click", ".accion", function(event){


  // popover_horario();

  // var myBackup = $('#myModal').clone();
  var cell = $(this);
  // popover_horario(cell);

  // var myClone = myBackup.clone();
  // $('body').append(myClone);

  // change_to_select_item(cell);

  var val = $(this).text();
  if (val == "X"){
    return false
  }
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
            alert(data.slice(0, 300));
              cell.css("background-color", "red");
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


