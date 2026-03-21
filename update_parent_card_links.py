import os
import json

# Load mapping
with open('services_data.json', 'r') as f:
    services = json.load(f)

# Title to filename map
title_to_file = {s["title"].strip(): s["filename"] for s in services}

pages = [
    "business-setup-licensing.html",
    "freezone-offshore.html",
    "visa-immigration.html",
    "pro-government.html",
    "corporate-admin.html",
    "office-business-support.html",
    "branding-expansion.html"
]

for page in pages:
    if not os.path.exists(page):
        print(f"Skipping {page} as it does not exist.")
        continue
        
    with open(page, 'r') as f:
        lines = f.readlines()
        
    modified = False
    for i, line in enumerate(lines):
        if '<h3 ' in line and '</h3>' in line:
            title = line.split('">')[1].split('</')[0].strip()
            title = title.replace('&amp;', '&')
            
            # In case title has HTML entities or spaces mismatch, let's normalize
            # Or just check if title matches exactly
            matched_filename = None
            if title in title_to_file:
                matched_filename = title_to_file[title]
            else:
                for k, v in title_to_file.items():
                    if k.lower() == title.lower() or k.replace('&', '&amp;') == title:
                        matched_filename = v
                        break
                        
            if matched_filename:
                # Look backwards for the card opening div
                div_idx = -1
                for j in range(i, max(-1, i-10), -1):
                    if '<div class="group bg-white' in lines[j] or '<a href=' in lines[j]:
                        div_idx = j
                        break
                
                if div_idx != -1:
                    # check if already an 'a' tag
                    if '<a href=' not in lines[div_idx]:
                        # Make it a link!
                        lines[div_idx] = lines[div_idx].replace('<div ', f'<a href="{matched_filename}" class="block " ')
                        
                        # Find the closing div 
                        # usually 2 lines down
                        for k in range(i, min(len(lines), i+10)):
                            if '</div>' in lines[k]:
                                lines[k] = lines[k].replace('</div>', '</a>', 1)
                                modified = True
                                break
                    else:
                         print(f"Skipping {title} in {page} as it's already an <a> tag.")
                else:
                    print(f"Warning: Did not find opening div for {title} in {page}")
            else:
                pass # print(f"Warning: Title not found in map: {title} in {page}")
                
    if modified:
        with open(page, 'w') as f:
            f.writelines(lines)
        print(f"Updated {page}")

print("Done linking cards.")
