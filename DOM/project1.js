'use strict'

window.addEventListener("load", function(event) {

    console.log("Archivo js cargado!");

    //Restart Game Button
    var restart = document.querySelector("#b");

    //Grabs all the squares
    var squares = document.querySelectorAll("td");

    //Clear al the squares
    function clearBoard() {
        for (var i = 0; i < squares.length; i++) {
            squares[i].textContent = "";
            
        }  
    }

    restart.addEventListener('click', clearBoard);

    //Check the square marker
    function changeMarker() {
        if (this.textContent == '') {
            this.textContent = 'X';
            console.log("Choose letter X");
            
        }else if (this.textContent == 'X') {
            this.textContent = 'O';
            console.log("Choose letter O");
            
        }else{
            this.textContent = '';
            console.clear();
            
        }
    }    

    //For loop add event listeners to all the squares 
    for (var j = 0; j < squares.length; j++) {
        squares[j].addEventListener('click', changeMarker);
        
    }
});