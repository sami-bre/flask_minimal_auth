import sqlite3

DATABASE_FILE_NAME = "test_database.db"

class DbHelper:
    def __init__(self):
        self.file_name = DATABASE_FILE_NAME
        assert (self.file_name.endswith(".db"))
        self.con = sqlite3.connect(self.file_name)

    def setup_database(self):
        cur = self.con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, password TEXT);")
        self.con.commit()

    def get_all_usernames(self):
        cur = self.con.cursor()
        res = cur.execute("SELECT username FROM users")
        # raw is a list of tuples
        raw = res.fetchall()
        usernames = []
        for tup in raw:
            usernames.append(tup[0])
        return usernames

    def username_exists(self, username):
        usernames = self.get_all_usernames()
        return username in usernames

    def register_user(self, username, password):
        cur = self.con.cursor()
        cur.execute(f'INSERT INTO users VALUES ("{username}", "{password}");')
        self.con.commit()

    def close(self):
        self.con.commit()
        self.con.close()

    def password_matches(self, username, password):
        cur = self.con.cursor()
        res = cur.execute(f"SELECT password FROM users WHERE username='{username}';")
        data = res.fetchone()
        print("data is :")
        print(data)
        retrieved_password = data[0]
        return retrieved_password == password
