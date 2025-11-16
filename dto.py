from pydantic import BaseModel
from typing import List

class ReviewBase(BaseModel):
    content: str
    rating: int

class ReviewCreate(ReviewBase):
 user_id: int
 movie_id: int

class Review(ReviewBase):
   id: int
   class Config:
      orm_mode = True

class ActorBase(BaseModel):
   name: str

class ActorCreate(ActorBase):
 pass   

class Actor(ActorBase):
   id: int
   class Config:
      orm_mode = True

class MovieBase(BaseModel):
   title: str
   year: int
   genre: str

class MovieCreate(MovieBase):
   pass       

class Movie(MovieBase):
   id: int
   actors: List[Actor] = []
   class Config:
      orm_mode = True

class UserBase(BaseModel):
   userrname: str
   email: str

class UserCreate(UserBase):
   pass

class User(UserBase):
   id: int
   reviews: List[Review] = []
   class Config:
      orm_mode = True
   