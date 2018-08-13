# Database related imports
# Make sure to import your tables!
from model import Base, User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# You can change the name of your database, just change project.db to whatever you want (make sure to include .db at the end!)
# Make sure you have the same name for the database in the app.py file!
engine = create_engine('sqlite:///BetterWays.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Your database functions are located under here (querying, adding items, etc.)
def add_user(user_name,password):
    print("you are singed up")
    user= User(user_name=user_name,password=password)
    session.add(user)
    session.commit()

def get_all_users():
    users=session.query(User).all()
    return users

# Example of adding a student:
def query_by_name(their_name,their_password):
    user = session.query(
       User).filter_by(user_name=their_name).first()
    print(user.password)
    print(user.password==their_password)
    if user!=None and str(user.password)==their_password:
        print("True")
        return True
    else:
        print("False")
        return False
##/////////////////////////////////
def add_content():

    pass
        
        


