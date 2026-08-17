from contextlib import asynccontextmanager

from fastapi import FastAPI
from sqlalchemy import Engine

from db_pulse.configs.sqlalchemy_base import Base
from db_pulse.database.engines import sqlite_engine


@asynccontextmanager
async def init_db(engine: Engine):
    Base.metadata.create_all(engine)
    yield


@asynccontextmanager
async def master_lifespan(app: FastAPI):
    async with init_db(engine=sqlite_engine()):
        yield
