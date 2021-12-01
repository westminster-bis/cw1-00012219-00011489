from User import User
import Teacher

teachersList = []


def checkTeacherUsername(username, password):
    for teacher in teachersList:
        if teacher.username == username and teacher.password == password:
            return teacher
    return None


def checkTeacher(fullName):
    for teacher in teachersList:
        if teacher.fullName == fullName:
            return False
    return True


def addTeacher(self):
    teachersList.append(self)
    print("completed successfully")


class TeacherClass(User):
    def __init__(self, full_name, username, password, module_Name):
        super(TeacherClass, self).__init__(full_name, username, password, True)
        self.moduleName = module_Name


teacher1 = TeacherClass("husan", "wiut", "123", "JV")
teachersList.append(teacher1)
