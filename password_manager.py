import random

import pandas as pd

import config


# Use pandas for exercising
class PasswordManager:
    def __init__(self):
        self.df = pd.read_csv(config.PASSWORD_FILE)

    def upsert_entry(self, website, username, password):
        self.df = self.df.append({"website": website, "username": username, "password": password}, ignore_index=True)
        self.df.drop_duplicates(subset=["website"], inplace=True, keep="last")
        self._save_current_entries()

    def delete_entry(self, website):
        self.df.drop(index=self.df[self.df.website == website].index, inplace=True)
        self._save_current_entries()

    def search_entries(self, search_term):
        return self.df.loc[self.df.website.str.contains(search_term), :].to_dict("records")

    def get_entry(self, website):
        records = self.df[self.df.website == website].to_dict("records")
        if records:
            return records[0]
        else:
            return None

    def _save_current_entries(self):
        self.df.to_csv(config.PASSWORD_FILE, index=False)

    def generate_password(self):
        letters = [random.choice(config.SYMBOLS)] + [random.choice(config.NUMBERS)] + [
            random.choice(config.LETTERS)] + [
                      random.choice(config.PASSWORD_LETTERS) for _ in range(0, 10)]
        random.shuffle(letters)
        return "".join(letters)
