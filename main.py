import Teacher
from Teacher import TeacherClass
import User
import Module
import Student
from Student import StudentClass


# LOGIN MENU
def loginMenu():
    while True:
        print("----------------------------------------------------")
        print("| -[1.Teacher]- \t -[2.Student]- \t -[0.Exit]-     |")
        print("----------------------------------------------------")
        option = int(input("choose option: "))
        if option == 1:
            username = input("enter your username: ")
            password = input("enter your password: ")
            teacher = Teacher.checkTeacherUsername(username, password)
            if teacher is not None:
                teacherMenu(teacher)
            else:
                print("invalid patterns")
        elif option == 2:
            studentID = input("enter your username: ")
            password = input("enter your password: ")
            student = Student.checkStudent(studentID, password)
            if student is not None:
                studentMenu(student)
            else:
                print("invalid patterns")


# SIGN IN MENU
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


# TEACHER MENU
def teacherMenu(teacher):
    while True:
        print("1.Set deadline\t 2.See late Submission claims\t 0.Exit")
        option = int(input("choose option: "))
        if option == 1:
            module = Module.getModule(teacher.moduleName)
            if module.deadlineDate == 0:
                print("----------------{}-----------------".format(teacher.moduleName))
                deadlineDate = int(input("choose the date of deadline: "))
                deadlineTime = int(input("choose the time of deadline"))
                Module.setDeadline(module, deadlineDate, deadlineTime)
                print("successfully completed")
            else:
                print("this module already has deadline")
        elif option == 2:
            pass
        elif option == 0:
            break


# STUDENT MENU
def studentMenu(student):
    while True:
        print("1.Enroll course\t 2.My Marks\t 0.Exit")
        option = int(input("choose option: "))
        if option == 1:
            Module.printModules()
            option2 = int(input("choose option: "))
            module = Module.modules[option2 - 1]
            pass
        elif option == 2:
            pass
        elif option == 0:
            break


def moduleSubmissionMenu(student, module):
    pass


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
