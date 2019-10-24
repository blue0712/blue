class Emp:
    gradeLevel = 6

    def startWork(self):
        pass

    def endWork(self):
        pass

    pass


class RD(Emp):
    def __init__(self):
        self.currentgrade = self.gradeLevel

    def startWork(self):
        print(f"{self.currentgrade} start to work")

    def endWork(self):
        print(f"{self.currentgrade} finish work")

    def endWork2(self):
        print(f"{self.gradeLevel} finish work")


rd1 = RD()
print(rd1.currentgrade, rd1.gradeLevel, RD.gradeLevel, Emp.gradeLevel)

rd1.currentgrade = 7
print(rd1.currentgrade, rd1.gradeLevel, RD.gradeLevel, Emp.gradeLevel)

rd1.startWork()
rd1.endWork()
rd1.endWork2()