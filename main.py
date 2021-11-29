import User

print("-----Hello to the Student Assessment System")
print("    -[1.Login]-\t\t -[Sign In]- ")

stepCode = 123

while stepCode != 0:
    stepcode = int(input("Choose option: "))

    if stepcode == 1:
        print("login menu")
    elif stepcode == 2:
        print("sign in menu")
    else:
        break


def loginMenu():
    while True:
        username = input("Enter your username/ID: ")
        password = input("Enter password: ")
        user = User.getUSer(username, password)
        # if(user.)

def signInMenu():
    while(True):
        print("Sign in As Teacher")