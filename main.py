import Teacher
from Teacher import TeacherClass
import User

print("husan")

def signInMenu():
    while True:
        print("----------------------------------------------------")
        print("| -[1.Teacher]- \t -[2.Student]- \t -[0.Exit]-     |")
        print("----------------------------------------------------")
        option = int(input("choose option: "))
        if option == 1:
            fullName = input("enter your full name(John Smith): ")
            if Teacher.checkTeacher(fullName):
                pass



        elif option == 2:
            pass
        elif option == 0:
            break


def mainMenu():
    while True:
        print("-----Hello to the Student Assessment System")
        print("    -[1.Login]-\t\t -[2.Sign In]- -[0.Exit]-")
        stepcode = int(input("Choose option: "))

        if stepcode == 1:
            print("login menu")
        elif stepcode == 2:
            pass
        elif stepcode == 0:
            break
        else:
            pass


#beginning of the project, front end part
while True:
    # for teacher in Teacher.teachersList:
    #     print("{}+{}".format(teacher.name, teacher.username))
    #     print(teacher.name)

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
        pass
