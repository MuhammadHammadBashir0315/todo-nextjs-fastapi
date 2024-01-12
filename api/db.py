from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

conn_str  = "postgresql://hammad.bashir0315:JPtH6Ecbpk0x@ep-tiny-bar-64942038.us-east-2.aws.neon.tech/neondb?sslmode=require"

engine = create_engine(conn_str)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()