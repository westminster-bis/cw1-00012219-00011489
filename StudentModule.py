student_Modules = []


def checkCwSubmitted(studentModule):
    for studentModule1 in student_Modules:
        if studentModule1.studentName == studentModule.studentName:
            if studentModule1.moduleName == studentModule.moduleName:
                return False

    return True


def submitCW(studentID, mark):
    pass



def add(studentModule):
    student_Modules.append(studentModule)
    print("completed successfully!")


class StudentModule:
    def init(self, studentName, moduleName):
        self.studentName = studentName
        self.moduleName = moduleName
        self.submitted = False
        self.mark = 0
