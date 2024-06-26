from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import requests

import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users

@app.get("/suggestions/", response_model=list[schemas.Suggestion])
def read_suggestion(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    suggestions = crud.get_suggestions(db, skip=skip, limit=limit)
    return suggestions

@app.post("/users/{user_id}/suggestions/", response_model=schemas.Suggestion)
def create_suggestion_for_user(
    user_id: int, suggestion: schemas.SuggestionCreate, db: Session = Depends(get_db)
):
    return crud.create_user_suggestion(db=db, suggestion=suggestion, user_id=user_id)

@app.post("/users/{user_id}/suggestions/{suggestion_id}", response_model=schemas.Suggestion)
def create_suggestion_for_user(
    user_id: int, suggestion: schemas.SuggestionCreate, db: Session = Depends(get_db)
):
    return crud.create_user_suggestion(db=db, suggestion=suggestion, user_id=user_id)

@app.get("/users/{user_id}/suggestions/{suggestion_id}", response_model=schemas.Suggestion)
def read_suggestion(user_id: int, suggestion_id: int, db: Session = Depends(get_db)):
    suggestions = crud.get_user_suggestion(db, suggestion_id=suggestion_id, user_id=user_id)
    return suggestions

@app.get("/users/{user_id}/suggestions", response_model=list[schemas.Suggestion])
def read_suggestion(user_id: int, limit: int = 100, db: Session = Depends(get_db)):
    suggestions = crud.get_user_suggestions(db, user_id=user_id, limit=limit)
    return suggestions


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/users/{user_id}/items/", response_model=schemas.Item)
def create_item_for_user(
    user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
):
    return crud.create_user_item(db=db, item=item, user_id=user_id)


@app.get("/items/", response_model=list[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items