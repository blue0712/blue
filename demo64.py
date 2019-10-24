class Team:
    member = 7

    def working_hour(self):
        return self.day

    def all_working_hour(self):
        self.day = 7
        return self.member * self.day

    @staticmethod
    def calculate(x, y):
        return x * y * 2
    @classmethod
    def getMember(cls):
        return cls.member


t1 = Team()
print(t1.all_working_hour())

print(t1.working_hour())
print(Team.calculate(3,2))
print(Team.getMember())