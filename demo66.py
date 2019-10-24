class Emp:
    gradeLevel = 6
    def startWork(self):
        pass
    def endWork(self):
        pass
    pass
class RD(Emp):
    pass
class PM(Emp):
    gradeLevel1 = 77
    pass

class PM2(PM):
    pass

print(Emp.gradeLevel, RD.gradeLevel, PM.gradeLevel)

RD.gradeLevel=8

print(Emp.gradeLevel, RD.gradeLevel, PM.gradeLevel)

Emp.gradeLevel=7
print(Emp.gradeLevel, RD.gradeLevel, PM.gradeLevel)

print(PM2.gradeLevel,PM2.gradeLevel1)