from .connection import Connection

class Command:
    """
    Class responsible for running the SQL scripts and returning the requests.
    """
    def __init__(self, conn: Connection):
        self.conn = conn

    def execute(self, script: str):
        """
        Execute the SQL script.
        """
        
        _conn = self.conn.conn
        _cursor = self.conn.cursor

        _cursor.execute(script)

        _command = script.strip().split()[0].upper()
        if _command == 'SELECT':
            _result = _cursor.fetchall()
            _cols = self._columns(cursor=_cursor)
            
            _result.insert(0, _cols)

            return _result
        
        else:
            _conn.commit()
            return 'Script executed successfully.'
    
    def _columns(self, cursor: Connection.cursor):
        """
        Get the name of the columns.
        """
        return tuple(description[0] for description in cursor.description)
