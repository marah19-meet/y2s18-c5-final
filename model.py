from datetime import datetime

from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

# Place your database schema code here
class User(Base):
    __tablename__="User"
    id=Column(Integer, primary_key = True)
    user_name=Column(String)
    password=Column(Integer)

    def __repr__(self):
        return("user name: {},password:{}".format(self.user_name,self.password))

class Content(Base):
    __tablename__="Content"
    id=Column(Integer, primary_key = True)
    title=Column(String)
    op=Column(String)
    time_of_upload=Column(DateTime, datetime.utcnow)
    text=Column(String)
    image=Column(String)

    def __repr__(self):
        return "Title: {} \n Original Poster: {} \n Time of Upload: {} \n Text: {} \n Image: {}"

# Example code:
# class Student(Base):
   # __tablename__ = "students"
    #id = Column(Integer, primary_key = True)
    #name = Column(String)
    #year = Column(Integer)

    #def __repr__(self):
        #return ("Student name: {}, Student year:{}".format(self.name, self.year))
