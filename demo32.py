def sample_variable_arguments(f1, f2, *args):
    print(f'two fixed variable, one is {f1}, another is {f2}')
    for e in args:
        print('variable part:%s' % e)


sample_variable_arguments("hello", "World")
sample_variable_arguments(3.14, 500)
sample_variable_arguments((1, 2), [3, 4, 5])
sample_variable_arguments("sample1", "order", 5, 6, 7, None, 9)
l1 = [5, 6, 7, None, 9]
sample_variable_arguments("sample2", "order", l1)
sample_variable_arguments("sample2", "order", *l1)
t1 = ('Sunday', 'Thursday')
sample_variable_arguments("sample3", "order", *t1)
s1 = set(list('APPLE'))
sample_variable_arguments("sample4", "not-order", *s1)
d1 = {'iphoneX11': 500, 'iphone7': 2000}
sample_variable_arguments("sample5", "a-dictionary", *d1)
sample_variable_arguments("sample5", "a-dictionary", d1)