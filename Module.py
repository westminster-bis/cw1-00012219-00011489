modules = []


class Module:
    # def __int__(self, name):
    #     self.name = name

    def __init__(self, name):
        self.name = name
        self.deadline = 0


module1 = Module("Computer Science Fundamentals")
modules.append(module1)
module2 = Module("Fundamentals of Programming")
modules.append(module2)
module3 = Module("Introduction to Organisation Behaviour and Management")
modules.append(module3)
module4 = Module("Introduction to Data science and statistics")
modules.append(module4)