from sqlalchemy.orm import Session

import models, schemas

def get_suggestion(db: Session, suggestion_id: int):
    return db.query(models.Suggestion).filter(models.Suggestion.id == suggestion_id).first()

def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()

def get_suggestions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Suggestion).offset(skip).limit(limit).all()

def get_user_suggestion(db: Session, suggestion_id: int, user_id: int):
    return db.query(models.Suggestion).filter(models.Suggestion.id == suggestion_id, models.Suggestion.owner_id == user_id).first()

def get_user_suggestions(db: Session, user_id: int, limit: int = 100):
    return db.query(models.Suggestion).filter(models.Suggestion.owner_id == user_id).limit(limit).all()

def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def create_user_suggestion(db: Session, suggestion: schemas.SuggestionCreate, user_id: int):
    db_suggestion = models.Suggestion(**suggestion.dict(), owner_id=user_id)
    db.add(db_suggestion)
    db.commit()
    db.refresh(db_suggestion)
    return db_suggestion

def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()





