from datetime import datetime

now = datetime.now()
print("using str:{}".format(str(now)))
print("using repr:{}".format(repr(now)))
print("using default:{}".format(now))
print(now)
print([now])
print((now,))
print((now))
print({now})
print({'k1': now})

# Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)] on win32
# from datetime import datetime
# now = datetime.now()
# now
# datetime.datetime(2019, 10, 23, 10, 0, 2, 537602)