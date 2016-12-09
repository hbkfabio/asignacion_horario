$(document).on("click", ".edit", function(event){

    var title = $(this).closest("tr").find("th").text();
    var pathname = window.location.pathname;
    console.log(pathname+title);
    window.location.href = pathname+title;

});

$(document).on("click", "button[type='reset']", function(){
    var pathname = window.location.pathname.split("/")[1];
    console.log(pathname);
    pathname="/"+pathname+"/";
    window.location.href =pathname;

});
