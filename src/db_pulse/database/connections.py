from sqlalchemy import Connection, Engine


def get_sqlite_connection(engine: Engine) -> Connection:
    return engine.connect()
