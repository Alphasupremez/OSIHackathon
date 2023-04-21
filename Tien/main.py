# This file where I am going to run when I want to start my web server or website
"""Library package requiremtns (pip install library's name)
    1. Install Flask
    2. Install Flask-login (being used to log users in)
    3. Install flask-sqlalchemy (database that can be used/ wrapper for SQL
                                /create/delete/add models)
"""

# import create_app function from the Website package
from Website import create_app

app = create_app()

if __name__ == '__main__':
    # debug means everytime I change the code, it automatically rerun the web server
    app.run(debug=True) 
