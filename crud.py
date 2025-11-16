from sqlalchemy.orm import Session
import models, dto

def get_users(db: Session):
    return db.query(models.User).all()

def create_users(db: Session, user: dto.UserCreate):
    db_user = models.User(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_users(db: Session, user_id: int, user: dto.UserCreate):
    db_user = db.get(models.User, user_id)
    for key, value in user.model_dump().items():
        setattr(db_user, key, value)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_users(db: Session, user_id: int):
    db_user = db.get(models.User, user_id)
    db.delete(db_user)
    db.commit()
    return db_user

def get_movies(db: Session):
    return db.query(models.Movie).all()

def create_movie(db: Session, movie: dto.MovieCreate):
    db_movie = models.Movie(**movie.model_dump())
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    return db_movie

def update_movie(db: Session, movie_id: int, movie: dto.MovieCreate):
    db_movie = db.get(models.Movie, movie_id)
    for key, value in movie.model_dump().items():
        setattr(db_movie, key, value)
    db.commit()
    db.refresh(db_movie)
    return db_movie

def delete_movie(db: Session, movie_id: int):
    db_movie = db.get(models.Movie, movie_id)
    db.delete(db_movie)
    db.commit()
    return db_movie

def get_actors(db: Session):
    return db.query(models.Actor).all()

def create_actor(db: Session, actor: dto.ActorCreate):
    db_actor = models.Actor(**actor.model_dump())
    db.add(db_actor)
    db.commit()
    db.refresh(db_actor)
    return db_actor

def update_actor(db: Session, actor_id: int, actor: dto.ActorCreate):
    db_actor = db.get(models.Actor, actor_id)
    for key, value in actor.model_dump().items():
        setattr(db_actor, key, value)
    db.commit()
    db.refresh(db_actor)
    return db_actor

def delete_actor(db: Session, actor_id: int):
    db_actor = db.get(models.Actor, actor_id)
    db.delete(db_actor)
    db.commit()
    return db_actor

def get_reviews(db: Session):
    return db.query(models.Review).all()

def create_review(db: Session, review: dto.ReviewCreate):
    db_review = models.Review(**review.model_dump())
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review

def update_review(db: Session, review_id: int, review: dto.ReviewCreate):
    db_review = db.get(models.Review, review_id)
    for key, value in review.model_dump().items():
        setattr(db_review, key, value)
    db.commit()
    db.refresh(db_review)
    return db_review

def delete_review(db: Session, review_id: int):
    db_review = db.get(models.Review, review_id)
    db.delete(db_review)
    db.commit()
    return db_review