from sqlalchemy import Column, Integer, String, ForeignKey, Table, Text
from sqlalchemy.orm import relationship
from database import Base

movie_actor = Table(
    "movie_actor",
    Base.metadata,
    Column("movie_id", Integer, ForeignKey("moview.id")),
    Column("actor_id", Integer, ForeignKey("actor.id")),
)

class User(Base):
 __tablename__ = "users"
id = Column(Integer, primary_key=True, index=True)
username = Column(String, unique=True, index=True)
email = Column(String, unique=True, index=True)
reviews = relationship("Review", back_populates="user")

class Movie(Base):
 __tablename__ = "users"
id = Column(Integer, primary_key=True, index=True)
title = Column(String, index=True)
year = Column(Integer)
genre = Column(String)
reviews = relationship("Review", back_populates="movies")
actors = relationship("Actor", secondary=movie_actor, back_populates="movies")

class Actors(Base):
 __tablename__ = "users"
id = Column(Integer, primary_key=True, index=True)
name = Column(String, index=True)
birth_year = Column(Integer)
movies = relationship("Movie", secondary=movie_actor, back_populates="actors")

class Review(Base):
  __tablename__ = "reviews"
id = Column(Integer, primary_key=True, index=True)
rating = Column(Integer)
comment = Column(Text)
user_id = Column(Integer, ForeignKey("user.id"))
movie_id = Column(Integer, ForeignKey("movie.id"))
user = relationship("User", back_populates="reviews")
user = relationship("Movie", back_populates="reviews")
