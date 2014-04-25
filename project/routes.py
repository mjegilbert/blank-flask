from project import app

from project.views import site

app.add_url_rule('/', 'site.home', site.home, methods=['get'])
