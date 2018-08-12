from sqlalchemy import Column, Integer, String, Boolean
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

# Example code:
# class Student(Base):
   # __tablename__ = "students"
    #id = Column(Integer, primary_key = True)
    #name = Column(String)
    #year = Column(Integer)

    #def __repr__(self):
        #return ("Student name: {}, Student year:{}".format(self.name, self.year))
