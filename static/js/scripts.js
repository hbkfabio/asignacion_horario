$(document).on("click", ".edit", function(event){

    var pathname = window.location.pathname;
    var id = $(this).val();
    window.location.href = pathname+"edit/"+id;
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


$(document).on("click", ".actividades", function(event){

  var val = $(this).text();

  console.log(val);

  if (val == ""){
    $(this).text("C");
  }else if(val == "C"){
    $(this).text("A");
  }else if(val == "A"){
    $(this).text("L");
  }else if( val == "L"){
    $(this).text("");
  }


});
