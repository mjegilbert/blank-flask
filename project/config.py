# Basics
DEBUG = True
SESSION_COOKIE_SECURE = False
SERVER_ENV = 'development'
SECRET_KEY = "awef98awefinq23r9wkladsf98q2jkl3rq2"

# Database Info
SQLALCHEMY_ECHO = False
SQL_HOSTNAME = 'localhost'
SQL_DB_NAME = 'development'
SQL_USERNAME = 'dropbox'
SQL_PASSWORD = 'dropbox'
SQLALCHEMY_DATABASE_URI = 'mysql://%s:%s@%s/%s?charset=utf8&use_unicode=1' % (SQL_USERNAME, SQL_PASSWORD, SQL_HOSTNAME, SQL_DB_NAME)
MYSQL_SERVER_URI = 'mysql://%s:%s@%s/?charset=utf8&use_unicode=1' % (SQL_USERNAME, SQL_PASSWORD, SQL_HOSTNAME)
