import os, sys

print(os.getcwd())

dir1 = 'trial'

#os.rmdir(dir1)
os.mkdir(dir1)
os.chdir(dir1)
print("now, we have dir:{}".format(os.getcwd()))
os.chdir("..")
os.rmdir(dir1)
print(sys.executable)
for arg in sys.argv:
    print(arg)

# python demo36.py
# python demo36.py -a -b c=d efg