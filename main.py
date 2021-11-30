import Teacher
from Teacher import TeacherClass
import User
import Module
import Student
from Student import StudentClass


def signInMenu():
    while True:
        print("----------------------------------------------------")
        print("| -[1.Teacher]- \t -[2.Student]- \t -[0.Exit]-     |")
        print("----------------------------------------------------")
        option = int(input("choose option: "))
        if option == 1:
            fullName = input("enter your full name(John Smith): ")
            if Teacher.checkTeacher(fullName):
                username = input("enter username: ")
                password = input("enter password: ")
                Module.printModules()
                option = int(input("choose option: "))
                moduleName = Module.modules[option - 1].name
                teacher = TeacherClass(fullName, username, password, moduleName)
                Teacher.addTeacher(teacher)
        elif option == 2:
            while True:
                studentID = input("enter your studentID(000xxxxx): ")
                if Student.checkIDStatus(studentID) and Student.checkStudent(studentID):
                    fullName = input("enter your full name(John Smith): ")
                    password = input("enter password: ")
                    student = StudentClass(fullName, studentID, password)
                    Student.addStudent(student)
                    break
                else:
                    print("invalid patterns")
                    print("----------------------------------")
                    print(" -[1.Try Again]- \t\t -[0.Exit]- ")
                    print("----------------------------------")
                    option = int(input("choose option: "))
                    if option == 0:
                        break

        elif option == 0:
            break


def mainMenu():
    while True:
        print("------------------------Hello to the Student Assessment System----------------------------")
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


# beginning of the project, front end part
while True:
    # for teacher in Teacher.teachersList:
    #     print("{}+{}".format(teacher.name, teacher.username))
    #     print(teacher.name)
    for teacher in Teacher.teachersList:
        print("{} + {}".format(teacher.fullName, teacher.isTeacher))

    print("-----Hello to the Student Assessment System")
    print("    -[1.Login]-\t\t -[2.Sign In]- \t\t -[0.Exit]-")
    stepcode = int(input("Choose option: "))

    if stepcode == 1:
        print("login menu")
    elif stepcode == 2:
        signInMenu()

    elif stepcode == 0:
        break
    else:
        pass
