'use strict'

window.addEventListener("load", function(event) {
    console.log("Archivo js cargado al html!");

    //Crear menu con opciones de agregar, eliminar, mostrar usuarios y la opcion de salir.
    //cada una de las opciones estara detallada en una funcion 

    //Comenzaremos declarando el array
    var est = [];

    //funcion para agregar un nuevo nombre
    function add() {
        var name = prompt("What name would you like add?");

        est.push(name);//agregar el nombre al final del arreglo
    }

    //funcion para eliminar un nombre de la lista
    function remove() {
        var rem = prompt("What name would you like remove?");

        var index = est.indexOf(rem);
        est.splice(index,1);
    }

    //funcion para mostrar los nombre que estan en el arreglo
    function show() {
        console.log(est);
    }


    //construir menu para que corra el programa

    var start = prompt("Would you like to start the student Web app? y/n");
    var req = "empty";

    if (start == "y") {
        while (req != "quit") {
            req = prompt("Please select an action: add, remove, display or quit ...");

            if (req == "add") {
                add();
            }else if (req == "remove") {
                remove();
            }else if (req == "display") {
                show();
            }else if (req == "quit") {
                alert("BYE!");
            }else{
                alert("Option no recognized! :(");
            }
        }
        
    }else{
        alert("Thanks for you visit... BYE!");
        
    }

});
