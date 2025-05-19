from flask import Flask, render_template
import docutils.core
import os
from datetime import datetime

app = Flask(__name__)

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

@app.route('/')
def home():
    return render_template('index.html',
                         content=get_content('index.rst'),
                         current_year=datetime.now().year)

@app.route('/publications')
def publications():
    return render_template('publications.html',
                         content=get_content('publications.rst'),
                         current_year=datetime.now().year)

@app.route('/experience')
def experience():
    return render_template('experience.html',
                         content=get_content('experience.rst'),
                         current_year=datetime.now().year)

if __name__ == '__main__':
    app.run(debug=True) 
