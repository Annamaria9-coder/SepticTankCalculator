// script.js
document.addEventListener('DOMContentLoaded', () => {
    const sidebar = document.querySelector('.sidebar');
    const toggleButton = document.getElementById('toggle-sidebar');

    if (sidebar && toggleButton) {
        // Toggle the sidebar visibility
        toggleButton.addEventListener('click', () => {
            sidebar.classList.toggle('visible');
        });

        // Close the sidebar when clicking outside (for mobile usability)
        document.addEventListener('click', (event) => {
            if (!sidebar.contains(event.target) && !toggleButton.contains(event.target)) {
                sidebar.classList.remove('visible');
            }
        });
    } else {
        console.error('Sidebar or toggle button not found in the DOM.');
    }
});
