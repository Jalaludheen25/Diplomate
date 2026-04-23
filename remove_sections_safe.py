#!/usr/bin/env python3
"""
Safely remove 'Client Success Stories' and 'Our Simple Process' sections
from all HTML pages. Uses a non-greedy, nested-section-aware approach.
"""

import os
import glob
import re

project_dir = os.path.dirname(os.path.abspath(__file__))
html_files = glob.glob(os.path.join(project_dir, '*.html'))

def find_section_containing(content, marker_text):
    """Find the <section>...</section> block that contains marker_text.
    Handles nested sections by counting open/close tags."""
    
    # Find the marker text position
    marker_pos = content.find(marker_text)
    if marker_pos == -1:
        return None, None
    
    # Walk backwards to find the opening <section tag for this marker
    # We need to find the section that directly contains this marker
    search_pos = marker_pos
    section_start = -1
    
    while search_pos >= 0:
        # Find the last <section before our marker
        idx = content.rfind('<section', 0, search_pos)
        if idx == -1:
            return None, None
        
        # Count section opens and closes between this <section and the marker
        between = content[idx:marker_pos]
        opens = len(re.findall(r'<section\b', between))
        closes = len(re.findall(r'</section>', between))
        
        # If opens > closes, this is a parent section of our marker
        if opens > closes:
            section_start = idx
            break
        
        search_pos = idx - 1
    
    if section_start == -1:
        return None, None
    
    # Now find the matching </section> by counting nested sections
    depth = 0
    pos = section_start
    while pos < len(content):
        open_match = re.search(r'<section\b', content[pos:])
        close_match = re.search(r'</section>', content[pos:])
        
        if open_match is None and close_match is None:
            break
        
        open_pos = pos + open_match.start() if open_match else float('inf')
        close_pos = pos + close_match.start() if close_match else float('inf')
        
        if open_pos < close_pos:
            depth += 1
            pos = open_pos + 1
        else:
            depth -= 1
            if depth == 0:
                section_end = close_pos + len('</section>')
                return section_start, section_end
            pos = close_pos + 1
    
    return None, None


def remove_section(content, marker_text):
    """Remove the section containing marker_text, including any preceding HTML comment."""
    start, end = find_section_containing(content, marker_text)
    if start is None:
        return content, False
    
    # Also remove any preceding comment like <!-- Testimonials --> or <!-- Process Steps -->
    # and whitespace/newlines before the section
    pre = content[:start]
    # Strip trailing whitespace and optional HTML comment
    pre_stripped = re.sub(r'\s*(?:<!--[^>]*-->\s*)*$', '', pre)
    
    # Strip leading whitespace after the section
    post = content[end:]
    post_stripped = post.lstrip('\n')
    
    return pre_stripped + '\n\n' + post_stripped, True


modified_files = {}

for filepath in html_files:
    filename = os.path.basename(filepath)
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    changes = []
    
    # Remove "Client Success Stories" section
    if 'Client Success Stories' in content:
        content, removed = remove_section(content, 'Client Success Stories')
        if removed:
            changes.append('testimonials')
    
    # Remove "Our Simple Process" section
    if 'Our Simple Process' in content:
        content, removed = remove_section(content, 'Our Simple Process')
        if removed:
            changes.append('process steps')
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        modified_files[filename] = changes
        print(f"✅ {filename}: removed {', '.join(changes)}")

print(f"\n🎉 Done! Modified {len(modified_files)} files.")
if modified_files:
    print("\nSummary:")
    for f, c in sorted(modified_files.items()):
        print(f"  - {f}: {', '.join(c)}")
