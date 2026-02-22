import re
with open('/home/carlmarxt/Documents/gosa_clon/website/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

with open('/home/carlmarxt/Documents/gosa_clon/members.html', 'r', encoding='utf-8') as f:
    members = f.read()

# Replace the team section content
pattern = r'<h3 class="subsection-title">Directores e Investigadores Principales</h3>.*?</section>'
replacement = members + '\n            </div>\n        </section>'
new_html = re.sub(pattern, replacement, html, flags=re.DOTALL)

with open('/home/carlmarxt/Documents/gosa_clon/website/index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)
