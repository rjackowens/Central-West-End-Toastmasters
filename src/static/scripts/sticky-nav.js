// Execute on user scroll
window.onscroll = function() {userScroll()};

// Get navbar
var navbar = document.getElementById("navbar");

// Get offset position of navbar
var sticky = navbar.offsetTop;

// Add sticky class to navbar after reaching scroll position
function userScroll() {
    if (window.pageYOffset >= sticky) {
        navbar.classList.add("sticky")
    } else {
        navbar.classList.remove("sticky");
    }
}
