import os

# Project root path
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Path to icon app
ICON_PATH = os.path.join(BASE_DIR, 'files/static/icon.ico')

# Path to last_connection.json file
JSON_PATH = os.path.join(BASE_DIR, 'files/connection/last_connection.json')

# Background colors
BG_GRAY = '#F0F0F0'
BG_WHITE = '#FFFFFF'

# Font styles
FONT_TITLE = ('Open Sans', 14, 'bold')
FONT_LABEL = ('Open Sans', 12, 'normal')
FONT_ENTRY = ('Open Sans', 10, 'normal')
FONT_TEXT = ('Open Sans', 12, 'normal')