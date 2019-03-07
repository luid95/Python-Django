'use strict'

window.addEventListener("load", function(event) {
    console.log("Archivo js cargado al html!");

    var hot = false;
    var temp = 50;

    if(temp > 80){
        console.log("Hot Outside!");
    }else if(temp <= 80 && temp >= 50 ){
        console.log("Average Temp Outside!");

    }else if(temp < 50 && temp >32){
        console.log("It's prety could out!");

    }else{
        console.log("It's very could out");

    }

    var ham = 10;
    var cheese = 10;

    var report = "blank";

    if(ham >=10 && cheese >= 10){
        report= "Strong sales of both ham and cheese!";

    }else if(ham == 0 && cheese == 0){
        report= "Nothing Sold!";

    }else{
        report= "We had some sales of team";

    }

    console.log(report);
    
    
});