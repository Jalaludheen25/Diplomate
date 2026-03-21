#!/usr/bin/env python3
import json
import os

with open('services_data.json', 'r') as f:
    services = json.load(f)

with open('golden-visa.html', 'r') as f:
    content = f.read()

# Fix the NAV extraction
nav_start = content.find('<nav id="navbar"')
# Find the exact end of the main navbar
hero_start = content.find('<!-- Hero Section -->')
# Look back from hero_start to find the ending </nav>
nav_end_idx = content.rfind('</nav>', nav_start, hero_start) + len('</nav>')
NAV = content[nav_start:nav_end_idx]

footer_start = content.find('<footer')
footer_end = content.find('</footer>') + len('</footer>')
FOOTER = content[footer_start:footer_end]

SCRIPT_TAG = '    <script src="script.js?v=20260112"></script>'

def generate_page(s):
    color = s.get("color", "indigo")
    reqs_html = ""
    for r in s.get("requirements", []):
        reqs_html += f'''                        <li class="flex items-start gap-3">
                            <svg class="w-5 h-5 text-{color}-600 mt-0.5 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg>
                            <span class="text-gray-600">{r}</span>
                        </li>\n'''

    steps_html = ""
    total_steps = len(s.get("steps", []))
    for i, st in enumerate(s.get("steps", []), 1):
        line_html = '<div class="absolute left-5 top-10 bottom-0 w-0.5 bg-gray-200"></div>' if i < total_steps else ''
        steps_html += f'''                        <div class="relative pl-14 pb-8 last:pb-0">
                            <!-- Line -->
                            {line_html}
                            <!-- Circle -->
                            <div class="absolute left-0 top-0 w-10 h-10 bg-gradient-to-br from-{color}-500 to-{color}-600 rounded-xl flex items-center justify-center text-white font-bold shadow-md z-10">{i}</div>
                            <!-- Content -->
                            <div class="bg-white p-6 rounded-2xl shadow-sm border border-gray-100 hover:shadow-md transition-shadow">
                                <h4 class="font-bold text-navy-900 mb-2">{st["title"]}</h4>
                                <p class="text-sm text-gray-500 leading-relaxed">{st["desc"]}</p>
                            </div>
                        </div>\n'''

    color = s.get("color", "indigo")
    parent_link = s.get("parent_link", "services.html")
    parent_name = s.get("parent_name", "Services")
    img = s.get("image", "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?auto=format&fit=crop&q=80&w=2000")
    
    html = f'''<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{s["title"]} | Diplomat Dubai</title>
    <meta name="description" content="{s.get('meta', 'Comprehensive ' + s["title"] + ' services in Dubai.')}">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Outfit:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {{
            theme: {{
                extend: {{
                    colors: {{
                        navy: {{ 900: '#0f172a', 800: '#1e293b' }},
                        indigo: {{ 700: '#4338ca' }},
                        gold: {{ 500: '#d4af37' }},
                        offwhite: {{ 50: '#f9fafb' }}
                    }},
                    fontFamily: {{
                        sans: ['Inter', 'sans-serif'],
                        heading: ['Outfit', 'sans-serif'],
                    }}
                }}
            }}
        }}
    </script>
    <link rel="stylesheet" href="styles.css">
</head>
<body class="bg-white font-sans text-gray-900 overflow-x-hidden">
    {NAV}

    <!-- Hero -->
    <section class="relative pt-24 pb-16 lg:pt-32 lg:pb-24 overflow-hidden">
        <div class="absolute inset-0 z-0">
            <div class="absolute inset-0 bg-gradient-to-r from-navy-900/90 to-{color}-700/80 z-10"></div>
            <img src="{img}" class="w-full h-full object-cover" alt="{s["title"]}">
        </div>
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
            <div class="max-w-3xl">
                <nav class="flex items-center space-x-2 text-sm text-gray-300 mb-6 mt-10">
                    <a href="index.html" class="hover:text-white">Home</a>
                    <span>/</span>
                    <a href="{parent_link}" class="hover:text-white">{parent_name}</a>
                    <span>/</span>
                    <span class="text-gold-500">{s["title"]}</span>
                </nav>
                <h1 class="text-4xl lg:text-5xl font-heading font-bold text-white mb-6 leading-tight">{s["title"]}</h1>
                <p class="text-lg text-gray-200 mb-8 leading-relaxed max-w-2xl">{s.get('hero_desc', 'Expert assistance for all your business needs.')}</p>
                <div class="flex flex-col sm:flex-row gap-4">
                    <a href="contact.html" class="bg-gold-500 text-navy-900 px-8 py-4 rounded-full font-bold text-sm tracking-widest hover:bg-white transition-all shadow-xl text-center">GET STARTED</a>
                    <a href="https://wa.me/971508878699" target="_blank" class="border-2 border-white text-white px-8 py-4 rounded-full font-bold text-sm tracking-widest hover:bg-white hover:text-navy-900 transition-all text-center">WHATSAPP US</a>
                </div>
            </div>
        </div>
        <div class="absolute bottom-0 left-0 w-full h-20 bg-gradient-to-t from-white to-transparent"></div>
    </section>

    <!-- About -->
    <section class="py-20 bg-white">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="grid lg:grid-cols-2 gap-16 items-center">
                <div>
                    <span class="inline-block px-4 py-1.5 rounded-full bg-{color}-50 text-{color}-700 text-xs font-bold uppercase tracking-widest mb-4">Overview</span>
                    <h2 class="text-3xl md:text-4xl font-heading font-bold text-navy-900 mb-6">{s.get("about_title", "About This Service")}</h2>
                    <p class="text-gray-600 leading-relaxed mb-6">{s.get("about_desc", "We provide comprehensive solutions tailored to your specific requirements, ensuring seamless and efficient processing.")}</p>
                </div>
                <div class="rounded-2xl overflow-hidden shadow-2xl">
                    <img src="{s.get("image2", img)}" alt="{s["title"]}" class="w-full h-80 object-cover">
                </div>
            </div>
        </div>
    </section>

    <!-- Requirements & Process -->
    <section class="py-24 bg-gradient-to-br from-gray-50 via-white to-{color}-50/30">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="text-center mb-16">
                <h2 class="text-3xl md:text-5xl font-heading font-bold text-navy-900 mb-4">Requirements & Process</h2>
                <div class="w-24 h-1.5 bg-gradient-to-r from-{color}-700 to-gold-500 mx-auto rounded-full"></div>
                <p class="text-gray-500 mt-6 max-w-2xl mx-auto text-lg">Everything you need to know and the steps we take to ensure your success.</p>
            </div>
            
            <div class="grid lg:grid-cols-2 gap-16">
                <!-- Requirements List -->
                <div class="bg-white rounded-3xl shadow-xl p-8 lg:p-10 border border-gray-100 h-fit lg:sticky lg:top-24">
                    <h3 class="text-2xl font-bold text-navy-900 mb-8 flex items-center gap-3">
                        <span class="w-10 h-10 rounded-lg bg-{color}-50 text-{color}-600 flex items-center justify-center">
                            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                        </span>
                        Key Requirements
                    </h3>
                    <ul class="space-y-5">
{reqs_html}                    </ul>
                </div>
                
                <!-- Process Steps -->
                <div>
                    <h3 class="text-2xl font-bold text-navy-900 mb-8 flex items-center gap-3">
                        <span class="w-10 h-10 rounded-lg bg-gold-50 text-gold-600 flex items-center justify-center">
                            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"/></svg>
                        </span>
                        How It Works
                    </h3>
                    <div class="space-y-0 relative">
{steps_html}                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- CTA -->
    <section class="py-20 bg-gradient-to-br from-navy-900 via-indigo-900 to-navy-900 relative overflow-hidden">
        <div class="absolute inset-0 opacity-10">
            <div class="absolute top-10 left-10 w-72 h-72 bg-gold-500 rounded-full blur-3xl"></div>
            <div class="absolute bottom-10 right-10 w-96 h-96 bg-indigo-500 rounded-full blur-3xl"></div>
        </div>
        <div class="max-w-4xl mx-auto px-4 text-center relative z-10">
            <h2 class="text-3xl lg:text-4xl font-heading font-bold text-white mb-6">Ready to Get Started?</h2>
            <p class="text-lg text-gray-300 mb-10 max-w-2xl mx-auto">Contact our expert team for a free consultation and let us handle the process for you.</p>
            <div class="flex flex-col sm:flex-row gap-4 justify-center">
                <a href="contact.html" class="bg-gold-500 text-navy-900 px-10 py-4 rounded-full font-bold tracking-wider hover:bg-white transition-all shadow-2xl">CONTACT US</a>
                <a href="https://wa.me/971508878699" target="_blank" class="border-2 border-white text-white px-10 py-4 rounded-full font-bold tracking-wider hover:bg-white hover:text-navy-900 transition-all">WHATSAPP</a>
            </div>
        </div>
    </section>

    {FOOTER}

{SCRIPT_TAG}
</body>
</html>'''
    return html

count = 0
for s in services:
    filename = s["filename"]
    html = generate_page(s)
    with open(filename, 'w') as f:
        f.write(html)
    count += 1

print(f"Done! Successfully generated {count} pages.")
