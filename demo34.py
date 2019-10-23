def sample_args_call(var1, var2, var3):
    print("1st:{},2nd:{},3rd:{}".format(var1, var2, var3))


sample_args_call("Intel", "Qualcomm", 'ARM')
sample_args_call("Mark", *("John", "Ken"))
sample_args_call("iphone", *["ipad", 'apple watch'])
sample_args_call(*["ipad", 'apple watch'], "iphone")


def describe(name, duration, location):
    print("{}:{}hr/{}".format(name, duration, location))


describe(name="BDPY", duration=35, location="Taipei")
describe(name="PYKT", duration=35, location="Hsinchu")
newCourse = {'name': 'PYKT', 'duration': 35,
             'location': 'Taipei'}
describe(**newCourse)