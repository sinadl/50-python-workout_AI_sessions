users = {
    "admin": "admin123",
    "sina": "python2025",
    "alice": "wonderland",
    "bob": "secure456",
    "charlie": "charlie789",
    "david": "pass1234",
    "emma": "emma2024",
    "john": "johnsmith",
    "mary": "mary321",
    "guest": "guest"
}

def login_sim():
    print('please enter your username and password:')

    while True:
        
        username = input('Username:')
        password = input('Password:')
        
        if not username or not password:
            print('password and username are required')
            break
        elif username and password:
            if username in users:
                if users[username] == password:
                    print('You have successfuly logged in')
                    break
                else:
                    print('your password is wrong')
            else:
                print(f'There is no {username} here!!!')
                
login_sim()