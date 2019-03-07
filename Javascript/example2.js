'use strict'

window.addEventListener("load", function(event) {
    console.log("Archivo js cargado al html!");

    var lbs = prompt("Weight in libs?");
    
    var kg = lbs * 0.454;

    alert("That is: "+ kg + " kilograms");

    console.log("Conversion complete!");
    
});