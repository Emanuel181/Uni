document.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('.animate-form');

    // Add the class to trigger the animation after a short delay
    setTimeout(() => {
        form.classList.add('form-animated');
    }, 500); // Delay of 500ms
});

document.addEventListener('DOMContentLoaded', () => {
    const container = document.querySelector('.animate-container');

    // Add the class to trigger the animation after a short delay
    setTimeout(() => {
        container.classList.add('container-animated');
    }, 500); // Delay of 500ms
});
