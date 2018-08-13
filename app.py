# Flask-related imports
from flask import Flask, render_template, url_for, redirect, request, session

# Add functions you need from databases.py to the next line!
from databases import add_user, get_all_users

from model import User
# Starting the flask 
app = Flask(__name__)

# App routing code here
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/signup',methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template('form.html')
    else:
        user_name = request.form['user_name']
        password= request.form['password']
        save_to_database(user_name,password)
        return render_template('from.html')


	
@app.route('/login',methods=['GET', 'POST'])
def login():
     


# Running the Flask app
if __name__ == "__main__":
    app.run(debug=True)
