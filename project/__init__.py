from flask import Flask
from flask.ext.assets import Bundle, Environment, ManageAssets
from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.script import Manager
from flask.ext.sqlalchemy import SQLAlchemy
from webassets.loaders import PythonLoader

import project.asset_bundles

app = Flask(__name__)
app.config.from_object('project.config')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

import routes
# from models import *

assets = Environment(app)
assets.versions = "hash:32"
assets.auto_build = app.config["SERVER_ENV"] == 'development'
assets.debug = False
bundles = PythonLoader(project.asset_bundles).load_bundles()
for name, bundle in bundles.iteritems():
    assets.register(name, bundle)

manager = Manager(app)
manager.add_command('db', MigrateCommand)
manager.add_command('assets', ManageAssets)

if __name__ == '__main__':
    manager.run()
