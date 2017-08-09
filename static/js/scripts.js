//FIXME the document ready
$(document).ready(function() {
    $('#dataTables-example').DataTable({
          responsive: true,
          "order": []

    });

  $('form:not(.filter) :input:visible:enabled:first').focus()

  $('.input-sm').focus();

});


$(document).on("click", ".edit", function(event){

  event.preventDefault();

  var pathname = window.location.pathname;
  var id = $(this).val();
  window.location.href = pathname+"edit/"+id;

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

