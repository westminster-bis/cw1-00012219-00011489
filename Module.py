modules = []


class Module:
    # def __int__(self, name):
    #     self.name = name

    def __init__(self, name):
        self.name = name
        self.deadlineDate = 0
        self.deadlineTime = 0

def setDeadline(moduleObj, deadlineDate, deadlineTime):
    moduleObj.deadlineDate = deadlineDate
    moduleObj.deadlineTime = deadlineTime


def printModules():
    ind = 1
    print("---------------Available modules---------------")
    for module in modules:
        print("{}.{}".format(ind, module.name))
        ind += 1
    print("-----------------------------------------------")


def getModule(moduleName):
    for module in modules:
        if module.name == moduleName:
            return module
    return None

# modules that level 4 students have
module1 = Module("Computer Science Fundamentals")
modules.append(module1)
module2 = Module("Fundamentals of Programming")
modules.append(module2)
module3 = Module("Introduction to Organisation Behaviour and Management")
modules.append(module3)
module4 = Module("Introduction to Data science and statistics")
modules.append(module4)
