# def checkStudent

# user class
class User:

    def __init__(self, name, password, isTeacher):
        self.isTeacher = isTeacher
        self.password = password
        self.name = name


students = list()
teachers = []


# to get user(teacher or student)
def getUSer(usernameOrID, password):
    for student in students:
        if student.ID == usernameOrID and student.password == password:
            return student
    for teacher in teachers:
        if teacher.name == usernameOrID and teacher.password == password:
            return teacher

    return None


# student class
class Student(User):

    def __init__(self, name, password, isteacher, studentID, CW_Mark, submissionTime):
        super().__init__(name, password, False)
        self.studentID = studentID
        self.CW_Mark = CW_Mark
        self.submissionTime = submissionTime


# to check if it is really teacher with code we are providing
def checkCode(code):
    if code == Teacher.teacherCode:
        return True

    return False


# check teacher existence
def checkTeacher(name):
    for teacher in teachers:
        if teacher.name == name:
            return False

    return True


# adding new teacher


# teacher class
class Teacher(User):
    teacherCode = "univer_code2021@wiut"

    def __init__(self, name, password, username, module_Name):
        super().__init__(name, password, True)
        self.username = username
        self.module_Name = module_Name

    def addTeacher(self, password, username, moduleName):
        teacher = Teacher(self, password, username, moduleName)
        teachers.append(teacher)
        print("completed successfully")
        return teacher
