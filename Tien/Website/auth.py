from flask import Blueprint, render_template, request, flash

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


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        print(email)
        firstName = request.form.get('firstName')
        print(firstName)
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        if len(email) < 4:
            flash("Email must be greater than 4 character.", category='error')
        elif len(firstName) < 2:
            flash("First name must be greater than 1 character.", category='error')
        elif password1 != password2:
            flash("Passwords don't match.", category='error')
        elif len(password1) < 7:
            flash("Password must be at least 7 character.", category='error')
        else:
            # add user infor to database
            # new_user = User(email=email, firstName=firstName, password=)
            flash("Account created!", category='success')
            pass

    return render_template("sign-up.html")

