$(document).ready(function(){

    periodo = $("select[name = 'periodo']");

    if (periodo.val() == ""){
        disable_all();
    }

});


function disable_all(){
    //Se deshabilitan todos los widget menos periodo.
    w = [
        carrera = $("select[name = 'carrera']"),
        plan = $("select[name = 'plan']"),
        //periodo = $("select[name = 'periodo']"),
        profesor = $("select[name = 'profesor']"),
        modulo = $("select[name = 'modulo']"),
    ]

    $.each(w, function(i){

        w[i].attr("disabled", true);
        w[i].val("");
    });

}

function load_select_data(widget, data){

    var name = widget.attr("name");
    name = name.split("-")[0];
    var txt = `Seleccione un(a) ${name}`;

    $(widget).append(
        $('<option></option>').val("").html(txt)
    );

    $.each(data, function(i, val){
        pk = val["pk"]
        txt = val["fields"]["nombre"]

        $(widget).append(
            $('<option></option>').val(pk).html(txt)
        )
    });


}

function get_data_model(widget, value){

    //Se agrega var periodo necesaria para GetModulo
    var periodo = $("select[name = 'periodo']").val();
    var diccionario = {"codigo" : value,
        "periodo":periodo,
    }

    var name = widget.attr("name");
    var url = `/horario/param/get_${name}/`;


    $.ajax({
        type: "POST",
        url: url,
        data: diccionario,
        async: false,
    })
        .done(function(data){
            data = $.parseJSON(data);
            load_select_data(widget, data)
        });

}


function disable_widget(widget, value){

    if (value != ""){

        widget.attr("disabled", false);
        widget.find('option').remove()
        get_data_model(widget, value)

    } else {

        widget.attr("disabled", true);
        widget.val("")

    }
}


$(document).on("change", "select[name = 'periodo']", function(event){

    event.preventDefault();

    //var widget = $("select[name = 'periodo']");
    var value = $(this).val();
    //disable_widget(widget, value);

    //var widget = $("select[name = 'profesor']");
    //disable_widget(widget, value);

    var widget = $("select[name = 'carrera']");
    disable_widget(widget, value);

    event.stopPropagation();

});

$(document).on("change", "select[name = 'carrera']", function(event){

    event.preventDefault();

    var carrera = $(this);

    value = carrera.val()

    if (value == ""){

        // disable_all();
        var widget = $("select[name = 'modulo']");
        disable_widget(widget, value);

        var widget = $("select[name = 'profesor']");
        disable_widget(widget, value);

        var widget = $("select[name = 'plan']");
        disable_widget(widget, value);

    } else {

        var widget = $("select[name = 'plan']");
        disable_widget(widget, value);

    }

    event.stopPropagation();

});


$(document).on("change", "select[name = 'plan']", function(event){

    event.preventDefault();

    var value = $(this).val();

    var widget = $("select[name = 'modulo']");
    disable_widget(widget, value);

    event.stopPropagation();

});


$(document).on("change", "select[name = 'modulo']", function(event){

    event.preventDefault();

    var value = $(this).val();

    var param = {"modulo": value}

    var url = `/horario/param/get_modulo_espejo_cursos_grupo/`;

    $.ajax({
        type: "POST",
        dataType: "json",
        url: url,
        data: param,
    })
        .done(function(data){
            if (!data.success){
                alert(data.msj);
                $("#table-cursos-grupo tbody tr").remove()
                $("#table-cursos-grupo").append(data.table);
            }

        });

    var widget = $("select[name = 'profesor']");
    disable_widget(widget, value);

    event.stopPropagation();

});


function valida_existe_ppm(){

    var periodo = $("select[name = 'periodo']");
    var carrera = $("select[name = 'carrera']");
    var plan = $("select[name = 'plan']");
    var modulo = $("select[name = 'modulo']");
    var profesor = $("select[name = 'profesor']");

    var param = {"periodo": periodo.val(),
        "carrera": carrera.val(),
        "plan": plan.val(),
        "modulo": modulo.val(),
        "profesor": profesor.val(),
    }

    var url = `/horario/horario/get_valida_ppm/`;

    $.ajax({
        type: "POST",
        dataType: "json",
        url: url,
        data: param,
    })
        .done(function(data){
            if (!data.success){
                alert(data.msj);
                profesor.val("");
            }

        });

}

$(document).on("change", "select[name = 'profesor']", function(event){

    event.preventDefault();

    deleteHorarioTemp();
    valida_existe_ppm();

    //$(".reset-horario").trigger("click");

    event.stopPropagation();

});



function deleteHorarioTemp(){

    var carrera = $("select[name = 'carrera']");
    var modulo = $("select[name = 'modulo']");
    var profesor = $("select[name = 'profesor']");

    var param = {"carrera": carrera.val(),
        "modulo": modulo.val(),
        "profesor": profesor.val(),
    }

    var url = `/horario/horario/delete_horario_temp/`;

    $.ajax({
        type: "POST",
        dataType: "json",
        url: url,
        data: param,
    })
        .done(function(data){

        });

}

$(document).on("click", ".reset-horario", function(event){


    deleteHorarioTemp();


});


$(document).on("change", "#id_compartido", function(event){

    console.log("click");

});
