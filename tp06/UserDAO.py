import sqlite3

class UserDAO:

    def __init__(self,db_file) -> None:
        self.__con = sqlite3.connect(db_file)

    
    def findAll(self):
        cur = self.__con.cursor()

    def __del__(self):
        self.__con.close()