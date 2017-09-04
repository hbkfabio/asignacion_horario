$(document).ready(function(){

    var carrera = $("#carrera");
    var url = "/horario/param/get_carrera/";
    var param = {}

    create_select_item(carrera, url, param);
    var w = [$("#plan"), $("#modulo")];
    disable_widget(w);

    var tabla = $("#tabla-modulos-espejo");
    var item =["plan-me", "modulo-me"];
    add_row_table(tabla, item);
    modulo = $("[name=modulo-me]");
    plan = $("[name=plan-me]");
    widget = [modulo, plan]
    disable_widget(widget);


    var pathname = window.location.pathname.split("/")[3];

    if (pathname != ""){
        load_data(pathname);
    }

});


function load_data(pathname){

    var url = "/param/get_data_moduloespejo/";
    param = {"codigo": pathname};

    $.ajax({
        type: "POST",
        dataType: "json",
        url: url,
        data: param,
        async: false,
    })
        .done(function(data){
            if (data.success){
                $("#carrera").val(data.carrera);
                action_carrera();

                $("#plan").val(data.plan);
                action_plan();

                $("#modulo").val(data.modulo);
                action_modulo();
            }
        });


    // action_carrera();

}

function action_carrera(){

    var plan = $("#plan");
    var modulo = $("#modulo");
    var carrera = $("#carrera").val();

    if (carrera == ""){
     widget = [plan, modulo];
     disable_widget(widget);
     return false;

    }

    var url = "/horario/param/get_plan/";

    var param = {"codigo":carrera};

    plan.empty();
    widget = [plan];
    enable_widget(widget);

    create_select_item(plan, url, param);


}

$(document).on("change", "#carrera", function(event){

    event.stopPropagation();
    event.preventDefault();

    action_carrera();

})


function action_plan(){

    var modulo = $("#modulo");
    var plan = $("#plan").val();
    if (plan == ""){

        widget = [modulo];
        disable_widget(widget);
        return false;

    }

    var url = "/horario/param/get_modulo/";
    var param = {"codigo": plan};

    modulo.empty();
    widget = [modulo];
    enable_widget(widget);

    create_select_item(modulo, url, param);

}

$(document).on("change", "#plan", function(event){

    event.stopPropagation();
    event.preventDefault();

    action_plan();

})


function action_modulo(){

    plan = $("[name=plan-me]");
    widget = [plan];
    enable_widget(widget);

    var table = $("#tabla-modulos-espejo");
    var rowCount = $(table).find("tr").length;

    if (rowCount == 2){
        url = "/horario/param/get_plan/";
        param = {"codigo":$("#carrera").val()};
        plan.empty();
        create_select_item(plan, url, param);
    }

}

$(document).on("change", "#modulo", function(event){

    event.stopPropagation();
    event.preventDefault();

    action_modulo();

})

$(document).on("click", "#add-item", function(event){

    carrera = $("#carrera")
    if (carrera.val() == ""){
        alert ("Seleccione una carrera");
        return false
    }

    var tabla = $("#tabla-modulos-espejo");
    var item =["plan-me", "modulo-me"];
    row = add_row_table(tabla, item);

    plan = row.find("[name=plan-me]");
    plan.empty();
    param = {"codigo": carrera.val()};
    url = "/horario/param/get_plan/";

    create_select_item(plan, url, param)

    modulo = row.find("[name=modulo-me]");
    widget = [modulo];
    disable_widget(widget);

})

$(document).on("change", "[name=plan-me]", function(event){

    event.stopPropagation();
    event.preventDefault();

    var plan = $(this);
    var modulo = plan.parent().parent().find("[name=modulo-me]");
    modulo.empty();
    widget = [modulo];
    enable_widget(widget);
    url = "/horario/param/get_modulo/";
    param = {"codigo": plan.val()};
    create_select_item(modulo, url, param)

    //remuevo item de modulo de cabecera
    var m = $("#modulo").val()
    $(modulo).find(`option[value=${m}]`).remove();
})


$(document).on("change", "[name=modulo-me]", function(event){

    event.preventDefault();
    event.stopPropagation();

    var parents = $(this).parents().find("[name=modulo-me]");

    $.each(parents, function(i){

        p = $(parents[i]);

    })


})


$(document).on("click", ".delete-table-grupo", function(event){

    event.stopPropagation();
    event.preventDefault();

    var carrera = $("#carrera").val();

    if (carrera == "" ){

        return false;

    }

    row = $(this).parent().parent().parent();
    row.remove();

    var table = $("#tabla-modulos-espejo");
    var rowCount = $(table).find("tr").length;

    if(rowCount == 1){

        $("#add-item").trigger("click");

    }

})


$(document).on("click", "[name=_save]", function(event){

    event.stopPropagation();
    event.preventDefault();

    var url = "/param/save_moduloespejo/";
    var param = [];
    var modulo = $("#modulo").val();
    var carrera = $("#carrera").val();
    var plan = $("#plan").val();

    tabla = $("#tabla-modulos-espejo");

    espejos = tabla.find("[name=modulo-me]");

    // console.log(espejos);
    $.each(espejos, function(i){
        var value = $(this).val();
        if (value != null && value != ""){
            param.push(value);
            console.log(param);
        }
    });

    if (param.length == 0){

        console.log("nada");
        return false;

    }

    dic ={"modulo": modulo,
        "espejo" : param,
    }

    save_form(url, dic, false);

})



