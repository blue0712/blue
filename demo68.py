class Emp:
    pass


class Engineer(Emp):
    pass


class PM(Engineer):
    pass


class HR(Emp):
    pass


emp1 = Emp()
engineer1 = Engineer()
pm1 = PM()
hr1 = HR()
staffs = [(emp1, "First Employee"), (engineer1, "Chief Engineer"),
          (pm1, "Primary Product Manager"), (hr1, "General Human Resource")]

emp_classes = [Emp, Engineer, PM, HR]

for staff, name in staffs:
    for emp_class in emp_classes:
        isA = isinstance(staff, emp_class)
        message1 = 'is a ' if isA else 'is not a '
        print(name, message1, emp_class.__name__)