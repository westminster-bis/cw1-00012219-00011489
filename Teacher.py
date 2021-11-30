from User import User

teachersList = []


def checkTeacher(fullName):
    for teacher in teachersList:
        pass


def addTeacher(self):
    teachersList.append(self)


class TeacherClass(User):

    def __init__(self, full_name, username, password, module_Name):
        super(TeacherClass, self).__init__(full_name, username, password)
        self.moduleName = module_Name


teacher1 = TeacherClass("husan", "wiut", "123", "JV")
print(teacher1.moduleName)
