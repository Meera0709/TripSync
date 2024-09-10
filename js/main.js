document.addEventListener('DOMContentLoaded', function() {
    // Add interactivity for form submissions, smooth scrolling, etc.
    console.log('TripSync App Loaded!');

    // Smooth scrolling for internal navigation links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });
});
