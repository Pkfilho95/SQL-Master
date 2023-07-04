import tkinter as tk
from tkinter import ttk

from .functions import *
from backend.connection import Connection
from backend.functions import *
from settings import *

class Screen(tk.Tk):
    def __init__(self):
        super().__init__()

        # Database connection
        self.conn = None

        # Setup
        self.title('SQL Master')
        self.iconbitmap(ICON_PATH)
        self.configure(bg=BG_GRAY)
        self.protocol('WM_DELETE_WINDOW', self.quit)

        # Resize
        _width = self.winfo_screenwidth()
        _height = self.winfo_screenheight()
        self.geometry(f'{_width}x{_height}')
        self.state('zoomed')

        # Grid
        self.block_menu = self.block(side='left', fill='y', expand=False)
        self.block_table = self.block(side='top', fill='both', expand=True)
        self.block_script = self.block(side='left', fill='both', expand=True)

        # Fields
        self.create_menu()
        self.conn_form()
        self.textbox = self.textbox()
        self.table = self.table()

# ==================== Fields ==================== #

    def block(self, side, fill, expand):
        """
        Create the Frame widgets.
        """

        _block = tk.Frame(self, bg=BG_WHITE)
        _block.pack(side=side, fill=fill, expand=expand, padx=20, pady=20)

        return _block

    def entry(self, text, disabled='normal'):
        """
        Create the Label and Entry widgets.
        """

        _label = tk.Label(self.block_menu, text=text, bg=BG_WHITE, font=FONT_LABEL)
        _label.pack(anchor='w', padx=10, pady=5)
        _entry = tk.Entry(self.block_menu, width=30, font=FONT_ENTRY, highlightthickness=1)
        _entry.config(state=disabled)
        _entry.pack(padx=10)

        return _entry

    def textbox(self):
        """
        Create the Text widgets.
        """

        _textbox = tk.Text(self.block_script, font=FONT_TEXT, highlightthickness=1, wrap='word')
        _textbox.pack(fill='both', expand=True, padx=10, pady=10)
        _textbox.config(width=20, height=5)

        return _textbox
    
    def table(self):
        """
        Create the Treeview widgets.
        """
                
        _scroll = tk.Scrollbar(self.block_table)
        _scroll.pack(side='right', fill='y')
        
        _table = ttk.Treeview(self.block_table,yscrollcommand=_scroll.set, selectmode="extended")
        _table.pack(anchor='center', fill='both', expand=True, padx=10, pady=10)
        
        _scroll.config(command=_table.yview)
        return _table

# ================================================ #


# ================ Menu and Form ================ #

    def create_menu(self):
        """
        Create the Menu.
        """

        _menu = tk.Menu(self)
        self.config(menu=_menu)

        _menu.add_command(
            label="Run",
            command=lambda: run_script(
                    conn=self.conn,
                    script=self.textbox.get('1.0', 'end-1c'),
                    table=self.table)
                )

    def conn_form(self):
        """
        Create the connection form.
        """

        _data = open_json()

        _label = tk.Label(self.block_menu, text='Connection', bg=BG_WHITE, font=FONT_TITLE)
        _label.pack(anchor='center', pady=10)

        _frame_radio = tk.Frame(self.block_menu, bg=BG_WHITE)
        _frame_radio.pack(anchor='center', pady=10)

        _var = tk.StringVar()
        if _data['db_type']: _var.set(_data['db_type'])
        else: _var.set('mysql')

        _my_psg = tk.Radiobutton(
            _frame_radio,
            text='MySQL',
            value='mysql',
            variable=_var,
            bg=BG_WHITE,
            command=lambda: change_form(widget=self.block_menu, option=_var.get()))
        _my_psg.pack(side='left')

        _my_psg = tk.Radiobutton(
            _frame_radio,
            text='PostgreSQL',
            value='postgresql',
            variable=_var,
            bg=BG_WHITE,
            command=lambda: change_form(widget=self.block_menu, option=_var.get()))
        _my_psg.pack(side='left')

        _sqlite = tk.Radiobutton(
            _frame_radio,
            text='SQLite',
            value='sqlite',
            variable=_var,
            bg=BG_WHITE,
            command=lambda: change_form(widget=self.block_menu, option=_var.get()))
        _sqlite.pack(side='left')

        _host = self.entry(text='Host')
        _database = self.entry(text='Database')
        _user = self.entry(text='User')
        _password = self.entry(text='Password')
        _db_path = self.entry(text='Database path', disabled='disabled')

        _submit = tk.Button(self.block_menu, text='Connect', width=30,
                    command=lambda: self.connect(
                                db_type = _var.get(),
                                host = _host.get(),
                                database = _database.get(),
                                user = _user.get(),
                                password = _password.get(),
                                db_path = _db_path.get()
                                )
                            )
        _submit.pack(anchor='center', pady=20)

        change_form(widget=self.block_menu, option=_data['db_type'], data=_data)

# =============================================== #

# ================== Functions ================== #

    def connect(self, db_type, host, database, user, password, db_path):
        """
        Update the json file and connect to the database.
        """

        update_json(
            db_type=db_type,
            host=host,
            database=database,
            user=user,
            password=password,
            db_path=db_path
            )

        self.conn = Connection()

        if self.conn.error:
            messagebox.showerror('Error', self.conn.error)
            self.conn = None
        else:
            messagebox.showinfo('Info', 'Database successfully connected.')

# =============================================== #
