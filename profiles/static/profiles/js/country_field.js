/*
    Handle the css for the country field in the deafult delivery info form
*/

// Define the country field variable
let selectedCountry = $('#id_default_country').val();

// Change the css colour of the field
// depending on whether a country is selected or not
if(!selectedCountry) {
    $('#id_default_country').css('color', '#aab7c4')
}
$('#id_default_country').change(function() {
    selectedCountry = $(this).val();
    if(!selectedCountry) {
        $(this).css('color', '#aab7c4');
    } else {
        $(this).css('color', '#000000')
    }
});