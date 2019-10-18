class Foo():
    def __init__(self,age,name):
        self.age = age
        self.name = name
    pass
    def __str__(self):
        return f'{self.name} is {self.age} years old.'
    def __repr__(self):
        return f'name=[{self.name}], age=[{self.age}]'

f1=Foo(43,'KEN')
f2=Foo(44,'john')
print(type(f1),f1)
print(f'{f1}')
print(repr(f1))
print(r'{f1}')
print('%s,%r' % (f1, f1))
print(f'{f1}',f'{f2}')
print('{0!r},{0!s},{0!a}'.format(f1))
