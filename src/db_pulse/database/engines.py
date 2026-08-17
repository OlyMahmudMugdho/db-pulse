from sqlalchemy import Engine, create_engine


def sqlite_engine() -> Engine:
    return create_engine("sqlite+pysqlite:///pulse_db.sqlite3")
