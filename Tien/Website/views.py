# Store all main views / URL / frontend aspects

"""A blueprint is used to organize a group of related views and other code
   in a modular and reusable way. It allows to define routes, templates, and static
   files for a specific part of the application"""

from flask import Blueprint, render_template

my_views = Blueprint('my_view', __name__)


# Define route
@my_views.route('/')  
def home_page():
    name = 'our Website'
    return render_template("home.html", name=name)

