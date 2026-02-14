import os

directory = '/Users/jalaludheenok/development/Diplomate'

# Same replacements as before but applied to all HTML files
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
    # Also handle the 'bg-[#1a1a1a]/95' case if any file was updated by previous scripts but not fully correct
    # We want everything at /80.
    ('bg-[#1a1a1a]/95', 'bg-[#1a1a1a]/80'),

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
]

for filename in os.listdir(directory):
    if filename.endswith(".html"):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        for old, new in replacements:
            content = content.replace(old, new)
        
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated {filename}")
        else:
            print(f"No changes for {filename}")
