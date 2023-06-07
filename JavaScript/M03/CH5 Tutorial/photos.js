/*    JavaScript 6th Edition
 *    Chapter 5
 *    Chapter case

 *    Photo gallery
 *    Variables and functions
 *    Author: Liliana Varela-Rodriguez
 *    Date:   09/30/218

 *    Filename: photos.js
 */
 "use strict"; // interpret document contents in JavaScript strict mode

/* global variables */
var photoOrder = [1,2,3,4,5];
var figureCount = 3;
var autoAdvance = setInterval(rightAdvance, 5000);	
/* 
   add src values to img elements based on order specified 
   in photoOrder array 
 */
   
function populateFigures() 
{
	var filename;
	var currentFig;
	
	if (figureCount === 3)
	{
		for (var i = 1; i < 4; i++)
		{
		filename = "images/IMG_0" + photoOrder[i] + "sm.jpg";
		currentFig = document.getElementsByTagName("img") [i - 1];
		currentFig.src = filename;
		}
	}
	else 
		{
		for (var i = 0; i < 5; i++)
		{
			filename = "images/IMG_0" + photoOrder[i] + "sm.jpg";
			currentFig = document.getElementsByTagName("img")[i];
			currentFig.src = filename;
		}
	}
}

/* shift all images one figure to the right, and change values in photoOrder array to match  */
function leftArrow() 
{
	clearInterval(autoAdvance);
   for (var i = 0; i < 5; i++) 
   {
      if ((photoOrder[i] - 1) === 0)
	  {
         photoOrder[i] = 5;
      } 
	  else 
	  {
         photoOrder[i] -= 1;
      }
      populateFigures();
   }
}

/*	create figure and img elements for fifth image

	this gets the element we want to attach to:
	var articleE1 = document.getElementsByTagName("article")[0];
	
	this statement uses the createElement() method to create a new 
	figure element and assign it to the variable name lastFigure. 
	var lastFigure = document.createElement("figure");
	
	
 	Attach node by specifying the [child] node to be attached
	and the node to attach it to. 
	
	parentNode.appendChild(childNode)
	
	var articleE1 = document.getElementsByTagName("article")[0];
	
	
	This statement uses the appendChild() method to add the lastImage node as a 
	child node of the lastFigure node, creating a document fragment:
	
		lastFigure.appendChild(lastImage);
		
	This statement uses the appendChild method to attach the lastFigure document 
	fragment as a child of the article element in the document (referenced 
	by the articleE1 variable):
	
		articleE1.appendChild(lastFigure);
	
	
*/

// switch to 5-image layout
function previewFive()
{
	// set value of articleE1 variable to the first element with the tag name article
	var articleE1 = document.getElementsByTagName("article")[0];
	
	// create figure and img elements for fifth image
	// create a new figure element and assign it to the variable name lastFigure
	var lastFigure = document.createElement("figure");
		lastFigure.id = "fig5";
		lastFigure.style.zIndex = "5";
		lastFigure.style.position = "absolute";
		lastFigure.style.right = "45px";
		lastFigure.style.top = "67px";
		
		// use createElement() method to create a new img element, then assign it 
		var lastImage = document.createElement("img");
		// assign values to element's width and height attributes
		lastImage.width = "240";
		lastImage.height = "135";
				
		// This statement uses the appendChild() method to add the lastImage node as a 
		// child node of the lastFigure node, creating a document fragment
		lastFigure.appendChild(lastImage);
		
		//	This statement uses the appendChild method to attach the lastFigure document 
		// 	fragment as a child of the article element in the document (referenced 
		//	by the articleE1 variable)
		
		//  articleE1.appendChild(lastFigure);
		articleE1.insertBefore(lastFigure, document.getElementById("rightArrow"));
		
		//	clone figure element for fifth image and edit to be first image; 
		var firstFigure = lastFigure.cloneNode(true);
		firstFigure.id = "fig1";
		firstFigure.style.right = "";
		firstFigure.style.left = "45px";
		
		// articleE1.appendChild(firstFigure);
		articleE1.insertBefore(firstFigure, document.getElementById("fig2"));
		// add appropriate values to two new img elements
		// the two statements assign values to the src attributes for
		// the two new img elements
		document.getElementsByTagName("img")[0].src = "images/IMG_0" + photoOrder[0] + "sm.jpg";
		document.getElementsByTagName("img")[4].src = "images/IMG_0" + photoOrder[4] + "sm.jpg";
		
		figureCount = 5;
		
		//change button to hide extra images
		var numberButton = document.querySelector("#fiveButton p"); 
		numberButton.innerHTML = "Show fewer images";
		if (numberButton.addEventListener) 
		{
			numberButton.removeEventListener("click", previewFive, false);
			numberButton.addEventListener("click", previewThree, false);
			} else if (numberButton.attachEvent)
			{
				numberButton.detachEvent("onclick", previewFive);
				numberButton.attachEvent("onclick", previewThree);
			}
		}

/* switch to 3-image layout */ 
function previewThree() 
{
	var articleEl = document.getElementsByTagName("article")[0];
	var numberButton = document.querySelector("#fiveButton p"); 
	
	articleEl.removeChild(document.getElementById("fig1"));
	articleEl.removeChild(document.getElementById("fig5"));
	
	figureCount = 3; 
	numberButton.innerHTML = "Show more images";
	if (numberButton.addEventListener) 
	{
		numberButton.removeEventListener("click", previewThree, false);
		numberButton.addEventListener("click", previewFive, false);
	} 
	else if (numberButton.attachEvent)
	{
		numberButton.detachEvent("onclick", previewThree); 
		numberButton.attachEvent("onclick", previewFive); 
	}
}		

 // stop automatic image switching and call rightAdvance() function
 function rightArrow() 
 {
	 clearInterval(autoAdvance); 
	 rightAdvance();
 }
		
/* 	shift all images one figure to the left, and 
	change values in photoOrder array to match  */
function rightAdvance() 
{
   for (var i = 0; i < 5; i++) 
   {
      if ((photoOrder[i] + 1) === 6) 
	  {
         photoOrder[i] = 1;
      }
	  else 
	  {
         photoOrder[i] += 1;
      }
      populateFigures();
   }
}
	
/* create event listeners for left arrow, right arrow, and center figure element */

function createEventListeners()
{
	// This statement creates a local variable named leftArrow, then uses the getElementById()
	// method to specify the variable value as the document element with the id value leftarrow
	
	var leftarrow = document.getElementById("leftarrow");

	if (leftarrow.addEventListener) 
	{
		leftarrow.addEventListener("click", leftArrow, false);
	} 
	else if (leftarrow.attachEvent) 
	{
		leftarrow.attachEvent("onclick", leftArrow);
	}
	
	var rightarrow = document.getElementById("rightarrow");

	if (rightarrow.addEventListener) 
	{
		rightarrow.addEventListener("click", rightArrow, false);
	} 
	else if (rightarrow.attachEvent) 
	{
		rightarrow.attachEvent("onclick", rightArrow);
	}
	
	
	// Uses the getElementsByTagName() method to assign var
	// mainFig the value of the second img element
	var mainFig = document.getElementsByTagName("img")[1];
	
	// this code calls a function when a user clicks the middle (main)
	// image in the gallery. 
	if (mainFig.addEventListener)
	{
		mainFig.addEventListener("click", zoomFig, false);
	}
	else if (mainFig.attachEvent)
	{
		mainFig.attachEvent("onclick, zoomFig");
	}	
		
	// add eventListener that calls the previewFive() function
	// when a user clicks the Show more images button. 
		
	var showAllButton = document.querySelector("#fiveButton p");
	if (showAllButton.addEventListener)
	{
		showAllButton.addEventListener("click", previewFive,
		false);
	}
	else if (showAllButton.attachEvent)
	{
		showAllButton.attachEvent("onclick", previewFive);
	}
} // end createEventListeners()	

/*
	The calculation of the winLeft variable starts with the width 
	of the existing browser window minus the width of the new browser 
	window, divided by two. This determines the amount the new window 
	should be offset from the left edge of the existing window. The 
	calculation for the winTop variable is similar to winLeft, using 
	vertical properties instead of horizontal ones. The winOptions 
	variable creates an options string for the window.open() method 
	that incorporates the calculated values.
*/

/* open center figure in separate window */
function zoomFig() 
{
	var propertyWidth = 960;
	var propertyHeight = 600;
	var winLeft = ((screen.width - propertyWidth) / 2);
	var winTop = ((screen.height - propertyHeight) / 2);
	var winOptions = "width=960,height=600";
	winOptions += ",left=" + winLeft;
	winOptions += ",top=" + winTop;	
  
  var zoomwin = window.open("zoom.htm", zoomwin,
	winOptions);
  zoomWindow.focus();
 
 /* 
     The statement that opens the photo gallery slideshow web page 
	 assigns an object representing the new web browser window to
	 a variable named zoomWindow. You can use any of the properties
	 and methods of the Window object with a variable that 
	 represents a Window object. 
  */ 
  
  // You append the focus() method to the variable that represents 
  // the window, not to the name argument of the window.open() method.
  

}

/* create event listeners and populate image elements */
function setUpPage() {
   createEventListeners();
   populateFigures();
}

/* run setUpPage() function when page finishes loading */
if (window.addEventListener) {
  window.addEventListener("load", setUpPage, false); 
} else if (window.attachEvent)  {
  window.attachEvent("onload", setUpPage);
}