# Database related imports
# Make sure to import your tables!
from model import Base, User,Content,Content2
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.pool import NullPool
from datetime import datetime

# You can change the name of your database, just change project.db to whatever you want (make sure to include .db at the end!)
# Make sure you have the same name for the database in the app.py file!
engine = create_engine('sqlite:///BetterWays.db', poolclass=NullPool)
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = scoped_session(DBSession)

# Your database functions are located under here (querying, adding items, etc.)
def add_user(user_name,password):
    print("you are signed up")
    user= User(user_name=user_name,password=password)
    session.add(user)
    session.commit()

def get_all_users():
    users=session.query(User).all()
    return users

# Example of addting a student:
def login(their_name,their_password):
    user = session.query(User).filter_by(user_name=their_name).first()
    if user!=None and str(user.password)==their_password:
        print("True")
        return user
    else:
        print("False")
        return False
##/////////////////////////////////
def add_content(title,op,text,image):
    content=Content(title=title,op=op,time_of_upload=datetime.utcnow(),text=text,image=image)
    session.add(content)
    session.commit()

def add_content2(title,op,text,image):
    content2=Content2(title=title,op=op,time_of_upload=datetime.utcnow(),text=text,image=image)
    session.add(content2)
    session.commit()

   
def query_by_news():
    news=session.query(Content).all()
    news.reverse()
    return news

def query_by_arts():
    arts=session.query(Content2).all()
    arts.reverse()
    return arts


def delete_content(id):
    session.query(Content).filter_by(id=id).delete()
    session.commit()

def delete_content2(id):
    session.query(Content2).filter_by(id=id).delete()
    session.commit()



        
        


