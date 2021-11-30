import Module
import User
import main


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
            name = input("enter name: ")
            if User.checkTeacher(name):
                username = input("enter your username: ")
                password = input("enter password: ")
                code = input("Enter university code for teachers: ")
                if User.checkCode(code):
                    ind = 1
                    print("------------------------")
                    for module in Module.modules:
                        print("\t{}.{}".format(ind, module.name))
                        ind += 1
                    print("------------------------")
                    option = int(input("choose option: "))
                    moduleObj = Module.modules[option - 1]
                    moduleName = moduleObj.name
                    # teacher = User.Teacher()
                    teacher = User.Teacher.addTeacher(name, password, username, moduleName)
                    teacherMenu(teacher, moduleObj)
                    break
                else:
                    print("invalid code")
            else:
                print("user already exist")

        elif option == 2:
            studentID = input("enter your student ID(000xxxxx): ")
            if studentID[0:3] != "000":
                print("invalid ID")
            elif User.checkTeacher(studentID):
                pass

        else:
            break


def teacherMenu(teacher, moduleObj):
    while True:
        print("\t-[1.Set Module DeadLine]-\t -[2.See LS reasons]-\t -[0.Exit]- ")
        option = int(input("choose option: "))
        if option == 1:
            set_Module_deadline(moduleObj)
            break
        elif option == 2:
            pass
        else:
            break


def set_Module_deadline(moduleObj):
    deadlineDate = int(input("enter date of the deadline: "))
    moduleObj.deadlineDate = deadlineDate
    deadlineTime = int(input("enter the time of deadline: "))
    moduleObj.deadlineTime = deadlineTime


def mainMenu():
    while True:
        print("-----Hello to the Student Assessment System")
        print("    -[1.Login]-\t\t -[2.Sign In]- -[0.Exit]-")
        stepcode = int(input("Choose option: "))

        if stepcode == 1:
            print("login menu")
        elif stepcode == 2:
            signInMenu()
        elif stepcode == 0:
            break
        else:
            main.mainMenu()


# beginning of the project, front end part
while True:
    for teacher in User.teachers:
        print("{}+{}".format(teacher.name, teacher.username))
        print(teacher.name)

    print("-----Hello to the Student Assessment System")
    print("    -[1.Login]-\t\t -[2.Sign In]- -[0.Exit]-")
    stepcode = int(input("Choose option: "))

    if stepcode == 1:
        print("login menu")
    elif stepcode == 2:
        signInMenu()
    elif stepcode == 0:
        break
    else:
        main.mainMenu()
