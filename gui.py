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

        input_search = Entry()
        input_search.grid(column=1, row=0)

        # list
        list_passwd = Listbox()
        list_passwd.grid(column=1, row=1)
        self.list_passwd = list_passwd
        self._load_entries()
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

    def _on_search_entry(self):
        pass

    def _on_click_generate_password(self):
        pass

    def _on_click_entry(self, evt):
        w = evt.widget
        index = int(w.curselection()[0])
        value = w.get(index)
        website, password = self.password_manager.get_entry(value)
        self.input_website.delete(0, END)
        self.input_website.insert(0, website)
        self.input_passwd.delete(0, END)
        self.input_passwd.insert(0, password)

    def _load_entries(self):
        self.entries = self.password_manager.entries_as_dict()
        self.list_passwd.delete(0, END)
        for idx, entry in enumerate(self.entries.items()):
            self.list_passwd.insert(idx, entry[0])

    def display(self):
        self.root.mainloop()
