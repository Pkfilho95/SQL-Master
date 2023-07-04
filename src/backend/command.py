from .connection import Connection

class Command:
    """
    Class responsible for running the SQL scripts and returning the requests.
    """
    def __init__(self, conn: Connection):
        self.conn = conn

    def execute(self, script: str):
        
        _conn = self.conn.conn
        _cursor = _conn.cursor()

        _cursor.execute(script)

        _command = script.strip().split()[0].upper()
        if _command == 'SELECT':
            _result = _cursor.fetchall()

            _table = script.upper().strip().split()
            _table = _table[_table.index('FROM') + 1]
            _cols = self._columns(table=_table)
            
            _result.insert(0, _cols)

            return _result
        
        else:
            _conn.commit()
            return 'Script executed successfully.'
    
    def _columns(self, table: str):
        _cursor = self.conn.conn.cursor()

        if self.conn.db_type == 'mysql':
            sql = f"""DESCRIBE {table}"""
            _cursor.execute(sql)
            return tuple(col[0] for col in _cursor.fetchall())

        elif self.conn.db_type == 'postgresql':
            sql = f"""SELECT column_name FROM information_schema.columns WHERE table_name={table}"""
            _cursor.execute(sql)
            return tuple(col[0] for col in _cursor.fetchall())

        elif self.conn.db_type == 'sqlite':
            sql = f"""PRAGMA table_info({table})"""
            _cursor.execute(sql)
            return tuple(col[1] for col in _cursor.fetchall())
    
        else:
            raise ValueError('Invalid database type.')
