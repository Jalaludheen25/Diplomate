#!/usr/bin/env python3
import json
import re

with open('services_data.json', 'r') as f:
    services = json.load(f)

with open('index.html', 'r') as f:
    html = f.read()

# Create lookup dict: title -> filename
service_map = {s["title"].strip(): s["filename"] for s in services}

# 1. Update Card Headers (h3 -> a wrapped h3)
header_links = {
    "Business Setup & Licensing": "business-setup-licensing.html",
    "Free Zone & Offshore Services": "freezone-offshore.html",
    "Visa & Immigration Services": "visa-immigration.html",
    "PRO & Government Services": "pro-government.html",
    "Corporate & Administrative Services": "corporate-admin.html",
    "Office & Business Support": "office-business-support.html",
    "Branding & Expansion Support": "branding-expansion.html"
}

for title, link in header_links.items():
    old_h3 = f'<h3 class="text-xl font-bold text-navy-900 mb-4">{title}</h3>'
    new_h3 = f'<a href="{link}" class="hover:text-gold-500 transition-colors block"><h3 class="text-xl font-bold text-navy-900 mb-4 hover:text-gold-500 transition-colors">{title}</h3></a>'
    html = html.replace(old_h3, new_h3)

# 2. Update all <li> items to wrap the text in an <a> tag
# Example: <li class="..."><span class="...">•</span>New Company Incorporation</li>
# Becomes: <li class="..."><span class="...">•</span><a href="..." class="hover:text-gold-500 transition-colors">New Company Incorporation</a></li>

for service_title, filename in service_map.items():
    # Use regex to find the exact list item
    pattern = rf'(<span[^>]*>•</span>)\s*({re.escape(service_title)})\s*</li>'
    replacement = rf'\1<a href="{filename}" class="hover:text-gold-500 transition-colors">\2</a></li>'
    html = re.sub(pattern, replacement, html)

# For existing mapped services not in JSON (e.g. Accounting & Bookkeeping -> accounting-tax.html)
extra_mappings = {
    "Free Zone License Setup": "freezone-setup.html",
    "Free Zone Visa Services": "visa-services.html",
    "Golden Visa Assistance": "golden-visa.html",
    "Corporate Bank Account Opening": "bank-account-opening.html",
    "Accounting & Bookkeeping": "accounting-tax.html",
    "Payroll Management": "payroll-management.html",
    "Reception & Call Handling": "virtual-receptionist.html",
    "Mail Handling Services": "mail-management.html",
    "Trademark Registration": "trademark-registration.html"
}
for service_title, filename in extra_mappings.items():
    pattern = rf'(<span[^>]*>•</span>)\s*({re.escape(service_title)})\s*</li>'
    replacement = rf'\1<a href="{filename}" class="hover:text-gold-500 transition-colors">\2</a></li>'
    html = re.sub(pattern, replacement, html)

with open('index.html', 'w') as f:
    f.write(html)

print("Updated index.html with links successfully!")
