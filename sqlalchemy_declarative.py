import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class fname(Base):
    __tablename__ = 'fname'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(250), nullable=False)

class lname(Base):
    __tablename__ = 'lname'
    id = Column(Integer, primary_key=True)
    last_name = Column(String(250), nullable=False)

class gender(Base):
    __tablename__ = 'gender'

    id = Column(Integer, primary_key=True)
    gender = Column(String(250), nullable=False)

class words(Base):
    __tablename__ = 'words'

    id = Column(Integer, primary_key=True)
    Quotes = Column(String(250), nullable=False)



engine = create_engine('sqlite:///sqlalchemy_example.db')

# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
Base.metadata.create_all(engine)
