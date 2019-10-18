day_of_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
lengthArray = []
for d in day_of_week:
    lengthArray.append(len(d))
print(lengthArray)

print([len(d) for d in day_of_week])
print([d for d in day_of_week if len(d) > 6])
x1, x2, x3, x4, x5, x6, x7 = day_of_week
print(x1, x3, x5)
print(x2, x4, x6, x7)
number_list = [3, 1, 4, 1, 5, 9, 26, 83, 42, 0, 100, 83, 99]
over30 = sorted(d**2 for d in number_list if d>30)
print(over30)
under50 = sorted((e for e in number_list if e < 50),reverse=True)
print(under50)