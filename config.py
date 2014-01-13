import os
basedir = os.path.abspath(os.path.dirname(__file__))

CSRF_ENABLED = True
SECRET_KEY = 'you own my secret'


SQLALCHEMY_DATABASE_URI = 'mysql://tadegenban:111111@localhost/aflaskadmin'
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
