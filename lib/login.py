import lib.db_lib as db 

def register(username, password, email):
    if db.checkUsername(username):
        raise ValueError('username: ' + username +' alredy exists')
    
    db.add_user(username, password, email)



def login(username, password):
    users_list = db.get_list_record()
    users_list.keys()

    if not db.checkUsername(username):
        raise ValueError('username: ' + username +' does not exists')
         
    id = db.getIdFromUsername(username)
    if users_list[id]['password'] == password:
        return username
    else:
        raise ValueError('wrong password')



def delete(username, password):
    if username == 'admin':
        raise ValueError('can not delete admin')
    users_list = db.get_list_record()
    users_list.keys()

    id = db.getIdFromUsername(username)
    if users_list[id]['password'] != password:
        raise ValueError('wrong password')
    
    db.delete(id, username)

def superDelete(username):
    users_list = db.get_list_record()
    users_list.keys()

    if not db.checkUsername(username):
        raise ValueError('username: ' + username +' does not exists')
    db.delete(db.getIdFromUsername(username), username)

def deleteAll():
    db.delete_all()



def updatePasword(username, password, newPassword):
    users_list = db.get_list_record()
    users_list.keys()
    
    id = db.getIdFromUsername(username)

    if users_list[id]['password'] != password:
        raise ValueError('wrong password')
        
    db.update_password(id, newPassword)

def superUodatePassword(username, newPassword):
    users_list = db.get_list_record()
    users_list.keys()

    if not db.checkUsername(username):
        raise ValueError('username: ' + username +' does not exists')
    db.update_password(db.getIdFromUsername(username), newPassword)        



def printAllUsers():
    users = db.get_list_record()
    for user in users:
        print('id: ' + str(user) +' - '+ str(users[user])) 


if __name__ == "__main__":
    register()
    delete()