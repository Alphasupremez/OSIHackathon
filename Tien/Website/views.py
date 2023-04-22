# Store all main views / URL / frontend aspects

"""A blueprint is used to organize a group of related views and other code
   in a modular and reusable way. It allows to define routes, templates, and static
   files for a specific part of the application"""

from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from .models import User


views = Blueprint('views', __name__)


# Define route
@views.route('/')  
@login_required
def home_page():
   Larray = '<iframe src="https://www.google.com/maps/embed?pb=!1m16!1m12!1m3!1d178903.0231394029!2d-94.31410684451964!3d45.522965959522146!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!2m1!1selectric%20vehicle%20charging%20station!5e0!3m2!1sen!2sus!4v1682088186159!5m2!1sen!2sus" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>'
   map_html = Larray
   return render_template("home.html", user=current_user, map_html=map_html)


