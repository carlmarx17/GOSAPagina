import json
import os
from html.parser import HTMLParser

class TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text = []
        self.script_style = False

    def handle_starttag(self, tag, attrs):
        if tag in ('script', 'style'):
            self.script_style = True

    def handle_endtag(self, tag):
        if tag in ('script', 'style'):
            self.script_style = False

    def handle_data(self, data):
        if not self.script_style:
            cleaned = data.strip()
            if cleaned:
                self.text.append(cleaned)

def extract_from_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            html = f.read()
        parser = TextExtractor()
        parser.feed(html)
        return '\n'.join(parser.text)
    except Exception as e:
        return str(e)

base_dir = 'oangosa2012.wixsite.com/gosa'
files = [
    'acerca-de-gosa.html',
    'divulgacion.html',
    'eventos.html',
    'integrantes.html',
    'publicaciones.html',
    'tesis.html',
    'áreas-de-investigación.html',
    'en.html'
]

result = {}
for file in files:
    path = os.path.join(base_dir, file)
    if os.path.exists(path):
        result[file] = extract_from_file(path)
    
with open('extracted_all.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, indent=2, ensure_ascii=False)
