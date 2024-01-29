import lib.login as account
## MD5 per la crittografia delle password si può fare direttamente sul db

def user():
    helpString = '''
    q           -- quit the program
    help        -- show commands
    register    -- create a new account
    login       -- enter in your account
    logut       -- exit the account
    delete      -- delete an account
    update      -- update password
    '''
    helpAdminString = '''
    q           -- quit the program
    help        -- show commands
    register    -- create a new account
    login       -- enter in your account
    logut       -- exit the account
    delete      -- delete an account(no passsword required)
    delete all  -- delete all users
    update      -- update password(no password required)
    print users -- show all users
    '''

    isAdmin = False
    isLogged = False
    username = None
    print(helpString)
    while True:
        function = input('>')
        if isAdmin:
            match function:
                case 'help':
                    print(helpAdminString)
                    continue
                case 'delete all':
                    account.deleteAll()
                    continue
                case 'delete':
                    username = input('>> enter username: ')
                    try:
                        account.superDelete(username)
                    except ValueError as err:
                        print(err)
                    continue
                case 'print users':
                    account.printAllUsers()
                    continue
                case 'update':
                    username = input('>> enter username: ')
                    newPassword = input('>> enter password: ')
                    try:
                        account.superUodatePassword(username, newPassword)
                    except ValueError as err:
                        print(err)
                    continue



        match function:
            case 'q':
                return
            
            case 'help':
                print(helpString)

            case 'register':
                if not isLogged:
                    username = input('>> enter username: ')
                    password = input('>> enter password: ')
                    email = input('>> enter email: ')

                    try:
                        account.register(username, password, email)
                    except ValueError as err:
                        print(err)
                else:
                    print('alredy logged')

            case 'login':
                if not isLogged:
                    username = input('>> enter username: ')
                    password = input('>> enter password: ')

                    try:
                        username = account.login(username, password)
                        if username == 'admin':
                            isAdmin = True
                        isLogged = True
                        print('welcome ' + username)
                    except ValueError as err:
                        print(err)
                else:
                    print('alredy logged')

            case 'logout':
                isLogged = False 
                isAdmin = False
                username = None
                print('exited')

            case 'delete':
                if isLogged:
                    try:
                        password = input('>> enter password: ')
                        account.delete(username, password)
                    except ValueError as err:
                        print(err)
                else:
                    print('not logged')

            case 'update':
                if isLogged:
                    try:
                        password = input('>> enter password: ')
                        newPassword = input('>> enter password: ')
                        account.updatePasword(username, password, newPassword)
                    except ValueError as err:
                        print(err)
                else:
                    print('not logged')

            case _:
                print('no such command')

if __name__ == "__main__":
    user()