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

document.getElementById('contactForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the default form submission

    var name = this.name.value;
    var email = this.email.value;
    var phone = this.phone.value;
    var message = this.message.value;

    var mailtoLink = `mailto:unihack235@gmail.com?subject=Contact Form Submission&body=Name: ${name}%0AEmail: ${email}%0APhone: ${phone}%0AMessage: ${message}`;
    window.location.href = mailtoLink; // Open the mail client with the composed message
});
