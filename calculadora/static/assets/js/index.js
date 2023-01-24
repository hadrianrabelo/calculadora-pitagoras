import { parseSerializedArray, filterIsNaN } from "./functions.js";
import { API_HOST } from "./configs.js";


$("#form-pythagoras").submit(function(e) {

    let postData = $('form').serialize();

    e.preventDefault();

    console.log("Starting to serialize form...");
    const fields = parseSerializedArray($(this).serializeArray());


    console.log("Starting to filter fields that is NaN...");
    const fieldsNaN = filterIsNaN(fields);

    if (fieldsNaN.length != 1) {
        alert("Por favor, deixe exatamente um campo em branco!");
        throw new Error(`Por favor, deixe exatamente um campo em branco! Campos em branco ${fieldsNaN.length}`)
    }

    $.ajax({
        url: API_HOST,
        method: 'post',
        data: postData,
    }).done(function(data) {
        $('#result').html(data);
    });
});

