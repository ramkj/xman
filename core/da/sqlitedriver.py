import sqlite3 


class SQLiteDriver:
    def __init__(self, dbname: str ):
        self.config = dbname

    def __enter__(self) -> 'cursor':
        self.connection = sqlite3.connect(self.config)
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_value, exc_trace) -> None:
        self.connection.commit()
        self.cursor.close()
        self.connection.close()
