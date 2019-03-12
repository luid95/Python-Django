'use strict'

window.addEventListener("load", function(event) {
    $('h1').click(function () {
        console.log("There was a click!");
        $(this).text("I was changed!");
        
    });

    $('li').click(function () {
        console.log("Any li was a click!");
        
    });

    //key press
    $('input').eq(0).keypress(function(){
        $('h3').toggleClass('turnBlue');
    });

    //on
    $('li').on('dblclick', function(){
        $(this).toggleClass('turnBlue');
    });

    $('h2').on('mouseenter', function(){
        $(this).toggleClass('turnBlue');
    });

    //desvanecer
    /*$('input').eq(1).on('click', function(){
        $('.container').fadeOut(3000);
    });*/
    //
    $('input').eq(1).on('click', function(){
        $('.container').slideUp(3000);
    })

     
});