import csv
import sqlite3

def main():
    file_name = "./tp06/MOCK_DATA.csv"
    con = sqlite3.connect("./tp06/users_db.db")
    cur = con.cursor()

    with open(file_name, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        sql ="""INSERT INTO users_tbl(first_name,last_name,email,gender,ip_address)
VALUES(?,?,?,?,?)"""

        for row in reader:
            values = list(row.values())[1:]
            cur.execute(sql,values)

    con.commit()
    con.close()

if __name__=='__main__':
    main()
