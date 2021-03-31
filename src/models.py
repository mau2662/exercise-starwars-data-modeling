import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

# class Person(Base):
 #   __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
  #  id = Column(Integer, primary_key=True)
   # name = Column(String(250), nullable=False)

#class Address(Base):
 #   __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
  #  id = Column(Integer, primary_key=True)
   # street_name = Column(String(250))
    # street_number = Column(String(250))
    # post_code = Column(String(250), nullable=False)
    #person_id = Column(Integer, ForeignKey('person.id'))
    # person = relationship(Person)

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    description = Column(String(250))
    hair_color = Column(String(250))
    image = Column(String(250))
    gender = Column(String(250))
    height = Column(Integer)

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    diameter = Column(Integer)
    rotation_period = Column(Integer)
    orbital_period = Column(Integer)
    image = (String(250))
    climate = (String(250))
    terrain = (String(250))
 
class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    planet_fav = Column(String(250),ForeignKey('planet.id'))
    #planet = relationship(Planet)
    character_fav = Column(String(250),ForeignKey('character.id'))
    #character = relationship(Character)

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250))
    password = Column(String(250))
    favorite_character_user = Column(String(250),ForeignKey('favorites.character_fav'))
    
    favorite_planet_user = Column(String(250),ForeignKey('favorites.planet_fav'))
   


    
    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')