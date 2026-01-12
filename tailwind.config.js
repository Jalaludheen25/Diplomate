/** @type {import('tailwindcss').Config} */
module.exports = {
    content: ["./*.html", "./script.js"],
    theme: {
        extend: {
            colors: {
                navy: {
                    900: '#0f172a',
                },
                indigo: {
                    700: '#4338ca',
                },
                gold: {
                    500: '#d4af37',
                },
                lightblue: {
                    200: '#bfdbfe',
                },
                offwhite: {
                    50: '#f9fafb',
                }
            },
            fontFamily: {
                sans: ['Inter', 'sans-serif'],
                heading: ['Outfit', 'sans-serif'],
            },
            animation: {
                'fade-in': 'fadeIn 0.8s ease-out forwards',
            },
            keyframes: {
                fadeIn: {
                    'from': { opacity: '0', transform: 'translateY(20px)' },
                    'to': { opacity: '1', transform: 'translateY(0)' },
                }
            },
            boxShadow: {
                'gold': '0 10px 15px -3px rgba(212, 175, 55, 0.2), 0 4px 6px -2px rgba(212, 175, 55, 0.1)',
            }
        },
    },
    plugins: [],
}
