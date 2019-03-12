'use strict'

window.addEventListener("load", function(event) {
    console.log("Archivo js cargado al html!");

    //Ejercicios de objetos.
    
    var employed = {
        name: 'Jhon Smith',
        job: 'Programmer',
        age: 25,
        namelength: function () {
            console.log(this.name.length);
            
        },
        report: function () {
            console.log("Name is: "+ this.name);
            console.log("Job is: "+ this.job);
            console.log("Age is: "+ this.age);
                        
        },
        lastname: function (){
            console.log(this.name.split(" ")[1]);
            
        }
    }

    console.log(employed);
    
    
});
