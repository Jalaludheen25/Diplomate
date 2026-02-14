import os

directory = '/Users/jalaludheenok/development/Diplomate'

# Replacements specific to services.html or any file using 'brand-card' for dropdowns
replacements = [
    # Dropdown container
    (
        'class="absolute top-20 left-0 w-64 brand-card shadow-xl border border-gray-100 opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-300 z-50 rounded-b-xl"',
        'class="absolute top-20 left-0 w-64 bg-[#1a1a1a]/95 shadow-xl border border-gray-700 opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-300 z-50 rounded-b-xl backdrop-blur-sm"'
    ),
    # Dropdown Links
    (
        'class="px-6 py-3 text-white/70 hover:brand-card/10 hover:text-gold-500 block font-medium"',
        'class="px-6 py-3 text-gray-200 hover:bg-gray-800 hover:text-white block font-medium"'
    )
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
