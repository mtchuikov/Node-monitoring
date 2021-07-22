from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.cursor import Cursor
from db.models import SystemLoadStatistic
from db.models import SystemRequirements
from db.base import Base

engine = create_engine(r'sqlite:///server_data.db', echo=True)
session = sessionmaker(bind=engine)()

cursorSystemRequirements = Cursor(SystemRequirements, session)
Base.metadata.create_all(engine)