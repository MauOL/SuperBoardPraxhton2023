/**
 * Functiones comunes a la funcionalidad de todo el sitio web
 */
Date.prototype.toDateInputValue = (function() {
    var local = new Date(this);
    local.setMinutes(this.getMinutes() - this.getTimezoneOffset());
    return local.toJSON().slice(0,10);
});

function today() {
    return new Date().toDateInputValue();
}

function checkAllBoxes(checksName, idUpperCheck){
    var isUpperChecked = $("#" + idUpperCheck).is(":checked");
    $("input[name='" + checksName + "']").prop("checked", isUpperChecked);
}

function cleanForm(idForm){
    $("#" + idForm)[0].reset();
}