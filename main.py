from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import models, dto, crud
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)
app = FastAPI(title= "Movie Catalog")
              
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@app.get("/user/", response_model=list[dto.User])
def read_users(db: Session = Depends(get_db)):
  return crud.get_users(db)

@app.post("/user/", response_model=dto.User)
def create_user(user: dto.UserCreate, db: Session = Depends(get_db)):
  return crud.create_users(db, user)  

@app.put("/user/{user_id}", response_model=dto.User)
def update_user(user_id: int, user: dto.UserCreate, db: Session = Depends(get_db)):
   return crud.update_users(db, user_id, user)

@app.delete("/user/{user_id}", response_model=dto.User)
def delete_user(user_id: int, db: Session = Depends(get_db)):
   return crud.delete_users(db, user_id)

@app.get("/movies/", response_model=list[dto.Movie])
def read_movies(db: Session = Depends(get_db)):
  return crud.create_movie(db)  

@app.post("/movies/", response_model=dto.Movie)
def create_movie(movie: dto.MovieCreate, db: Session = Depends(get_db)):
  return crud.create_movie(db, movie)  

@app.put("/movies/{movie_id}", response_model=dto.Movie)
def update_movie(movie_id: int, movie: dto.MovieCreate, db: Session = Depends(get_db)):
   return crud.update_movie(db, movie_id, movie)

@app.delete("/movies/{movie_id}", response_model=dto.Movie)
def delete_movie(movie_id: int, db: Session = Depends(get_db)):
   return crud.delete_movie(db, movie_id)


@app.get("/actors/", response_model=list[dto.Actor])
def read_actors(db: Session = Depends(get_db)):
  return crud.create_actors(db)     

@app.post("/actors/", response_model=dto.Actor)
def create_actor(actor: dto.ActorCreate, db: Session = Depends(get_db)):
  return crud.create_actor(db, actor)    

@app.put("/actors/{movie_id}", response_model=dto.Movie)
def update_actor(actor_id: int, actor: dto.ActorCreate, db: Session = Depends(get_db)):
   return crud.update_actor(db, actor_id, actor)

@app.delete("/actors/{actor_id}", response_model=dto.Actor)
def delete_actor(actor_id: int, db: Session = Depends(get_db)):
   return crud.delete_actor(db, actor_id)


@app.get("/reviews/", response_model=list[dto.Review])
def read_reviews(db: Session = Depends(get_db)):
  return crud.create_reviews(db)

@app.post("/reviews/", response_model=dto.Review)
def create_review(review: dto.ReviewCreate, db: Session = Depends(get_db)):
  return crud.create_review(db, review)

@app.put("/reviews/{review_id}", response_model=dto.Review)
def update_review(review_id: int, review: dto.ReviewCreate, db: Session = Depends(get_db)):
   return crud.update_review(db, review_id, review)

@app.delete("/reviews/{review_id}", response_model=dto.Review)
def delete_review(review_id: int, db: Session = Depends(get_db)):
   return crud.delete_review(db, review_id)
