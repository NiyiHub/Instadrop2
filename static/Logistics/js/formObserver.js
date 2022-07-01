/*!
* Start Bootstrap - Landing Page v6.0.4 (https://startbootstrap.com/theme/landing-page)
* Copyright 2013-2021 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-landing-page/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project

// FORM OBSERVERS START
var navButton = document.querySelector(".mobile-button");
const menuOption = document.querySelector(".header");
const instadropTitle = document.querySelector(".instadrop-title");


function displayMenu(e)
{
    var menuOptionSelected = menuOption.getAttribute("data-appear");
    if(e.type == "click"){
        if(menuOptionSelected == ""){
            document.getElementById("burger").src = "{% static 'Logistics/images/instadrop-logo-white.svg' %}";
            menuOption.setAttribute("data-appear", "true");
            navButton.setAttribute("data-spin","spinning");
            // whitenHeader.unobserve(instadropTitle);
            // sublistNav.classList.remove("whitened");
            navlinks.forEach(link =>{
                link.classList.remove("blackened");
            });
            subLinks.forEach(sublink =>{
                sublink.classList.remove("reddened");
            });    
        }
        else if (menuOptionSelected == "true")
        {
            menuOption.setAttribute("data-appear", "false");
            navButton.setAttribute("data-spin","");
            // whitenHeader.observe(instadropTitle);
        }
        else if (menuOptionSelected == "false")
        {
            menuOption.setAttribute("data-appear", "true");
        }
    }
    
    function revert(){
        var opin = menuOption.getAttribute("data-appear");
        if(opin == "false")
        {
            menuOption.setAttribute("data-appear", "");
        }
        console.log(opin);
    };
    
    setTimeout(revert, 500);
}

navButton.addEventListener("click", displayMenu);


//  ADDING JAVASCRIPT FOR SHIPMENT NAV START

var mainNavItem = document.querySelectorAll(".nav-list-item");

var navItemShipment = mainNavItem[3];

var shipmentMenu = document.querySelector(".sub-list-nav"); 


function showShipmentMenu(e)
{
    var fontAwesome = document.querySelector("#font-awesome");
    var fontAwesomeStyle = fontAwesome.getAttribute("data-shown");

    if(e.type == "click"){
        shipmentMenu.classList.toggle("opened-up");
        if(fontAwesomeStyle == "right")
        {
            fontAwesome.setAttribute("data-shown","down");
        }
        else if(fontAwesomeStyle == "down"){
            fontAwesome.setAttribute("data-shown","right");
        }
    }
}

navItemShipment.addEventListener("click", showShipmentMenu);
//  ADDING JAVASCRIPT FOR SHIPMENT NAV ENDS


const header = document.querySelector("header");
const instructions = document.querySelector(".instructions");
var instaLogo = document.querySelector(".instadrop-logo");
var navlinks = header.querySelectorAll(".nav-link");
var sublistNav = header.querySelector(".sub-list-nav");
var subLinks = header.querySelectorAll(".sub-link"); 
var sideNavLinks = header.querySelectorAll(".side-nav-link");
const aboutUsHeader = document.querySelector(".about-us-header");

const NameOptions = {
    rootMargin: "-100px 0px 0px 0px"
  };
  
const whitenHeader = new IntersectionObserver(function(entries, whitenHeader){
    entries.forEach(entry => {
        if(!entry.isIntersecting)
        {
            header.classList.add("whitened");
            document.getElementById("burger").src = "{% static 'Logistics/images/menu-icon-hamburger-white.svg' %}";
            document.getElementById("instalogo").src = "{% static 'Logistics/images/instadrop-logo-white.svg' %}";          
            navlinks.forEach(link =>{
                link.classList.add("blackened");
            });
            sublistNav.classList.add("whitened");
            subLinks.forEach(sublink =>{
                sublink.classList.add("reddened");
            });
            sideNavLinks.forEach(sidelink =>{
                sidelink.classList.toggle("switch");
            });
        }
        else{
            header.classList.remove("whitened");
            document.getElementById("burger").src = "{% static 'Logistics/images/menu-icon-hamburger-white.svg' %}";
            document.getElementById("instalogo").src = "{% static 'Logistics/images/instadrop-logo-white.svg' %}"; 
            navlinks.forEach(link =>{
                link.classList.remove("blackened");
            });
            sublistNav.classList.remove("whitened");
            subLinks.forEach(sublink =>{
                sublink.classList.remove("reddened");
            });
            sideNavLinks.forEach(sidelink =>{
                sidelink.classList.toggle("switch");
            });
        }
    })
}, NameOptions);

whitenHeader.observe(instructions);

// FORM OBSERVERS END
