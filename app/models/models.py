from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, JSON
from sqlalchemy.orm import relationship
from uuid import uuid4

from sqlalchemy.dialects.postgresql import UUID
from app.db.config import Base

class DocumentJob(Base):
    __tablename__ = "document_job"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    time_stamp = Column(DateTime, nullable=False)
    document_status = Column(String, nullable=False)
    event_type = Column(String, nullable=False)
    document_data = Column(JSON, nullable=False)

    documents = relationship("Document", back_populates="document_job")

class Document(Base):
    __tablename__ = "document"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    created_at = Column(DateTime, nullable=False)
    modified_at = Column(DateTime, nullable=False)
    path_to_file = Column(String, nullable=False)
    policy_status = Column(String, nullable=False)
    policy_id = Column(UUID(as_uuid=True), nullable=False)
    account_id = Column(UUID(as_uuid=True), nullable=False)
    company_id = Column(UUID(as_uuid=True), nullable=False)
    product_id = Column(UUID(as_uuid=True), nullable=False)
    document_job_id = Column(UUID(as_uuid=True), ForeignKey("document_job.id"), nullable=False)

    document_job = relationship("DocumentJob", back_populates="documents")

