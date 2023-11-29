def main():
    dao = UserDAO('./tp06/users_db.db')

    users = dao.findAll()
    for user in users:
        print(user.name,user.email)

        
if __name__=='__main__':
    main()
