import glob
import re

html_files = glob.glob('*.html')

style_injection = """
    <style>
        /* Apple-style Scroll Animation */
        .reveal {
            opacity: 0;
            transform: translateY(40px);
            transition: all 0.8s cubic-bezier(0.25, 0.46, 0.45, 0.94);
        }
        .reveal.active {
            opacity: 1;
            transform: translateY(0);
        }
        .reveal-delay-1 { transition-delay: 0.1s; }
        .reveal-delay-2 { transition-delay: 0.2s; }
        .reveal-delay-3 { transition-delay: 0.3s; }
    </style>
"""

script_injection = """
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const reveals = document.querySelectorAll('.reveal');
            
            const revealOptions = {
                threshold: 0.15,
                rootMargin: "0px 0px -50px 0px"
            };

            const revealOnScroll = new IntersectionObserver(function(entries, observer) {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        entry.target.classList.add('active');
                        observer.unobserve(entry.target); // Trigger only once
                    }
                });
            }, revealOptions);

            reveals.forEach(reveal => {
                revealOnScroll.observe(reveal);
            });
        });
    </script>
</body>
"""

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Inject CSS before </head> if not already there
    if ".reveal {" not in content:
        content = content.replace('</head>', style_injection + '</head>')
        
    # Inject JS before </body> if not already there
    if "const reveals = document.querySelectorAll('.reveal');" not in content:
        content = content.replace('</body>', script_injection)
        
    # Add .reveal class to key structural elements
    # <section ...> -> <section ... class="... reveal">
    # We will carefully inject 'reveal' into class attributes of sections and main headers
    
    # Simple regex to add 'reveal' to section and header tags that already have a class
    content = re.sub(r'<section([^>]*)class="([^"]*)"', r'<section\1class="\2 reveal"', content)
    content = re.sub(r'<header([^>]*)class="([^"]*)"', r'<header\1class="\2 reveal"', content)
    
    # Also target the main cards in case studies (div with bg-[#0F1626])
    content = content.replace('class="bg-[#0F1626] rounded-xl shadow-[0_0_15px_rgba(0,229,255,0.2)]', 'class="bg-[#0F1626] rounded-xl shadow-[0_0_15px_rgba(0,229,255,0.2)] reveal')
    
    # And the 6 pillars in join.html
    content = content.replace('class="flex flex-col md:flex-row items-center gap-10"', 'class="flex flex-col md:flex-row items-center gap-10 reveal"')
    content = content.replace('class="flex flex-col md:flex-row-reverse items-center gap-10"', 'class="flex flex-col md:flex-row-reverse items-center gap-10 reveal"')
    
    # And the forms/surveys
    content = content.replace('class="bg-[#080D1A] border border-white/10 rounded-2xl p-8 shadow-[0_0_15px_rgba(0,229,255,0.2)] text-center"', 'class="bg-[#080D1A] border border-white/10 rounded-2xl p-8 shadow-[0_0_15px_rgba(0,229,255,0.2)] text-center reveal"')

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Apple-style scroll animations applied to all HTML files.")
