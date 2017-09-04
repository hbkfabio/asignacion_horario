function create_select_item(widget, url, param){

    $.ajax({
        type: "POST",
        dataType: "json",
        url: url,
        data: param,
        async: false,
    })
    .done(function(data){
        select_item_to_html(widget, data);
    });

}

function select_item_to_html(widget, data){

    widget.append("<option value=''></option>");
    $.each(JSON.parse(data), function(i, val){
        pk = val["pk"];
        txt = val["fields"]["nombre"];
        $(widget).append(
            $('<option></option>').val(pk).html(txt)
        )
    });
}


function disable_widget(widget){

    $.each(widget, function(i){

        widget[i].attr("disabled", true);
        widget[i].val("");
    });

}

function enable_widget(widget){

    $.each(widget, function(i){

        widget[i].attr("disabled", false);
        widget[i].val("");
    });

}


function add_row_table(table, select_item){

    var rowCount = $(table).find("tr").length;
    var td = "";
    // var row = "<tr>";
    $.each(select_item, function(i){
        td += `<td width=30%><select class='form-control' name=${select_item[i]}></td>`
    })

    td +=("<td width=10%>"+
        "<center>"+
        "<button class='btn btn-danger btn-sm delete-table-grupo'>"+
        "<span class='glyphicon glyphicon-minus'></span></button>"+
        "</center>"+
        "</td>"
    );
    row =$("<tr>" + td + "</tr>");
    $(table).find('tbody:last-child').append(row);

    return row;

}


function save_form(url, param, another){

    console.log(param);

    $.ajax({
        type: "POST",
        dataType: "json",
        url: url,
        data: param,
        async: false,
    })
    .done(function(data){

    });


}
