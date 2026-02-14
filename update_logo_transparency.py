import os

directory = '/Users/jalaludheenok/development/Diplomate'

# Replacements
replacements = [
    # 1. Update Logo Globally (including 'logo.png' and 'Diplomat logo.png')
    ('assets/images/logo/logo.png', 'assets/images/logo/logo-white.png'),
    ('assets/images/logo/Diplomat logo.png', 'assets/images/logo/logo-white.png'),
    
    # 2. Update Dropdown Transparency (95% -> 80% approx, using /80 which is tailwind opacity or custom)
    # The existing code uses bg-[#1a1a1a]/95. We want bg-[#1a1a1a]/80.
    ('bg-[#1a1a1a]/95', 'bg-[#1a1a1a]/80'),
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
