function filterIsNaN(fields) {
    return fields.filter(function (index) {
        return isNaN(index["value"]);
    });
}

function parseSerializedArray(arr) {
    for (let i = 0; i < arr.length; i++) {
        arr[i]["value"] = parseFloat(arr[i]["value"]);
    }
    return arr;
}

export {filterIsNaN, parseSerializedArray}