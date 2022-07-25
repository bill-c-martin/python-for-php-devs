x = 2

# typical conditionals 
print(x == 2)
print(x == 3)
print(x > 1)

# uses and/or, not && or ||
# no parenthesis, and : replaces brackets
name = "john"
age = 23
if name == "john" and age == 23:
    print('Your name is john')
    print('And you are 23 years old')

if name == "john" or name == "rick":
    print("you are either john or rick..")

# What about the and/or vs && and || lazy eval?

# in array checks
if name in ["John","Rick"]:
    print("you are either john or rick..")

# Nested if statements
if name == "john":
    print('Your name is john')
    if age == 23:
        print('And you are 23 years old')

# if/else blocks
# Uses abbeviations for elseif
# blocks defined by indentation
# "pass" is just an empty statement, placeholder..
statement = False
another_statement = True
if statement is True:
    # do something
    pass
elif statement is False:
    # do something else
    pass
else:
    # do yet another thing
    pass

# array comparison
x = [1,2,3]
y = [1,2,3]
z = [3,2,1]
print(x == y)
print(x == z)

# is: matches instances, not values
x = [1,2,3]
y = [1,2,3]
print(x == y) # Prints out True
print(x is y) # Prints out False

# not
print(not False) # Prints out True
print((not False) == (False)) # Prints out False
