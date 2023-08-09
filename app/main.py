from typing import Union
from sqlalchemy.orm import Session
from app.db import config
from app.models import models
from app.schemas import schemas
from app.utils import crud
from fastapi import FastAPI, Depends, HTTPException, status


models.Base.metadata.create_all(bind=config.engine)
app = FastAPI()

def get_db():
    db = config.SessionLocal()
    try:
        yield db
    finally:
        db.close()

consumer_task = None

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/document_job", response_model=schemas.DocumentJob)
def create_document_job(document_job: schemas.DocumentJobCreate, db: Session = Depends(get_db)):
    db_document_job = crud.create_document_job(db, document_job)
    return db_document_job

@app.get("/document_jobs", response_model=list[schemas.DocumentJob])
def read_document_jobs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    document_jobs = crud.get_document_jobs(db, skip=skip, limit=limit)
    return document_jobs

@app.get("/document_job/{document_job_id}", response_model=schemas.DocumentJob)
def read_document_job(document_job_id: str, db: Session = Depends(get_db)):
    db_document_job = crud.get_document_job(db, document_job_id=document_job_id)
    if db_document_job is None:
        raise HTTPException(status_code=404, detail="Document Job not found")
    return db_document_job


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)

# uvicorn main:app --reload