#!/usr/bin/env python3
import requests
import xml.etree.ElementTree as ET
import subprocess
from urllib.parse import urlparse
from datetime import datetime

RSS = "https://news.google.com/rss?hl=en-US&gl=US&ceid=US:en"
print("Fetching...")
r = requests.get(RSS)
root = ET.fromstring(r.content)

items = []
for item in root.findall('.//item')[:8]:
    title_el = item.find('title')
    link_el = item.find('link')
    if title_el is not None and link_el is not None:
        t = title_el.text.strip()
        if t and 'Google News' not in t:
            if ' - ' in t:
                title, source = t.rsplit(' - ', 1)
            else:
                title, source = t, urlparse(link_el.text).netloc
            items.append((title.strip(), source.strip(), link_el.text))

print(f"Found {len(items)} headlines")


html = f'''<html><body><h1>Coffee News {datetime.now().strftime("%Y-%m-%d %H:%M")}</h1>

<style>body{{padding:20px;font-family:Arial;}}.a{{margin:20px 0;padding:15px;border:1px solid #ddd;}}</style>'''
for title, source, link in items:
    print(f"Original: {title}")
    result = subprocess.run(['ollama', 'run', 'llama3.1', f"Rewrite '{title}' as one factual summary sentence."], capture_output=True, text=True)
    summary = result.stdout.splitlines()[0].strip()
    print(summary)
    html += f'<div class="a"><b>{source}:</b> <a href="{link}">{summary}</a><br><small>{title}</small></div>'
    print("---")
html += '</body></html>'
with open('coffee.html', 'w') as f:
    f.write(html)
subprocess.Popen(['firefox', 'coffee.html'])





