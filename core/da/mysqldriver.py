import mysql.connector


class MySQLDriver:
    def __init__(self, config : dict  ):
        self.config = config 

    def __enter__(self) -> 'cursor':
        self.connection = mysql.connector.connect( user=self.config[ 'username' ], password=self.config[ 'password' ] , host=self.config[ 'hostname' ], database=self.config[ 'dbname' ] )
        assert self.connection is not None, 'failed getting connection from DB'
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_value, exc_trace) -> None:
        self.connection.commit()
        self.cursor.close()
        self.connection.close()
