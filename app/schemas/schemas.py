import uuid
import datetime
from pydantic import BaseModel, Field

class DocumentJobBase(BaseModel):
    time_stamp: datetime.datetime
    document_status: str
    event_type: str
    document_data: dict

class DocumentJobCreate(DocumentJobBase):
    pass

class DocumentJob(DocumentJobBase):
    id: uuid.UUID

    class Config:
        orm_mode = True


class DocumentBase(BaseModel):
    created_at: datetime.datetime
    modified_at: datetime.datetime
    path_to_file: str
    policy_status: str
    policy_id: uuid.UUID
    account_id: uuid.UUID
    company_id: uuid.UUID
    product_id: uuid.UUID
    document_job_id: uuid.UUID

class DocumentCreate(DocumentBase):
    pass

class Document(DocumentBase):
    id: uuid.UUID

    class Config:
        orm_mode = True