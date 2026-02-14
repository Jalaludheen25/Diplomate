import os

# index.html uses 'brand-card' for dropdowns, unlike others which were updated to bg-[#1a1a1a]/95 then /80.
# We need to replace 'brand-card' with 'bg-[#1a1a1a]/80' and 'backdrop-blur-sm' in index.html specifically for dropdowns.

filepath = '/Users/jalaludheenok/development/Diplomate/index.html'

replacements = [
    # Dropdown container in index.html (About Us, Contacts, Business Setup)
    # Business Setup Mega Menu
    (
        'class="absolute top-20 left-0 w-full brand-card shadow-2xl border-t border-gray-100 opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-300 z-50 overflow-hidden"',
        'class="absolute top-20 left-0 w-full bg-[#1a1a1a]/80 shadow-2xl border-t border-gray-700 opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-300 z-50 overflow-hidden backdrop-blur-sm"'
    ),
    # About Us Dropdown
    (
        'class="absolute top-20 left-0 w-64 brand-card shadow-xl border border-gray-100 opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-300 z-50 rounded-b-xl"',
        'class="absolute top-20 left-0 w-64 bg-[#1a1a1a]/80 shadow-xl border border-gray-700 opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-300 z-50 rounded-b-xl backdrop-blur-sm"'
    ),
    # Contacts Dropdown - same as About Us usually, but let's be safe
    # Also ensuring text colors in dropdowns are readable (light) since background is dark.
    # The links in index.html might still be using dark text or brand-card/10 hover.
    
    # Update Link Styles in Dropdowns
    (
        'class="px-6 py-3 text-white/70 hover:brand-card/10 hover:text-gold-500 block font-medium"',
        'class="px-6 py-3 text-gray-200 hover:bg-gray-800 hover:text-white block font-medium"'
    ),
    (
        'class="text-white/70 hover:text-gold-500 font-medium"',
        'class="text-gray-200 hover:text-white font-medium"'
    )
]

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

original_content = content
for old, new in replacements:
    content = content.replace(old, new)

if content != original_content:
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filepath}")
else:
    print(f"No changes for {filepath}")
