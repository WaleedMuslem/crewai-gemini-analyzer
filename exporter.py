# exporter.py
import markdown2

def save_markdown(text, filename='output.md'):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)

def convert_markdown_to_html(md_file, html_file='output.html'):
    with open(md_file, 'r', encoding='utf-8') as f:
        html = markdown2.markdown(f.read())
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html)
