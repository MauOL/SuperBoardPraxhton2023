/**
 * Functiones correspondientes al perfil de consultor del aplicativo
 */
function showBonusList(){
    var idConsultor = $("#idConsultor").val();
    $.ajax({
        type: "GET",
        url: "/bonusList",
        data: {
            "idConsultor": idConsultor
        },
        success: function (response) {
            $("#divScripts").html("");
            $("#divScripts").html(response);
        },
        error: function (response){
            console.log("Error ajax: " + response);
        }
    });
}

function showTaskList(){
    var idConsultor = $("#idConsultor").val();
    // El parametro tipoRequest se debe remover en versiones posteriores y manejar 
    // desde la capa de autenticacion y manejo de perfiles.
    // Ya que ese parametro actualmente permite controlar si la lista 
    // de tareas o actividades es actualizable. 
    // Dicha funcionalidad es propia del perfil admin.
    $.ajax({
        type: "GET",
        url: "/taskList",
        data: {
            "idConsultor": idConsultor,
            "tipoRequest": "01"
        },
        success: function (response) {
            $("#divProfileContent").html("");
            $("#divProfileContent").html(response);
        },
        error: function (response){
            console.log("Error ajax: " + response);
        }
    });
}

function showAdvancePanel(nombreFoto){
    var idConsultor = $("#idConsultor").val();
    $.ajax({
        type: "GET",
        url: "/advancePanel",
        data: {
            "idConsultor": idConsultor,
            "nombreFoto": nombreFoto
        },
        success: function (response) {
            $("#divProfileContent").html("");
            $("#divProfileContent").html(response);
        },
        error: function (response){
            console.log("Error ajax: " + response);
        }
    });
}

function consultAdvance(idContainer, nombreFoto){
    var idConsultor = $("#idConsultor").val();
    $.ajax({
        type: "GET",
        url: "/consultAdvance",
        data: {
            "idConsultor": idConsultor,
            "fechaInicial": $("#fechaInicial").val(),
            "fechaFinal": $("#fechaFinal").val(),
            "nombreFoto": nombreFoto
        },
        success: function (response) {
            $("#" + idContainer).html("");
            $("#" + idContainer).html(response);
        },
        error: function (response){
            console.log("Error ajax: " + response);
        }
    });
}

function saveAvatarSettings(){
    var cualidades = "";
    $("input[name='cualidad']").each(function(){
        cualidades += $(this).val() + " ";
    });

    var nombreFoto = $("#nombreFoto").val();
    var colorFondo = $("#colorFondo").val();
    if ( (cualidades.length <= 1) || (colorFondo == "") ) { return; }

    console.log("idConsultor: " + $("#idConsultor").val() + 
                " cualidades: " + cualidades + 
                " nombreFoto: " + nombreFoto + 
                " colorFondo: " + colorFondo);

    $.ajax({
        type: "POST",
        url: "/storeAvatarSettings/",
        data: {
            "idConsultor": $("#idConsultor").val(),
            "cualidades": cualidades,
            "nombreFoto": nombreFoto,
            "colorFondo": colorFondo
        },
        success: function (response) {
            $("#modEditAvatar").modal("hide");
            location.href = "http://localhost:8000/profile";
        },
        error: function (response){
            alert("Error ajax: " + response);
            $("#modEditAvatar").modal("hide");
        }
    });
}