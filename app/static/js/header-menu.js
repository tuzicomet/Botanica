// Get the menu icon, menu bar, and overlay elements
const menuIcon = document.querySelector('.menu-icon');
const menuBar = document.querySelector('.menu-bar');
const overlay = document.querySelector('.overlay');

// Toggle the 'active' class on the menu bar when the icon is clicked
menuIcon.addEventListener('click', () => {
    // Toggle the 'active' class on the menu bar
    menuBar.classList.toggle('active');

    // Toggle the 'open' class on the overlay for dimming effect
    overlay.classList.toggle('open');
});