/*    JavaScript 6th Edition
 *    Chapter 3
 *    Chapter case
 *    Tipton Turbines
 *    Variables and functions
 *    Author: Liliana Varela-Rodriguez
 *    Date:   9/16/2018
 *    Filename: tt.js
 */
//global variables 
var daysOfWeek = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
var opponents = ["Lightining", "Combines", "Combines", "Combines",
     "Lightining", "Lightining", "Lightining", "Lightining",
     "Barn Raisers", "Barn Raisers", "Barn Raisers", "Sodbusters", "Sodbusters", "Sodbusters", 
     "Sodbusters", "(off)", "River Riders", 
     "River Riders", "River Riders", "Big Dippers",
     "Big Dippers", "Big Dippers", "(off)",
     "Sodbusters", "Sodbusters", "Sodbusters", 
     "Combines", "Combines", "Combines", "(off)", "(off)"];
var gameLocations = ["away", "away", "away", "away", "home", "home",
     "home", "home", "home", "home", "home", "away",
     "away", "away", "away", "", "away", "away", "away",
     "away", "away", "away", "", "home", "home", "home",
     "home", "home", "home", "", ""];
// function to place daysOfWeek values in header row cells
function addColumnHeaders() {
    var i = 0;
    while (i < 7) {
        document.getElementsByTagName("th") [i].innerHTML = daysOfWeek[i];
        i++;
    }
}
// function to place day of month value in first p element within each table data cell that has an id
function addCalendarDates() {
    var i = 1;
    var paragraphs = "";
    do {
        var tableCell = document.getElementById("08-" + i);
        paragraphs = tableCell.getElementsByTagName("p");
        paragraphs[0].innerHTML = i;
        i++;
    } while (i <= 31);
}
// function to place opponents and gameLocation values in second p element within each table data cell that has an id
function addGameInfo () {
    var paragraphs = "";
    for (var i = 0; i < 31; i++) {
        var date = i + 1;
        var tableCell = document.getElementById("08-" + date);
        paragraphs = tableCell.getElementsByTagName ("p");
/*      if (gameLocations[i] === "away") {
            paragraphs[1].innerHTML = "@";
        }
        if (gameLocations[i] === "home") {
            paragraphs[1].innerHTML = "vs";
        }*/
/*        if (gameLocations[i] === "away") {
            paragraphs[1].innerHTML = "@ ";
        }
        else {
            paragraphs[1].innerHTML = "vs ";
        }
        if (gameLocations[i] === "away") {
            paragraphs[1].innerHTML = "@ ";
        }
        else {
            if (gameLocations[i] === "homes") {
                paragraphs[1].innerHTML = "vs ";
            }
        }*/
        switch (gameLocations[i]) {
            case "away":
                paragraphs[1].innerHTML = "@ ";
                break;
            case "home":
                paragraphs[1].innerHTML = "vs ";
                break;           
        }
        paragraphs[1].innerHTML += opponents[i];
    }
}
// function to populate calendar
function setUpPage () {
    addColumnHeaders();
    addCalendarDates();
    addGameInfo ();
}
// runs addColumnHeader() function when page loads

//window.addEventListener("load", addColumnHeaders, false);
// runs setUpPage () function when page loads
if (window.addEventListener) {
    window.addEventListener ("load", setUpPage, false);
} else if (window.attachEvent) {
    window.attachEvent ("onload", setUpPage);
}