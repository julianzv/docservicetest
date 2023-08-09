from sqlalchemy.orm import Session
from app.models import models
from app.schemas import schemas

def get_document_job(db: Session, document_job_id: str):
    return db.query(models.DocumentJob).filter(models.DocumentJob.id == document_job_id).first()

def get_document_jobs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.DocumentJob).offset(skip).limit(limit).all()

def get_document(db: Session, document_id: str):
    return db.query(models.Document).filter(models.Document.id == document_id).first()

def create_document_job(db: Session, document_job: schemas.DocumentJobCreate):
    db_document_job = models.DocumentJob(**document_job.dict())
    db.add(db_document_job)
    db.commit()
    db.refresh(db_document_job)
    return db_document_job

def create_document(db: Session, document: schemas.DocumentCreate):
    db_document = models.Document(**document.dict())
    db.add(db_document)
    db.commit()
    db.refresh(db_document)
    return db_document