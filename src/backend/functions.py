from tkinter import messagebox
from tkinter.ttk import Treeview
import json

from .connection import Connection
from .command import Command
from settings import JSON_PATH

def open_json():
    try:
        with open(JSON_PATH, 'r') as _file:
            _data = json.load(_file)

        return _data
    
    except Exception as error:
        raise error
    
def update_json(db_type: str, host: str, database: str, user: str, password: str, db_path: str):
    try:
        with open(JSON_PATH, 'r') as file:
            data = json.load(file)
    
    except Exception as error:
        raise error
    
    data['db_type'] = db_type
    data['host'] = host
    data['database'] = database
    data['user'] = user
    data['password'] = password
    data['db_path'] = db_path

    with open(JSON_PATH, 'w') as file:
        json.dump(data, file, indent=4)

def run_script(conn: Connection, script: str, table: Treeview):
    if script == "":
        messagebox.showerror('Error', 'Write a valid script.')
        return None

    if not conn:
        messagebox.showerror('Error', 'Connect to a database.')
        return None

    cmd = Command(conn=conn)

    try:
        result = cmd.execute(script=script)
    except Exception as error:
        messagebox.showerror('Error', error)
        return None

    if isinstance(result, list):
        table.delete(*table.get_children())
        table['columns'] = result[0]

        col_width = table.winfo_width() // len(result[0])

        table.column("#0", width=0, stretch=False)
        
        for col in result[0]:
            table.column(col, stretch=False, width=col_width, anchor='center')
            table.heading(col, text=col, anchor='center')
        
        for row in result[1:]:
            table.insert('', 'end', values=row)
    
    else:
        table.delete(*table.get_children())
        for column in table['columns']:
            table.column(column, width=0)
            
        messagebox.showinfo('Info', result)