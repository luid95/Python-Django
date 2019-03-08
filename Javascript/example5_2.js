'use strict'

window.addEventListener("load", function(event) {
    console.log("Exercise loops (while, for)!");

    /*Problem 1
    Use a for loop to print (console.log) out the world "hello" 5 times 
    *Do this with a while looop and a for loop*/
   
    //while loop

    var x=0;

    while (x<5) {
        console.log("hello");
        x++;
    }

    for (var i = 0; i < 5; i++) {
        console.log("Hello since for loop");
        
    }

    /*Numbers */
    var num=0;

    while (num<25) {
        if (num%2 != 0) {
            console.log(num);
        }
        num++;
    }

    console.log("With for..");

    for (var i = 0; i < 25; i++) {
        if (i%2 != 0) {
            console.log(i);
        }
        
    }
});