import pandas as pd

import config


# Use pandas for exercising
class PasswordManager:
    def __init__(self):
        self.df = pd.read_csv(config.PASSWORD_FILE)

    def upsert_entry(self, website, passwd):
        self.df = self.df.append({"website": website, "password": passwd}, ignore_index=True)
        self.df.drop_duplicates(subset=["website"], inplace=True, keep="last")
        self._save_current_entries()

    def delete_entry(self, website):
        self.df.drop(index=self.df[self.df.website == website].index, inplace=True)
        self._save_current_entries()

    def entries_as_dict(self):
        return dict(self.df.values)

    def search_entry_as_dict(self, search_term):
        return dict(self.df.loc[self.df.website.str.contains(search_term), :].values)

    def get_entry(self, website):
        values = self.df[self.df.website == website].values
        print(f"values : {values}")
        if values is not None:
            return self.df[self.df.website == website].values[0]
        return None

    def _save_current_entries(self):
        self.df.to_csv(config.PASSWORD_FILE, index=False)
