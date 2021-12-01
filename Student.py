from User import User

studentsList = []


def addStudent(student):
    studentsList.append(student)
    print("successfully completed")


def checkStudent(studentID, password):
    for student12 in studentsList:
        if student12.username == studentID and student12.password == password:
            return student12
    return None


def checkIDStatus(studentID):
    if studentID[0:3] == "000":
        if len(studentID) == 8:
            return True

    return False


def checkStudent(studentID):
    for student in studentsList:
        if student.username == studentID:
            return False
    return True


class StudentClass(User):
    overallMark = 0

    def __init__(self, full_name, studentID, password):
        super().__init__(full_name, studentID, password, False)

    # OVERALL MARK SETTER
    def overall_Mark(self, overallMark):
        self.overallMark = overallMark


student1 = StudentClass("Husan Xolmatov", "00011489", "1234")
studentsList.append(student1)