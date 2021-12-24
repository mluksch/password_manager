from tkinter import *

import config
from password_manager import PasswordManager


class Gui:
    def __init__(self, password_manager: PasswordManager):
        self.password_manager = password_manager
        root = Tk()
        root.wm_title("Password-Manager")
        root.minsize(width=config.WIDTH, height=config.HEIGHT)
        self.root = root

        # search field
        lbl_search = Label(text="Search Website")
        lbl_search.grid(column=0, row=0)

        self.var_search_term = StringVar()
        input_search = Entry(root, textvariable=self.var_search_term)
        self.var_search_term.trace_add("write", self._on_search_entry)
        input_search.grid(column=1, row=0)
        self.input_search = input_search
        self.input_search.focus()

        # list
        list_passwd = Listbox()
        list_passwd.grid(column=1, row=1)
        self.list_entries = list_passwd
        self._update_list()
        list_passwd.bind('<<ListboxSelect>>', self._on_click_entry)

        # Website field
        lbl_website = Label(text="Website")
        lbl_website.grid(row=2, column=0)

        input_website = Entry()
        input_website.grid(row=2, column=1)
        self.input_website = input_website

        # Password field / Generate button
        lbl_passwd = Label(text="Password")
        lbl_passwd.grid(row=3, column=0)

        input_passwd = Entry()
        input_passwd.grid(row=3, column=1)
        self.input_passwd = input_passwd

        # button add
        btn_upsert_entry = Button(text="Upsert Entry", command=self._on_click_add_entry)
        btn_upsert_entry.grid(row=2, column=2)

        # button delete
        btn_delete_entry = Button(text="Delete", command=self._on_click_delete_entry)
        btn_delete_entry.grid(row=3, column=2)

    # gui event handlers
    def _on_click_add_entry(self):
        website = self.input_website.get()
        password = self.input_passwd.get()
        self.password_manager.upsert_entry(website, password)

    def _on_click_delete_entry(self):
        website = self.input_website.get()
        self.password_manager.delete_entry(website)
        self._update_list()
        self.input_website.delete(0, END)
        self.input_passwd.delete(0, END)

    def _update_list(self):
        search_term = self.input_search.get()
        items = self.password_manager.search_entry_as_dict(search_term=search_term).items()
        self.list_entries.delete(0, END)
        for idx, entry in enumerate(items):
            self.list_entries.insert(idx, entry[0])

    def _on_search_entry(self, a, b, c):
        print("_on_search_entry")
        search_term = self.input_search.get()
        result = self.password_manager.search_entry_as_dict(search_term=search_term)
        self.list_entries.delete(0, END)
        for idx, item in enumerate(result.items()):
            self.list_entries.insert(idx, item[0])

    def _on_click_generate_password(self):
        pass

    def _on_click_entry(self, evt):
        w = evt.widget
        if len(w.curselection()) > 0:
            index = int(w.curselection()[0])
            value = w.get(index)
            entry = self.password_manager.get_entry(value)
            if entry is not None:
                (website, password) = entry
                self.input_website.delete(0, END)
                self.input_website.insert(0, website)
                self.input_passwd.delete(0, END)
                self.input_passwd.insert(0, password)

    def display(self):
        self.root.mainloop()
