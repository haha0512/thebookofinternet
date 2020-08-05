#app.wsgi
import sys

sys.path.append('/var/www/html/thebookofinternet')

from thebookofinternet import app as application