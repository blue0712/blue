class Team:
    name = 'normal team'


t1 = Team()
t2 = Team()
print(t1.name, t2.name, Team.name)

t1.name = 'R&D team'
print(t1.name, t2.name, Team.name)

del t1.name
print(t1.name, t2.name, Team.name)

t1.size=7
print(t1.size, )# no Team.size