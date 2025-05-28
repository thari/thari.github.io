import os
import shutil
from flask import Flask, render_template
import docutils.core
from datetime import datetime

app = Flask(__name__)
# Configure Flask for URL generation
app.config.update(
    SERVER_NAME='localhost',
    APPLICATION_ROOT='/',
    PREFERRED_URL_SCHEME='http'
)

def rst_to_html(rst_content):
    """Convert RST content to HTML."""
    overrides = {
        'input_encoding': 'unicode',
        'output_encoding': 'unicode',
        'report_level': 5,  # Suppress all messages
        'halt_level': 5,    # Don't halt on any level
    }
    return docutils.core.publish_string(
        source=rst_content,
        writer_name='html',
        settings_overrides=overrides
    )

def get_content(filename):
    """Read and convert RST content from file."""
    with open(os.path.join('content', filename), 'r', encoding='utf-8') as f:
        return rst_to_html(f.read())

def build_page(template, content_file, output_file):
    """Build a single page."""
    with app.app_context():
        content = get_content(content_file)
        html = render_template(template,
                             content=content,
                             current_year=datetime.now().year)
        
        # Ensure the directory exists
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html)

def main():
    # Create output directory
    if os.path.exists('_site'):
        shutil.rmtree('_site')
    os.makedirs('_site')

    # Build pages
    build_page('index.html', 'index.rst', '_site/index.html')
    build_page('publications.html', 'publications.rst', '_site/publications/index.html')
    build_page('experience.html', 'experience.rst', '_site/experience/index.html')

    # Copy static files
    if os.path.exists('static'):
        shutil.copytree('static', '_site/static', dirs_exist_ok=True)
        print("Static files copied successfully")
    else:
        print("Warning: static directory not found")

if __name__ == '__main__':
    main() 
