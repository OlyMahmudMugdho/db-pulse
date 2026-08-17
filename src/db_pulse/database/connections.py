from sqlalchemy import Connection

from db_pulse.database.engines import sqlite_engine


def get_sqlite_connection() -> Connection:
    return sqlite_engine().connect()
