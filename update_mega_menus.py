import os

filepath = '/Users/jalaludheenok/development/Diplomate/index.html'

replacements = [
    # 1. Update Dropdown Containers (Business Setup & Services)
    # They use 'w-full brand-card'
    (
        'class="absolute top-20 left-0 w-full brand-card shadow-2xl border-t border-gray-100 opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-300 z-50 overflow-hidden"',
        'class="absolute top-20 left-0 w-full bg-[#1a1a1a]/80 shadow-2xl border-t border-gray-700 opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-300 z-50 overflow-hidden backdrop-blur-sm"'
    ),
    (
        'class="absolute top-20 left-0 w-full brand-card shadow-2xl border-t border-gray-100 opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-300 z-50"',
        'class="absolute top-20 left-0 w-full bg-[#1a1a1a]/80 shadow-2xl border-t border-gray-700 opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-300 z-50 backdrop-blur-sm"'
    ),

    # 2. Update Link Colors in these Mega Menus
    # Current: text-white/70 hover:text-gold-500 font-medium
    # New: text-gray-200 hover:text-white font-medium
    (
        'class="text-white/70 hover:text-gold-500 font-medium"',
        'class="text-gray-200 hover:text-white font-medium"'
    ),
    (
        'class="text-white/70 hover:text-gold-500 font-medium transition-colors"',
        'class="text-gray-200 hover:text-white font-medium transition-colors"'
    ),
    
    # 3. Update Headings in Mega Menus (keep gold or make white? "about" headings are white or gold.
    # In About dropdown, there are no headings, just links.
    # In Services/Business Setup, there are headings.
    # Current: h4 class="text-gold-500 ..." -> Keep Gold for hierarchy.
    
    # 4. Update "Hey, we're Diplomate" text color if needed.
    # It has text-white, which is fine on dark background.
    
    # 5. Update "Explore All Solutions" button if needed.
    # class="btn-indigo-small" -> might need check.
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
