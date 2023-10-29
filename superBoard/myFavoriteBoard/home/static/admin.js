/**
 * Functiones correspondientes al perfil admin del aplicativo
 */
function fillNewActivityModal(){
    var keysVar = $("#consultor").val();
    var name = $("#consultor option:selected").text();
    if ( (typeof keysVar === "undefined") || (keysVar == "00-00") ) { return; }
    keysArray = keysVar.split("-");
    $("#idConsultor").val(keysArray[0]);
    $("#clave, #bonusClave").val(keysArray[1]);
    $("#nombre, #bonusNombre").val(name);
    console.log( "value: " + keysVar + " name: " +  name);
}

function loadTaskBoardForm(){
    $.ajax({
        type: "GET",
        url: "/taskBoardForm",
        success: function (response) {
            $("#divAdminContent").html("");
            $("#divAdminContent").html(response);
        },
        error: function (response){
            console.log("Error ajax: " + response);
        }
    });
}

function loadManyTasksForm() {
    $.ajax({
        type: "GET",
        url: "/manyTaskBoardForm",
        success: function (response) {
            $("#divAdminContent").html("");
            $("#divAdminContent").html(response);
        },
        error: function (response){
            console.log("Error ajax: " + response);
        }
    });
}

function showTaskList(){
    var keysVar = $("#consultor").val();
    if ( (typeof keysVar === "undefined") || (keysVar == "00-00") ) { return; }
    keysArray = keysVar.split("-");
    var idConsultor = keysArray[0];
    
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
            "tipoRequest": "03"
        },
        success: function (response) {
            $("#divTaskList").html("");
            $("#divTaskList").html(response);
        },
        error: function (response){
            console.log("Error ajax: " + response);
        }
    });
}

function saveActivity(){
    $.ajax({
        type: "POST",
        url: "/storeActivity/",
        data: {
            "idConsultor": $("#idConsultor").val(),
            "descrip": $("#actividad").val(),
            "categoria": $("#categoria").val(),
            "proyecto": $("#proyecto").val(),
            "valor": $("#valor").val(),
            "estatus": $("#estatus").val(),
            "notas": $("#notas").val(),
            "fechaAsignacion": $("#fechaAsignacion").val(),
            "fechaEntrega": $("#fechaEntrega").val()
        },
        success: function (response) {
            alert("Actividad Guardada Exitosamente!");
            $("#staticBackdrop").modal("hide");
            showTaskList();
        },
        error: function (response){
            console.log("Error ajax: " + response);
            $("#staticBackdrop").modal("hide");
        }
    });
}

function saveActivityBlock(){
    var lineIds = "";
    var descrip = $("#actividadB").val();
    var proyecto = $("#proyectoB").val();
    var valor = $("#valorB").val();
    var fechaAsignacion = $("#fechaAsignacionB").val();
    var fechaEntrega = $("#fechaEntregaB").val();

    // Validaciones iniciales
    if ( (descrip == "") || (proyecto == "") || (valor == "") ) { 
        return; 
    }
    if ( (fechaAsignacion == "") || (fechaEntrega == "")) { 
        return; 
    }

    // Se procesan los ids seleccionados
    $("input[name='checkForActivity']").each(function(){
        if ( $(this).is(":checked") ) {
            lineIds += $(this).val() + ",";
        }
    });
    
    if (lineIds == ""){ return; }
    lineIds = lineIds.substring(0, (lineIds.length-1));
    console.log("lineIds: *" + lineIds + "*");
    console.log("descrip: " + descrip + 
                "categoria: " + $("#categoriaB").val() + 
                "proyecto: " + proyecto + 
                "valor: " + valor + 
                "estatus: " + $("#estatusB").val() + 
                "notas: " + $("#notasB").val() + 
                "fechaAsignacion" + fechaAsignacion + 
                "fechaEntrega " + fechaEntrega);

    $.ajax({
        type: "POST",
        url: "/storeActivityBlock/",
        data: {
            "idsConsultores": lineIds,
            "descrip": descrip,
            "categoria": $("#categoriaB").val(),
            "proyecto": proyecto,
            "valor": valor,
            "estatus": $("#estatusB").val(),
            "notas": $("#notasB").val(),
            "fechaAsignacion": fechaAsignacion,
            "fechaEntrega": fechaEntrega
        },
        success: function (response) {
            alert("Actividades Asignadas Exitosamente!");
        },
        error: function (response){
            console.log("Error ajax: " + response);
        }
    });
}

function saveBonus(){
    var textCualidades = "";
    var cualidades = $("input[name='cualidades']:checked").each(function(){
        textCualidades = textCualidades + "-" + $(this).val();
    });
    console.log("Cualidades: " + textCualidades);

    $.ajax({
        type: "POST",
        url: "/storeBonus/",
        data: {
            "idConsultor": $("#idConsultor").val(),
            "descrip": textCualidades,
            "valor": $("#bonusValor").val(),
            "fechaAsignacion": today(),
        },
        success: function (response) {
            alert("Bonus Enviado Exitosamente!");
            $("#modSendBonus").modal("hide");
        },
        error: function (response){
            console.log("Error ajax: " + response.text);
            $("#modSendBonus").modal("hide");
        }
    });
}

function updateStatusActivity(idActivity, newStatus) {
    $.ajax({
        type: "POST",
        url: "/updateStatusAct/",
        data: {
            "idActivity": idActivity,
            "newStatus": newStatus
        },
        success: function (response) {
            showTaskList();
        },
        error: function (response){
            console.log("Error ajax: " + response.text);
        }
    });
}

function showStatistics(){
    $.ajax({
        type: "GET",
        url: "/statistics",
        success: function (response) {
            $("#divAdminContent").html("");
            $("#divAdminContent").html(response);
        },
        error: function (response){
            console.log("Error ajax: " + response);
        }
    });
}

function showGreenActivitiesReport(idContainer){
    $.ajax({
        type: "GET",
        url: "/consultGreenActivities",
        data: {
            "fechaInicial": $("#fechaInicial").val(),
            "fechaFinal": $("#fechaFinal").val()
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