'use strict'

window.addEventListener("load", function(event) {
    console.log("For loops...!");

    for (let i = 0; i < 5; i++) {
        
        console.log("Nujmber is: "+ i);

    }

    var word = "ABCDEFGHIJK";

    console.log("Algunas letras del abecedario...");
    

    for (var i = 0; i < word.length; i++) {
        console.log(word[i]);
        
    }
    
});