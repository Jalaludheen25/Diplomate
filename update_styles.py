import os

directory = '/Users/jalaludheenok/development/Diplomate'

replacements = [
    # 1. Header Background
    (
        'nav id="navbar" class="fixed top-0 w-full z-50 transition-all duration-300 bg-[#1a5492] shadow-md "',
        'nav id="navbar" class="fixed top-0 w-full z-50 transition-all duration-300 bg-[#1a1a1a] shadow-md "'
    ),
    # 2. Dropdown Container Background (General for About and Contact)
    (
        'class="absolute top-20 left-0 w-64 bg-white shadow-xl border border-gray-100 opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-300 z-50 rounded-b-xl"',
        'class="absolute top-20 left-0 w-64 bg-[#1a1a1a]/95 shadow-xl border border-gray-700 opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-300 z-50 rounded-b-xl backdrop-blur-sm"'
    ),
    # 3. Dropdown Links Text Color & Hover (General Pattern)
    (
        'class="px-6 py-3 text-gray-600 hover:bg-offwhite-50 hover:text-indigo-700 block font-medium"',
        'class="px-6 py-3 text-gray-200 hover:bg-gray-800 hover:text-white block font-medium"'
    ),
    # 4. Mobile Menu Background
    (
        'id="mobile-menu"\n            class="fixed inset-y-0 right-0 w-80 bg-[#1a5492] shadow-2xl',
        'id="mobile-menu"\n            class="fixed inset-y-0 right-0 w-80 bg-[#1a1a1a] shadow-2xl'
    )
]

for filename in os.listdir(directory):
    if filename.endswith(".html") and filename != "index.html": # index.html is already done
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
