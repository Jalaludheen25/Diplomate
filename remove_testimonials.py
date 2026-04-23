#!/usr/bin/env python3
"""Remove all 'Client Success Stories' testimonial sections from HTML pages."""

import os
import re
import glob

project_dir = os.path.dirname(os.path.abspath(__file__))

# Find all HTML files
html_files = glob.glob(os.path.join(project_dir, '*.html'))

# Pattern to match the testimonial section
# It starts with <!-- Testimonials --> or a section containing "Client Success Stories"
# and ends with </section>
# We need to match the entire <section> block that contains "Client Success Stories"

pattern = re.compile(
    r'\n?\s*(?:<!-- Testimonials -->)?\s*\n?\s*<section[^>]*>.*?Client Success Stories.*?</section>',
    re.DOTALL
)

modified_count = 0
for filepath in html_files:
    filename = os.path.basename(filepath)
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'Client Success Stories' not in content:
        continue
    
    # Find and remove the testimonial section(s)
    new_content = pattern.sub('', content)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        modified_count += 1
        print(f"✅ Removed testimonials from: {filename}")
    else:
        print(f"⚠️  Pattern not matched in: {filename}")

print(f"\n🎉 Done! Modified {modified_count} files.")
