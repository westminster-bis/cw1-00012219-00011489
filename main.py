import User
import main

print("-----Hello to the Student Assessment System")
print("    -[1.Login]-\t\t -[Sign In]- ")

stepCode = 123

print("user2 has connected")


def loginMenu():
    while True:
        username = input("Enter your username/ID: ")
        password = input("Enter password: ")
        user = User.getUSer(username, password)
        # if(user.)


def signInMenu():
    while True:
        print(" -[1.Sign in As Teacher]- \t\t -[2.Sign in As Student]- \t\t -[0.Exit]-")
        option = int(input("Choose option: "))
        if option == 1:
            username = input("enter username: ")
            if User.checkTeacher(username):
                password = input("enter password: ")
                code = input("Enter university code for teachers: ")
                if User.checkCode(code):
                    create_Module()

                else:
                    print("invalid code")
            else:
                print("user already exist")


def create_Module():
    moduleName = input("enter module Name: ")


while stepCode != 0:
    stepcode = int(input("Choose option: "))

    if stepcode == 1:
        print("login menu")
    elif stepcode == 2:
        signInMenu()
    else:
        break
