'use strict'

window.addEventListener("load", function(event) {
    console.log("Archivo js cargado al html!");

    function hello() {
        console.log("Hello world!");
    }

    hello();
    
    //with params
    function helloyou(name) {
        console.log("Hello "+name);
    }

    helloyou("luis");

    //operations
    function add(num1, num2) {
        var res = num1 + num2;

        console.log("La suma de los numeros es: "+ res);
    }

    add(3,7);

    //concat
    function formal(name="Luis", title="Eng.") {
        console.log("Hello "+ title+ " "+name);
    }

    formal();
    
    //operaciones
    var num=0;
    function mul(num) {
        var res = num*5;

        return res;
    }

    var r1 = mul(10);
    console.log("La multiplicacion de 10 y 5 es: "+ r1);
    

});
