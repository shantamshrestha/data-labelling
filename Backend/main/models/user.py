from main.models.db import conn

cursor = conn.cursor()

def login(username,password):
    cmd = "SELECT ID FROM Users WHERE USERNAME = '%s' and PASSWORD = '%s'" % (username,password)
    cursor.execute(cmd)
    id = cursor.fetchone()
    if id:
        return id[0]
    else:
        return None
