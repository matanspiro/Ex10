from flask import Blueprint, render_template

# base blueprint definition
base = Blueprint('base', __name__, static_folder='static', static_url_path='/base', template_folder='templates')
