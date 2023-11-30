from UserDAO import UserDAO
from User import User

def filterMale(userGen):
    for user in userGen:
        if user.gender == "Male":
            yield user 
def main():
    dao = UserDAO('./tp06/users_db.db')

    users = dao.findAll()
    filteredUsers = filterMale(users)

    # dao.findAll() | filterMale()
    print(users)
    for user in filteredUsers:
        print(user.last_name,user.email,user.gender)

    for user in filterMale(dao.findAll()):
        print(user.last_name,user.email,user.gender)
    
    u = User(last_name="GAURAT",first_name="Fred",email="fred@toto.com",gender="Male")
    dao.save(u)
if __name__=='__main__':
    main()
