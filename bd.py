import sqlite3


__connection = None

def get_connection():
    global __connection
    if __connection is None:
        __connection == sqlite3.connect('anceta.bd')
        return __connection