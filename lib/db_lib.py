from os.path import join
import sqlite3

def connect_db():
    filename_db = join("database", "autenticazione.db")
    conn = sqlite3.connect(filename_db)
    conn.row_factory = sqlite3.Row
    return conn

def add_user(username, password, email):
    try:
        conn = connect_db()

        cur = conn.cursor()
        sqlcommand = 'INSERT INTO Utenti(user_name, _password, email) VALUES (?, ?, ?)'
        cur.execute(sqlcommand, (username, password, email))
        conn.commit()
    except sqlite3.Error as error:
        print(f'Error in insert operation! {error.args}')
    finally:
        conn.close()



def get_record():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("select * from Utenti")
    return cur.fetchall()



def get_list_record():
    record = get_record()
    list_record = {}
    for user in record:
        list_record[user[0]] = {'username':user[1], 'password':user[2], 'email':user[3]}
    return list_record



def delete_all():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("DELETE FROM Utenti WHERE NOT user_name = 'admin'")
    conn.commit()
    print("all users were deleted succesfully")



def delete(id, username):
    
    conn = connect_db()
    cur = conn.cursor()
    sqlcommand = "DELETE FROM Utenti WHERE ID = ?"
    cur.execute(sqlcommand, (id,))
    conn.commit()
    print("user "+ username +" was deleted succesfully")



def update_password(id, newPassword):
    conn = connect_db()
    cur = conn.cursor()
    sqlcommand = "UPDATE Utenti SET _password = ? WHERE ID = ?"
    cur.execute(sqlcommand, (newPassword, id,))
    conn.commit()
    print("password updated")



def checkUsername(username):
    users_list = get_list_record()
    isUsernamePresent = False
    for tempId in users_list:
        if users_list[tempId]['username'] == username:
            isUsernamePresent = True
            break
    return isUsernamePresent
    


def getIdFromUsername(username):
    users_list = get_list_record()
    for tempId in users_list:
        if users_list[tempId]['username'] == username:
            return tempId
    return None
    
if __name__ == '__main__':
    delete_all()