from tkinter import Entry, Label

def change_form(widget, option, data=None):
    """
    Function that modifies the connection form based on the selected option.
    """
    
    entry = [field for field in widget.winfo_children() if isinstance(field, Entry)]

    if data:
        label = [field for field in widget.winfo_children() if isinstance(field, Label)]

    if option != 'sqlite':
        for field in entry[:-1]:
            field.config(state='normal')
        
        if data:
            for index, field in enumerate(label[1:]):
                key = field.cget('text').lower().replace('database path', 'db_path')
                entry[index].insert('0', data[key])
        
        entry[-1].delete('0', 'end')
        entry[-1].config(state='disabled')
    
    else:
        for field in entry[:-1]:
            field.delete('0', 'end')
            field.config(state='disabled')
        
        entry[-1].config(state='normal')
        
        if data:
            entry[-1].insert('0', data['db_path'])
            