// Wait for the DOM content to be fully loaded
document.addEventListener('DOMContentLoaded', function () {
    // Get the menu icon and menu bar elements
    const menuIcon = document.querySelector('.menu-icon');
    const menuBar = document.querySelector('.menu-bar');

    // Toggle the 'active' class on the menu bar when the icon is clicked
    menuIcon.addEventListener('click', function () {
        menuBar.classList.toggle('active');
    });
});