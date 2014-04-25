import json
from flask import render_template

def home():
    return render_template('base.jinja2',
        data=json.dumps({})
    )
