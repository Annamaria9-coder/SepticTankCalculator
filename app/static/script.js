// script.js
document.querySelectorAll('.sidebar a').forEach(link => {
    link.addEventListener('click', () => {
        link.classList.add('active');
        setTimeout(() => link.classList.remove('active'), 200);
    });
});
