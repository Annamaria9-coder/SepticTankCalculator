// script.js

// Highlight active link in the sidebar on click
document.querySelectorAll('.sidebar a').forEach(link => {
    link.addEventListener('click', () => {
        document.querySelectorAll('.sidebar a').forEach(el => el.classList.remove('active')); // Remove active from all links
        link.classList.add('active'); // Add active to the clicked link
    });
});

// Sidebar toggle for mobile
document.addEventListener('DOMContentLoaded', () => {
    const sidebar = document.querySelector('.sidebar');
    const toggleButton = document.querySelector('.sidebar-toggle');

    if (toggleButton) {
        toggleButton.addEventListener('click', () => {
            sidebar.classList.toggle('hidden');
        });
    }
});
