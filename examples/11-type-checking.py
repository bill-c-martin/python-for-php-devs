import string

mystring = 'hello'
myfloat = 10.0 
myint = 20 

# Determining types with type()
print("mystring is a " + type(mystring).__name__ )
print("myfloat is a " + type(myfloat).__name__)
print("myint is an " + type(myint).__name__)

# Conditionally check types with isinstance()
if isinstance(mystring, str):
    print("String: %s" % mystring)
if isinstance(myfloat, float):
    print("Float: %f" % myfloat)
if isinstance(myint, int):
    print("Integer: %d" % myint)

# Conditionally checking values
if mystring == "hello":
    print("mystring is: %s" % mystring)
if myfloat == 10.0:
    print("myfloat is: 10.0")
if myint == 20:
    print("myint is: 20")

# Conditionally checking values across types
if myfloat == 10:
    print("although myfloat = 10.0, myfloat == 10 too")
if myint == 20.0:
    print("although myint = 20, myint == 20.0 too")

