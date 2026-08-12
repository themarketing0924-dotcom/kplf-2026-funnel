import os
import re
import glob

# Mapping of light theme / gold classes to luxury dark / cyan classes
replacements = [
    # Global body
    (r'<body class="bg-gray-50 text-gray-900 font-sans antialiased">', r'<body class="bg-[#050B14] text-gray-300 font-sans antialiased selection:bg-[#00E5FF] selection:text-black">'),
    (r'<body class="bg-gray-100 text-gray-900 font-sans antialiased">', r'<body class="bg-[#050B14] text-gray-300 font-sans antialiased selection:bg-[#00E5FF] selection:text-black">'),
    
    # Backgrounds
    (r'bg-white', r'bg-[#0F1626] border border-white/10'), # Cards
    (r'bg-gray-50', r'bg-[#080D1A]'),
    (r'bg-gray-100', r'bg-[#121A2F]'),
    (r'bg-gray-200', r'bg-[#1E293B]'),
    (r'bg-navy', r'bg-[#030712]'),
    (r'bg-yellow-50/50', r'bg-[#00E5FF]/5'),
    
    # Text colors
    (r'text-gray-900', r'text-white'),
    (r'text-gray-800', r'text-gray-100'),
    (r'text-gray-700', r'text-gray-300'),
    (r'text-gray-600', r'text-gray-400'),
    (r'text-black', r'text-[#050B14]'),
    
    # Brand colors (Gold -> Neon Cyan)
    (r'text-gold', r'text-[#00E5FF] drop-shadow-[0_0_8px_rgba(0,229,255,0.5)]'),
    (r'text-red-600', r'text-[#FF3366]'),
    (r'bg-gold', r'bg-gradient-to-r from-[#00E5FF] to-[#0088FF] text-white shadow-[0_0_20px_rgba(0,229,255,0.4)]'),
    (r'hover:bg-yellow-600', r'hover:from-[#00BFFF] hover:to-[#0077FF]'),
    (r'bg-red-600', r'bg-[#FF3366]'),
    
    # Borders
    (r'border-gold', r'border-[#00E5FF]'),
    (r'border-gray-200', r'border-white/10'),
    (r'border-gray-100', r'border-white/5'),
    
    # Forms & Inputs
    (r'border rounded', r'border-white/20 bg-[#0B1120] text-white rounded'),
]

html_files = glob.glob('*.html')

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    for old, new in replacements:
        content = re.sub(old, new, content)
        
    # Inject glow styles in the head
    style_block = """    <style>
        body { font-family: 'Pretendard', sans-serif; background-color: #050B14; }
        .glass-panel { background: rgba(15, 22, 38, 0.7); backdrop-filter: blur(12px); border: 1px solid rgba(255, 255, 255, 0.1); }
        .neon-text { color: #00E5FF; text-shadow: 0 0 10px rgba(0, 229, 255, 0.5); }
    </style>"""
    
    content = re.sub(r'<style>.*?</style>', style_block, content, flags=re.DOTALL)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Luxury Dark Theme applied to all HTML files.")
