from hashlib import new
from fastapi import FastAPI, Depends
# from pydantic import BaseModel
from . import schemas, models
from .database import SessionLocal, engine
from sqlalchemy.orm import Session

models.Base.metadata.create_all(engine)

def get_db() :
    db = SessionLocal()
    try :
        yield db
    finally :
        db.close()

app = FastAPI()

# uvicorn blog.main:app --reload
@app.post("/blog")
def create(request: schemas.Blog, db: Session = Depends(get_db)):
    # return request
    # return db
    new_blog = models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog
