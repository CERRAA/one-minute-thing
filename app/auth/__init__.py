# from flask import Blueprint,render_template

# auth = Blueprint("auth", __name__, static_folder='static', template_folder='templates')
# from app.auth import views


from flask import Blueprint


auth = Blueprint('auth',__name__)

from . import views,forms