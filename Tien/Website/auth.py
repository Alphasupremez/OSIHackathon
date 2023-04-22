from flask import Blueprint, render_template, request, flash, url_for, redirect
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

from .Saving import Saving
from .save_calc import DisplaySavings
import pandas as pd

auth = Blueprint('auth', __name__)


# Define login/logout route for the website

# Login
@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html", boolean=True)

# Logout
@auth.route('/logout')
def logout():
    return "<p>Logout</p>"


# Signup
@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        if len(email) < 4:
            flash("Email must be greater than 4 character.", category='error')
        elif len(first_name) < 2:
            flash("First name must be greater than 1 character.", category='error')
        elif password1 != password2:
            flash("Passwords don't match.", category='error')
        elif len(password1) < 7:
            flash("Password must be at least 7 character.", category='error')
        else:
            # add user info to database
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            # db.commit() #Causes Error - AttributeError: commit
            flash("Account created!", category='success')
            return redirect(url_for('my_view.home_page'))

    return render_template("sign-up.html")




# Added stuff


# Profile
@auth.route('/profile', methods=['GET', 'POST'])
def profile():
    return render_template("profile.html", name='Zachary', email='bottleofwater@gmail.com', total_savings = '0.00', boolean=True)

# Rewards
@auth.route('/rewards', methods=['GET', 'POST'])
def rewards():
    return render_template("rewards.html", boolean=True)


# Savings Function Test (Replace with Lor's)
def saveFunction(start, end, rate):
    return (start + end - rate)
    

# Savings
@auth.route('/savings', methods=['GET', 'POST'])
def savings():
    # Default values
    startTime = 1
    endTime = 2
    rate = 1
    
    # After pressing the submit button or enter this takes effect
    if request.method == 'POST':
        startTime = request.form.get('startTime')
        endTime = request.form.get('endTime')
        rate = request.form.get('rate')
        
        # startTime needs to be 0-22
        if int(startTime) < 0 or int(startTime) > 2200:
            flash("Start time must be greater than 0.", category='error')
        
        # endTime needs to be 1-23
        elif int(endTime) > 2300 or int(endTime) < 100:
            flash("End time must be less than 23.", category='error')
        
        # startTime and endTime can't be equal to each other
        elif int(startTime) >= int(endTime):
            flash("Start time needs to be less than end time.", category='error')
            
        # Rate needs to be greater than 0
        elif float(rate) <= 0:
            flash("Rate needs to be greater than 0.", category='error')
            
        
        # save = 0.00
    Savings = Saving(startTime, endTime, rate)
    save_amount = Savings.compute_saving()
    filename = "Tien/Website/savings.csv"
    ds = DisplaySavings(filename, save_amount)
    ts = ds.total_savings()
    
    cps = ds.calculate_past_savings()
    saving = pd.read_csv(filename)
    
    ps = saving['Savings'].iloc[-1]
    
    
        
    # formated way to pass the total_savings value from the function and immediatly display it
    return render_template("savings.html", total_savings = f"{ts :0.2f}", past_savings = f"{ps :0.2f}", boolean=True)
