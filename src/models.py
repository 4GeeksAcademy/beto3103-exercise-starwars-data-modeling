from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
	__tablename__ = "user"
	id = Column(Integer(), primary_key = True)
	name = Column(String(80), nullable= False)
	last_name = Column(String(80), nullable = False)
	username = Column(String(40), nullable = False, unique = True)
	email = Column(String(80), nullable= False, unique= True)
	favorite=relationship("Favorite", uselist = True, backref="user")
	created_date = Column(DateTime())

class Favorite(Base):
	__tablename__ = "favorite"
	id = Column(Integer(), primary_key= True)
	user_id = Column(Integer(), ForeignKey("user.id"))
	planet = Column(Integer(), ForeignKey("planet.id"))
	character = Column(Integer(), ForeignKey("character.id"))

class Planet(Base):
	__tablename__ = "planet"
	id = Column(Integer(), primary_key = True)
	name = Column(String(80), nullable = False)
	favorite = relationship("Favorite", uselist = True, backref = "planet")
	climate = Column(String(40))
	created = Column(DateTime())
	diameter = Column(Integer())
	edited = Column(DateTime())
	gravity = Column(Integer())
	orbital_period = Column(Integer())
	population = Column(Integer())
	rotation_period = Column(Integer())
	surface_water = Column(Integer())
	terrain = Column(String(40))

class Character(Base):
    __tablename__ = "character"
    id = Column(Integer(), primary_key = True)
    name = Column(String(50), nullable = False)
    birth_year = Column(String(10))
    eye_color = Column(String(10))
    gender = Column(String(10))
    hair_color = Column(String(10))
    height = Column(Integer())
    mass = Column(Integer())
    skin_color = Column(String(10))
    favorite = relationship("Favorite", uselist = True, backref = "planet")

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

#     def to_dict(self):
#         return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
