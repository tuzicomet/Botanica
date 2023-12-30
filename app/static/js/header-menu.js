/*
    header-menu.js - Script for handling the header menu functionality on the Botanica website.

    This script includes the logic for toggling the menu bar and managing the overlay.

    Author: Leonard Lau
    Last Updated: 30/12/2023
*/

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

// Add an event listener to close the menu when clicking outside the menu bar
document.addEventListener('click', (event) => {
    if (!menuBar.contains(event.target) && !menuIcon.contains(event.target)) {
        menuBar.classList.remove('active');
        overlay.classList.remove('open');
    }
});