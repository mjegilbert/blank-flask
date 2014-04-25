import fnmatch
import os
import subprocess

from flask.ext.assets import Bundle
import project.lib.constants as c
from webassets.filter import (
    Filter,
    register_filter
    )

HAML_PATH = os.path.join(os.path.dirname(__file__),'static','haml')
HAML_OUT_PATH = os.path.join(os.path.dirname(__file__),'static','gen','_templates.js')
HAML_CMD = "cd %s; haml-coffee -i . -n window.Templates -o %s" % (HAML_PATH, HAML_OUT_PATH)

class HamlCoffeeFilter(Filter):
    name = 'haml_coffee'

    def output(self, _in, out, **kwargs):
        subprocess.call(HAML_CMD, shell=True)
        with open(HAML_OUT_PATH, 'r') as f:
            out.write(f.read())

    def input(self, _in, out, **kwargs):
        out.write(_in.read())

register_filter(HamlCoffeeFilter)

if c.IS_PROD:
    js_filter = "jsmin"
    scss_output = "gen/application.%(version)s.scss"
    all_css_output = "gen/application.%(version)s.css"
    all_js_output = "gen/application.%(version)s.js"
    backbone_models_output = "gen/backbone_models.%(version)s.coffee"
    backbone_views_output = "gen/backbone_views.%(version)s.coffee"
    backbone_collections_output = "gen/backbone_collections.%(version)s.coffee"
    backbone_output = "gen/backbone.%(version)s.coffee"
    coffeescript_output = "gen/coffeescript.%(version)s.coffee"
    haml_output = "gen/templates.%(version)s.js"
else:
    js_filter = []
    scss_output = "gen/application.scss"
    all_css_output = "gen/application.css"
    all_js_output = "gen/application.js"
    backbone_models_output = "gen/backbone_models.coffee"
    backbone_views_output = "gen/backbone_views.coffee"
    backbone_collections_output = "gen/backbone_collections.coffee"
    backbone_output = "gen/backbone.coffee"
    coffeescript_output = "gen/coffeescript.coffee"
    haml_output = "gen/templates.js"

scss_all = Bundle(
    "scss/*.scss",
    filters="scss",
    output=scss_output)

css_all = Bundle(
    "css/*.css",
    scss_all,
    filters="cssutils",
    output=all_css_output)

haml_files = []
for root, dirnames, filenames in os.walk(HAML_PATH):
    for filename in fnmatch.filter(filenames, '*.haml'):
        print filename
        asset_path = os.path.join(root, filename)[len(HAML_PATH) - 4:]
        haml_files.append(asset_path)

haml = Bundle(
    *haml_files,
    filters='haml_coffee',
    output=haml_output)

backbone_models = Bundle(
    "coffee/backbone/models/base.coffee",
    output=backbone_models_output)

backbone_views = Bundle(
    "coffee/backbone/views/base.coffee",
    "coffee/backbone/views/home.coffee",
    output=backbone_views_output)

backbone_collections = Bundle(
    "coffee/backbone/collections/base.coffee",
    output=backbone_collections_output)

backbone = Bundle(
    "coffee/backbone/backbone.coffee",
    "coffee/backbone/router.coffee",
    backbone_models,
    backbone_views,
    backbone_collections,
    output=backbone_output)

coffeescript = Bundle(
    backbone,
    filters="coffeescript",
    output=coffeescript_output)

js_all = Bundle(
    "lib/jquery.min.js",
    "lib/jquery-ui.min.js",
    "lib/underscore.min.js",
    "lib/backbone.min.js",
    haml,
    coffeescript,
    filters=js_filter,
    output=all_js_output)
