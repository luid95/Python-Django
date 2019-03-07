'use strict'

window.addEventListener("load", function(event) {
    console.log("Archivo js cargado al html!");

    var x = 0;

    while (x < 5) {
        console.log("x is currently: " +x);

        if(x===3){
            console.log("X is equal to three!");

            break;
            
        }

        console.log("x is still less than 5, adding 1 to x");
        
        x += 1;
        
    }
    
    var num=0;

    while (num<11) {
        if(num%2 ==0){
            console.log(num);
            
        }
        num += 1;
    }
    
});