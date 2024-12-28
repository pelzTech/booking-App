document.addEventListener('DOMContentLoaded', () => {
    const toggleButton = document.getElementById('theme-toggle');
    const root = document.documentElement;

    toggleButton.addEventListener('click', () => {
        if (root.style.getPropertyValue('--background-color') === '#121212') {
            root.style.setProperty('--background-color', '#f8f8f8');
            root.style.setProperty('--text-color', '#333');
            root.style.setProperty('--hover-color', '#007BFF');
            root.style.setProperty('--button-bg', '#007BFF');
            root.style.setProperty('--button-color', '#fff');
            toggleButton.textContent = 'Dark Mode';
        } else {
            root.style.setProperty('--background-color', '#121212');
            root.style.setProperty('--text-color', '#f8f8f8');
            root.style.setProperty('--hover-color', '#BB86FC');
            root.style.setProperty('--button-bg', '#BB86FC');
            root.style.setProperty('--button-color', '#121212');
            toggleButton.textContent = 'Default Mode';
        }
    });
});