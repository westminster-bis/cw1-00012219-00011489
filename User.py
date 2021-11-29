class User:
    deadline = 0

    def __init__(self, name, password, isteacher):
        self.isteacher = isteacher
        self.password = password
        self.name = name


students = list()
teachers = []


def getUSer(usernameOrID, password):
    for student in students:
        if student.ID == usernameOrID and student.password == password:
            return student
    for teacher in teachers:
        if teacher.name == usernameOrID and teacher.password == password:
            return teacher

    return None


class Student(User):

    def __init__(self, name, password, isteacher, studentID, CW_Mark, submissionTime):
        super().__init__(name, password, False)
        self.studentID = studentID
        self.CW_Mark = CW_Mark
        self.submissionTime = submissionTime


class Teacher(User):
    teacherCode = "univer_code2021@wiut"

    def __init__(self, name, password, isteacher, username):
        super().__init__(self, name, password, True)
        self.username = username
