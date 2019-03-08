'use strict'

window.addEventListener("load", function(event) {
    console.log("Project...!");
    //Four conditions

    var fname= prompt("First name please: ");
    var lname= prompt("Last name please: ");
    var age= prompt("How old are you? ");
    var height= prompt("What is your height? ");
    var pet= prompt("Whats is yout pet name? ");
    alert("Thank so much for the information!");

    var ncond =null;
    var acond = null;
    var hcond = null;
    var pcond = null;
    
    //name condition

    if (fname[0] == lname[0]) {
        ncond = true;
    }else{
        ncond = false;
    }

    //age
    if (age >20 && age <30) {
        acond = true;
    }else{
        acond = false;
    }
    
    //height
    if (height > 170) {
        hcond = true;
    }else{
        hcond = false;
    }

    //pet
    if (pet[pet.length-1] == "y") {
        pcond = true;
    }else{
        pcond = false;
    }

    if (ncond==true && acond==true && hcond==true && pcond==true) {
        console.log("Welcome SPY");
    }else{
        console.log("Nothing to see here!");
    }
});