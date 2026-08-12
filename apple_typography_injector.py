import glob
import re

html_files = glob.glob('*.html')

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update Body & Fonts for Apple feel (SF Pro / Pretendard) + Antialiased + Tracking tight
    content = content.replace("font-family: 'Pretendard', sans-serif;", "font-family: -apple-system, BlinkMacSystemFont, 'Apple SD Gothic Neo', 'Pretendard', sans-serif; letter-spacing: -0.02em; word-break: keep-all;")
    
    # 2. Make all text elements centered and responsive
    # Headers H1
    content = re.sub(r'<h1([^>]*)class="([^"]*)"', r'<h1\1class="\2 text-center mx-auto tracking-tighter leading-tight md:leading-tight lg:leading-tight"', content)
    # Make sure text sizes are responsive: mobile smaller, desktop huge
    content = content.replace('text-3xl md:text-5xl', 'text-4xl md:text-6xl lg:text-7xl')
    content = content.replace('text-4xl md:text-6xl', 'text-4xl md:text-6xl lg:text-7xl')

    # Headers H2
    content = re.sub(r'<h2([^>]*)class="([^"]*)"', r'<h2\1class="\2 text-center mx-auto tracking-tight leading-snug md:leading-snug"', content)
    content = content.replace('text-3xl md:text-4xl', 'text-3xl md:text-5xl lg:text-6xl')
    
    # Paragraphs - center them and constrain width for readability like Apple
    content = re.sub(r'<p([^>]*)class="([^"]*)"', r'<p\1class="\2 text-center mx-auto max-w-3xl leading-relaxed md:leading-loose"', content)
    # If it's already centered, we might duplicate text-center, but Tailwind handles duplicates fine.
    
    # Update Grid layouts for Mobile/iPad/Desktop
    # Cards grid
    content = content.replace('grid md:grid-cols-2 lg:grid-cols-3', 'grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3')
    
    # 3. Clean up any weird alignments in lists or cards to make them centered
    content = content.replace('text-left', 'text-center')
    
    # Button alignment
    content = content.replace('flex-col md:flex-row items-center', 'flex-col md:flex-row items-center justify-center')
    content = content.replace('text-left space-y-6', 'text-center space-y-6 max-w-2xl mx-auto')

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Apple-style typography, spacing, and centered alignment applied across mobile, iPad, and desktop.")
