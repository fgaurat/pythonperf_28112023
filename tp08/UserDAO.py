import sqlite3
from User import User
class UserDAO:

    def __init__(self,db_file) -> None:
        self.__con = sqlite3.connect(db_file)

    
    def findAll(self):
        # users = []
        cur = self.__con.cursor()
        sql="SELECT * FROM users_tbl"
        rs = cur.execute(sql)
        for row in rs.fetchall():
            u = User(*row)
            yield u
            # users.append(u)

        # return users
    

    def save(self,user):
        cur = self.__con.cursor()
        sql ="""INSERT INTO users_tbl(first_name,last_name,email,gender,ip_address)
VALUES(?,?,?,?,?)""" 
        cur.execute(sql,[user.first_name,user.last_name,user.email,user.gender,user.ip_address])       
        cur = self.__con.commit()

        
    def __del__(self):
        self.__con.close()