const header = document.querySelector("header");
const instadropTitle = document.querySelector(".instadrop-title");
var navlinks = header.querySelectorAll(".nav-link");
var sublistNav = header.querySelector(".sub-list-nav");
var subLinks = header.querySelectorAll(".sub-link"); 
var sideNavLinks = header.querySelectorAll(".side-nav-link");

const NameOptions = {
    rootMargin: "-300px 0px 0px 0px"
};

const whitenHeader = new IntersectionObserver(function(entries, whitenHeader){
    entries.forEach(entry => {
        if(!entry.isIntersecting)
        {
            header.classList.add("whitened");
            document.getElementById("burger").src = "{% static 'Logistics/images/menu-icon-hamburger-black.svg' %}";
            navlinks.forEach(link =>{
                link.classList.add("blackened");
            });
            document.getElementById("instalogo").src = "{% static 'Logistics/images/instadrop-logo-black.svg' %}";          
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
            document.getElementById("instalogo").src = "{% static 'Logistics/images/instadrop-logo-white.svg %}";          
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

whitenHeader.observe(instadropTitle);



const serviceImage = document.querySelectorAll(".from-right");
const serviceWords = document.querySelectorAll(".from-left");

const appearingOptions = {
    threshold:1,
    rootMargin: "0px 0px 180px 0px"
};

const appearOnScroll = new IntersectionObserver(function(entries, appearOnScroll){
    entries.forEach(entry => {
        if(!entry.isIntersecting)
        {
            return;
        }
        else{
            entry.target.classList.add('appear');
            appearOnScroll.unobserve(entry.target);
        }
    })
}, appearingOptions);

serviceImage.forEach(service =>{
    appearOnScroll.observe(service)
})


const showOnScroll = new IntersectionObserver(function(entries, showOnScroll){
    entries.forEach(entry => {
        if(!entry.isIntersecting)
        {
            return;
        }
        else{
            entry.target.classList.add('fade-in');
            showOnScroll.unobserve(entry.target);
        }
    })
}, appearingOptions);

serviceWords.forEach(word =>{
    showOnScroll.observe(word)
})

 ADDING JAVASCRIPT FOR SHIPMENT NAV START

let mainNavItem = document.querySelectorAll(".nav-list-item");
 

let shipmentMenu = document.querySelector(".sub-list-nav");

const navItemShipment = mainNavItem[3];

function showShipmentMenu(e)
{    
    let fontAwesome = document.querySelector("#font-awesome");
    let fontAwesomeStyle = fontAwesome.getAttribute("data-shown");

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

// JAVASCRIPT FOR NAVIGATION BUTTON STARTS
let navButton = document.querySelector(".mobile-button");
const menuOption = document.querySelector(".header");

function displayMenu(e)
{
    var menuOptionSelected = menuOption.getAttribute("data-appear");
    if(e.type == "click"){
        if(menuOptionSelected == ""){
            menuOption.setAttribute("data-appear", "true");
            navButton.setAttribute("data-spin","spinning");
            whitenHeader.unobserve(instadropTitle);
            sublistNav.classList.remove("whitened");
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
    };
    


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

// JAVASCRIPT FOR NAVIGATION BUTTON ENDS
