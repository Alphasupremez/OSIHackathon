from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

from .Saving import Saving
from .save_calc import DisplaySavings
import pandas as pd

auth = Blueprint('auth', __name__)


# Define login/logout route for the website

# LOG IN
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True) # Keep the user'page while have yet rerun website
                return redirect(url_for('views.home_page')) # get to the home page
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)

# LOG OUT
@auth.route('/logout')
# """@login_required is used to make sure cannot access this page through the route
#    unless the user login successfully"""
@login_required     
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

# SIGN UP
@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        user = User.query.filter_by(email=email).first()

        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash("Email must be greater than 4 character.", category='error')
        elif len(first_name) < 2:
            flash("First name must be greater than 1 character.", category='error')
        elif password1 != password2:
            flash("Passwords don't match.", category='error')
        elif len(password1) < 7:
            flash("Password must be at least 7 character.", category='error')
        else:
            # add user infor to database
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(user, remember=True)
            flash("Account created!", category='success')
            return redirect(url_for('views.home_page'))

    return render_template("sign-up.html", user=current_user)


    
# Added stuff


# Profile
@auth.route('/profile', methods=['GET', 'POST'])
def profile():
    filename = "Website/savings.csv"
    saving = pd.read_csv(filename)
    ts = saving['Savings'].iloc[-1]
    return render_template("profile.html", user=current_user, total_savings = f"{ts :0.2f}", boolean=True)

# Rewards
@auth.route('/rewards', methods=['GET', 'POST'])
def rewards():
    return render_template("rewards.html", user=current_user, boolean=True)
    

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
    filename = "Website/savings.csv"
    ds = DisplaySavings(filename, save_amount)
    ts = ds.total_savings()
    
    cps = ds.calculate_past_savings()
    saving = pd.read_csv(filename)
    
    ps = saving['Savings'].iloc[-1]
    
    
        
    # formated way to pass the total_savings value from the function and immediatly display it
    return render_template("savings.html", user=current_user, total_savings = f"{ts :0.2f}", past_savings = f"{ps :0.2f}", boolean=True)
