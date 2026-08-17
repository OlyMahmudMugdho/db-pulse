from sqlalchemy.orm import sessionmaker

from db_pulse.database.engines import sqlite_engine

SessionLocal = sessionmaker(bind=sqlite_engine())
