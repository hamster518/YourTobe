from common.database import Database

Database.initialize()
Database.insert('users', {"account":"Larry@gmail.com", "password":"222222","name":"Larry"})

user = Database.find_one('users', {"account":"Larry@gmail.com"})
print(user)