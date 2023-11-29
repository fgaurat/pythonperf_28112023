import sqlite3
from User import User
class UserDAO:

    def __init__(self,db_file) -> None:
        self.__con = sqlite3.connect(db_file)

    
    def findAll(self):
        users = []
        cur = self.__con.cursor()
        sql="SELECT * FROM users_tbl"
        rs = cur.execute(sql)
        for row in rs.fetchall():
            u = User(*row)
            users.append(u)

        return users
    
    
    def __del__(self):
        self.__con.close()