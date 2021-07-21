from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

base = declarative_base()
engine = create_engine(r'sqlite:///server_data.db', echo=True)
session = sessionmaker(bind=engine)()

# base.metadata.create_all(engine)