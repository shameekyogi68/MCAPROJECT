import os
import re
from nicegui import ui

# Resolve the absolute path to index.html
current_dir = os.path.dirname(os.path.abspath(__file__))
index_path = os.path.join(current_dir, 'index.html')

try:
    with open(index_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
except Exception as e:
    html_content = f"<h1>Error loading index.html: {str(e)}</h1>"

# Extract the inner contents of <head> and <body>
head_match = re.search(r'<head>(.*?)</head>', html_content, re.DOTALL)
body_match = re.search(r'<body.*?>(.*?)</body>', html_content, re.DOTALL)

# Inject the head elements (custom styles, fonts, etc.)
if head_match:
    ui.add_head_html(head_match.group(1), shared=True)

@ui.page('/')
def index():
    # Remove default NiceGUI padding and layout constraints to match raw HTML exactly
    ui.query('.nicegui-content').classes('p-0 m-0 gap-0 w-full min-h-screen bg-[#020205]')
    
    # Render the full body HTML content
    if body_match:
        ui.html(body_match.group(1))
    else:
        ui.html("<h1>Error parsing body content from index.html</h1>")

# Run the local NiceGUI dev server
ui.run(port=8550, host="127.0.0.1", show=False)
