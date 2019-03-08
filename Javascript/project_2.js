'use strict'

window.addEventListener("load", function(event) {
    console.log("Archivo js cargado al html!");

    //sleepIn(false, false) = true
    //sleepIn(true, false) = false
    //sleepIn(false, true) = true

    function sleepIn(weekday, vacation) {
        var r = (!weekday || vacation);
        console.log(r);
        
    }

    sleepIn(false, true);

    //monkeyTrouble(true, true) = true
    //monkeyTrouble(false, false) = true
    //monkeyTrouble(true, false) = false
    
    function monkeyTrouble(aSmile, bSmile) {
        var r = (aSmile && bSmile) || (!aSmile && !bSmile);
        console.log(r);
    }

    //stringTimes("Hi", 1) = "Hi"
    //stringTimes("Hi", 2) = "HiHi"
    //stringTimes("Hi", 3) = "HiHiHi"

    function stringTimes(str, n) {
        var rstr = "";
        var i=0;

        while (i<n) {
            rstr += str;
            i++;
        }
        console.log(rstr);
    }

    //luckySum(1, 2, 3) = 6
    //luckySum(1, 2, 13) = 3
    //luckySum(1, 13, 3) = 1

    function luckySum(a, b, c) {
        var sum =0;
        if (a == 13) {
            break;
        }else if (b == 13) {
            sum += a;
            break;
        }else if (c == 13) {
            sum = a+b;
            break;
        }else{
            sum= a+b+c;
            break;
        }

        console.log(sum);
    }

    //caught_speeding(60, false) = 0
    //caught_speeding(65, false) = 1
    //caught_speeding(65, true) = 0

    function caught_speeding(speed, is_birthday) {
        if (is_birthday) {
            speed -= 5;
        }

        if (speed <= 60) {
            console.log(0);
            break;
        }

        if (60<speed<=80) {
            console.log(1);
            break;
        }

        console.log(2);
    }

    //makeBricks(3, 1, 8) = true
    //makeBricks(3, 1, 9) = false
    //makeBricks(3, 2, 10) = true

    function makeBricks(small, big, goal) {
        var r = goal%5 >=0 && goal%5 - small <=0 && small + 5*big >= goal;
        console.log(r);
    }

});
