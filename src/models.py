import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

#python src/models.py


class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)

class FavPeople(Base):
    __tablename__ = 'FavPeople'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    people_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))

class FavPlanet(Base):
    __tablename__ = 'FavPlanet'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    people_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))

class Characters(Base):
    __tablename__ = 'Characters'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, ForeignKey('FavPeople.people_id'))
    people_id = Column(String, primary_key=True)
    birth_year = Column(String, primary_key=True)
    eye_color = Column(String, primary_key=True)
    films = Column(String, primary_key=True)
    gender = Column(String, primary_key=True)
    hair_color = Column(String, primary_key=True)
    height = Column(String, primary_key=True)
    homeworld = Column(String, primary_key=True)
    mass= Column(String, primary_key=True)
    name= Column(String, primary_key=True)
    skin_color = Column(String, primary_key=True)
    crated = Column(String, primary_key=True)
    edited = Column(String, primary_key=True)
    species = Column(String, primary_key=True)
    starships = Column(String, primary_key=True)
    url = Column(String, primary_key=True)
    vehicles = Column(String, primary_key=True)
    
class Planets(Base):
    __tablename__ = 'Planets'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, ForeignKey('FavPlanet.people_id'))
    climate = Column(String, primary_key=True)
    created = Column(String, primary_key=True)
    diameter = Column(String, primary_key=True)
    edited = Column(String, primary_key=True)
    films = Column(String, primary_key=True)
    gravity = Column(String, primary_key=True)
    name = Column(String, primary_key=True)
    orbital_period = Column(String, primary_key=True)
    population= Column(String, primary_key=True)
    residents= Column(String, primary_key=True)
    rotation_period = Column(String, primary_key=True)
    surface_water = Column(String, primary_key=True)
    terrain = Column(String, primary_key=True)
    url = Column(String, primary_key=True)
    starships = Column(String, primary_key=True)

    




# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')