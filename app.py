# Flask-related imports
from flask import Flask, render_template, url_for, redirect, request, session

# Add functions you need from databases.py to the next line!
from databases import *

from model import User, Content
# Starting the flask 
app = Flask(__name__)


#Session here
Session['username']=user_name


# App routing code here
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/signup',methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        print ("get method")
        return render_template('sign-up.html')
    else:
        print("post method 1")
        user_name = request.form['user_name']
        password= request.form['password']
        add_user(user_name,password)
        print ("post method 2")
        return redirect (url_for("home"))



	
@app.route('/login',methods=['GET', 'POST'])
def login():
    if request.method== 'GET':
        return render_template("login.html")
    else:
        user_name = request.form['user_name']
        password= request.form['password']
        
        if query_by_name(user_name,password):
            return redirect (url_for("home"))
        else:
            return render_template("login.html",message="your user name or password is wrong")


        


# Running the Flask app
if __name__ == "__main__":
    app.run(debug=True)
