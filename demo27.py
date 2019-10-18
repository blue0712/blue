day_of_week = ('Sunday', 'Monday')
day_of_week += ('Tuesday',)
print(day_of_week)
print('Wednesday' * 5)
print(('Wednesday',) * 5)
print(day_of_week[0], day_of_week[1:])
print('day' in 'Wednesday')
print('day' in ('Wednesday',))
print('Wednesday' in ('Wednesday',))


def split_head(sequence):
    return sequence[0], sequence[1:]


day_of_week_list = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

head, remaining = split_head(day_of_week_list)
print(type(remaining), remaining)
print(type(head), head)