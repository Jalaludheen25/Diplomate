#!/usr/bin/env python3
"""Remove all 'Our Simple Process' sections from HTML pages."""

import os
import re
import glob

project_dir = os.path.dirname(os.path.abspath(__file__))

# Find all HTML files
html_files = glob.glob(os.path.join(project_dir, '*.html'))

# Pattern to match the "Our Simple Process" / "Process Steps" section
# It often starts with <!-- Process Steps --> and contains "Our Simple Process" inside an h2 tag.
# We match `<section` until the `</section>` that contains "Our Simple Process".

# Using regex to find <section... > up to </section> containing "Our Simple Process"
pattern = re.compile(
    r'\n?\s*(?:<!-- Process Steps -->)?\s*\n?\s*<section[^>]*>.*?Our Simple Process.*?</section>',
    re.DOTALL
)

modified_count = 0
for filepath in html_files:
    filename = os.path.basename(filepath)
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'Our Simple Process' not in content:
        continue
    
    # Find and remove the process section(s)
    new_content = pattern.sub('', content)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        modified_count += 1
        print(f"✅ Removed 'Our Simple Process' from: {filename}")
    else:
        print(f"⚠️  Pattern not matched in: {filename} even though the text exists")

print(f"\n🎉 Done! Modified {modified_count} files.")
