import os

directory = '/Users/jalaludheenok/development/Diplomate'

# The main missing piece is the header background color which might have varied formatting.
# We will globally replace the blue color code with the black color code.
# We also check for any remaining instances of the old dropdown classes just in case.

replacements = [
    # Global Color Replacement (covers Header and any missed Mobile Menu)
    ('bg-[#1a5492]', 'bg-[#1a1a1a]'),
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
