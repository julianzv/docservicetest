from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


config = {
    "host": os.environ.get("DB_HOST", ""),
    "port": os.environ.get("DB_PORT", ""),
    "user": os.environ.get("DB_USER", ""),
    "pass": os.environ.get("DB_PASS", ""),
    "name": os.environ.get("DB_NAME", ""),
}

SQLALCHEMY_DATABASE_URL = f"postgresql://{config['user']}:{config['pass']}@{config['host']}:{config['port']}/{config['name']}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
