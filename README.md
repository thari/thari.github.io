# Dr. Hariharan Thiagarajan's Personal Website

This is a personal website built with Flask and reStructuredText for easy content management.

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Unix/macOS
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the development server:
```bash
python app.py
```

## Content Management

The website content is managed through reStructuredText (RST) files in the `content` directory. To update content:

1. Edit the corresponding RST file in the `content` directory
2. The changes will be automatically reflected on the website

## Structure

- `app.py`: Main Flask application
- `content/`: RST content files
- `templates/`: HTML templates
- `static/`: Static files (CSS, images, etc.) 
