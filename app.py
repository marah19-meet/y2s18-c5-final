# Flask-related imports
from flask import Flask, render_template, url_for, redirect, request
from flask import session as login_session

# Add functions you need from databases.py to the next line!
from databases import add_user, get_all_users, login, add_content, query_by_arts,query_by_news, delete_content, delete_content2 ,add_content2

from model import User, Content,Content2
# Starting the flask 
app = Flask(__name__)
app.secret_key='ayyy lmao'

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
def login_route():
    if request.method== 'GET':
        return render_template("login.html")
    else:
        user_name = request.form['user_name']
        password= request.form['password']
        user = login(user_name, password)
        if user == False:
            print("Unable to initiate session")
            return render_template("login.html",message="Your username or password is incorrect")
        else:
            login_session['username']=user.user_name
            return redirect (url_for("home"))



@app.route('/news', methods=['GET','POST'])
def news_route():
    if request.method=='GET':
        return render_template('news.html',news=query_by_news())
    else:
        
        if 'username' in login_session:
            title=request.form['title']
            content=request.form['content']
            image_url=request.form['image_url']
            op = login_session.get('username')
            add_content(title, op, content, image_url)
            return render_template('news.html',news=query_by_news())

        else:
            print('You are not logged in')
            return redirect (url_for("home"))



@app.route('/news/delete/<content_id>', methods=['POST'])
def delete_news_content(content_id):
    
    if 'username' in login_session:
        delete_content(content_id)
        return redirect(url_for('news_route'))
    else:
        return redirect (url_for("home"))



@app.route('/about-team')
def a_team():
    return render_template('about-team.html')

@app.route('/about-website')
def a_website():
    return render_template('about-website.html')

@app.route('/arts', methods=['GET','POST'])
def arts_route():
    if request.method=='GET':
        return render_template('neighborhood-2.html',arts=query_by_arts())
    else: 
        title=request.form['title']
        content=request.form['content']
        image_url=request.form['image_url']
        op = login_session.get('username')
        add_content2(title, op, content, image_url)
        return render_template('news.html',arts=query_by_arts())
    
@app.route('/arts/delete/<content2_id>', methods=['POST'])
def delete_arts_content(content2_id):
    if 'username' in login_session:
        delete_content2(content2_id)
        
        return redirect(url_for('arts_route'))
    else:
        return redirect (url_for("home"))
        


        
        

@app.route('/logout', methods=['GET'])
def logout():
    del login_session['username']
    return redirect (url_for("home"))



# Running the Flask app
if __name__ == "__main__":
    app.run(debug=True)
