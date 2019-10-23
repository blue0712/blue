def sample_key_arguments(fix1, fix2, **kwargs):
    print(f"fix part {fix1}, {fix2}")
    for k, v in kwargs.items():
        print(f"{k} has value= {v}")
        print(f"[{k}] has value= {v}")

sample_key_arguments("hello", "world")
sample_key_arguments("putsome ", "key,value", title='RD', level=6, location='Taipei')
course = {"title": "BDPY", "duration": 35, "location": 'taipei',
          'instructor': "Mark"}
#sample_key_arguments("put a dictionary", "with two *", course)  error
sample_key_arguments("put a dictionary", "with two *", **course)