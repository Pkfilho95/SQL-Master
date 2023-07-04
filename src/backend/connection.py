import mysql.connector as mysql
import psycopg2
import sqlite3
import json

from settings import JSON_PATH

class Connection:
    """
    Class responsible for establishing the connection with the database.
    """

    def __init__(self):
        self.conn = None
        self.error = None

        self._set_vars()
        getattr(self, '_conn_%s' %self.db_type)()
    
    def _open_json(self):
        """
        Open the last_connection.json file and return the data.
        """

        try:
            with open(JSON_PATH, 'r') as _file:
                _data = json.load(_file)

            return _data
        
        except Exception as error:
            raise error

    def _set_vars(self):
        """
        Open the conn.json file and get all variables.
        """
        _data = self._open_json()
        
        self.db_type = _data['db_type']
        self.host = _data['host']
        self.database = _data["database"]
        self.user = _data["user"]
        self.password = _data["password"]
        self.db_path = _data["db_path"]

    def _conn_mysql(self):
        """
        Establish the connection to the MySQL database.
        """
        try:
            _conn = mysql.connect(
                host = self.host,
                database = self.database,
                user = self.user,
                password = self.password
            )

            self.conn = _conn
            self.error = None
        
        except Exception as error:
            self.conn = None
            self.error = error
    
    def _conn_postgresql(self):
        """
        Establish the connection to the PostgreSQL database.
        """
        try:
            _conn = psycopg2.connect(
                host = self.host,
                database = self.database,
                user = self.user,
                password = self.password
            )

            self.conn = _conn
            self.error = None
        
        except Exception as error:
            self.conn = None
            self.error = error

    def _conn_sqlite(self):
        """
        Establish the connection to the SQLite database.
        """
        try:
            _conn = sqlite3.connect(database=self.db_path)
        
            self.conn = _conn
            self.error = None
        
        except Exception as error:
            self.conn = None
            self.error = error
