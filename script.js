/**
 * Diplomate - Business Consultancy Logic
 * Handles Sticky Navbar, Mobile Menu, and Cost Calculator
 */

document.addEventListener('DOMContentLoaded', () => {
    initNavbar();
    initMobileMenu();
    initCostCalculator();
});

/**
 * Mobile Accordion Toggle
 */
function toggleMobileAccordion(id) {
    const content = document.getElementById(id);
    const button = content.previousElementSibling;
    const icon = button.querySelector('svg');

    // Close other open accordions
    document.querySelectorAll('.mobile-accordion div').forEach(div => {
        if (div.id !== id && !div.classList.contains('hidden')) {
            div.classList.add('hidden');
            div.previousElementSibling.querySelector('svg').classList.remove('rotate-180');
        }
    });

    content.classList.toggle('hidden');
    icon.classList.toggle('rotate-180');
}

/**
 * Sticky Navbar on Scroll
 */
function initNavbar() {
    const navbar = document.getElementById('navbar');

    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            navbar.classList.add('shadow-lg', 'scrolled');
            navbar.classList.add('py-2');
            navbar.classList.remove('py-4');
        } else {
            navbar.classList.remove('shadow-lg', 'scrolled');
            navbar.classList.remove('py-2');
            navbar.classList.add('py-4');
        }
    });
}

/**
 * Mobile Menu Toggle Logic
 */
function initMobileMenu() {
    const menuBtn = document.getElementById('mobile-menu-btn');
    const closeBtn = document.getElementById('close-menu-btn');
    const mobileMenu = document.getElementById('mobile-menu');
    const overlay = document.getElementById('menu-overlay');

    const toggleMenu = (show) => {
        if (show) {
            mobileMenu.classList.remove('translate-x-full');
            overlay.classList.remove('opacity-0', 'pointer-events-none');
            overlay.classList.add('opacity-100', 'pointer-events-auto');
            document.body.style.overflow = 'hidden';
        } else {
            mobileMenu.classList.add('translate-x-full');
            overlay.classList.add('opacity-0', 'pointer-events-none');
            overlay.classList.remove('opacity-100', 'pointer-events-auto');
            document.body.style.overflow = '';
        }
    };

    menuBtn.addEventListener('click', () => toggleMenu(true));
    closeBtn.addEventListener('click', () => toggleMenu(false));
    overlay.addEventListener('click', () => toggleMenu(false));

    // Close menu on link click
    mobileMenu.querySelectorAll('a').forEach(link => {
        link.addEventListener('click', () => toggleMenu(false));
    });
}

/**
 * Dynamic Cost Calculator
 */
function initCostCalculator() {
    const jurisdiction = document.getElementById('jurisdiction');
    const visas = document.getElementById('visas');
    const totalCostDisplay = document.getElementById('total-cost');

    if (!jurisdiction || !visas || !totalCostDisplay) return;

    function calculateTotal() {
        const basePrice = parseInt(jurisdiction.value) || 0;
        const visaCost = parseInt(visas.value) || 0;
        const total = basePrice + visaCost;

        // Animate counter effect (simple)
        animateValue(totalCostDisplay, parseInt(totalCostDisplay.innerText.replace(',', '')), total, 500);
    }

    // Event listeners
    jurisdiction.addEventListener('change', calculateTotal);
    visas.addEventListener('change', calculateTotal);
}

/**
 * Simple Counter Animation
 */
function animateValue(obj, start, end, duration) {
    let startTimestamp = null;
    const step = (timestamp) => {
        if (!startTimestamp) startTimestamp = timestamp;
        const progress = Math.min((timestamp - startTimestamp) / duration, 1);
        const value = Math.floor(progress * (end - start) + start);
        obj.innerText = value.toLocaleString();
        if (progress < 1) {
            window.requestAnimationFrame(step);
        }
    };
    window.requestAnimationFrame(step);
}

/**
 * Form Submission (Placeholder)
 */
const heroForm = document.getElementById('hero-form');
if (heroForm) {
    heroForm.addEventListener('submit', (e) => {
        e.preventDefault();
        alert('Thank you! Your request for consultation has been received. Our manager will contact you shortly.');
        heroForm.reset();
    });
}
