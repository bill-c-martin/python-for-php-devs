x = 9.99

# Logical operators 
print(x > 9 and x < 10)          # True
print(x < 10 or x > 10)          # True
print( not (x > 9 and x < 10) )  # true

# == works like php's ===, but not int/bool/float vs str
print(1 == '1')
print(1 == 1.0)
print(1 == True)

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

# in and not in
x = [1,2,3]
y = "Hello world"

if 1 in x:       print('1 is in [1,2,3]')
if 6 not in x:   print('6 is not in [1,2,3]')
if "Hello" in y: print('"Hello" is in "Hello World"')
if "H" in y:     print('And so is "H"')
if "X" not in y: print('But "X" is not')
    
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

# Conditional expressions
print("Your name is: ")
print( "john" if name == "john" else "unknown" )

# array comparison
x = [1,2,3]
y = [1,2,3]
z = [3,2,1]
print(x == y)
print(x == z)

# is: matches instances, not values
a = [1,2,3]
b = [1,2,3]
print(a == b) # Prints out True. Same values.
print(a is b) # Prints out False. Different memory addresses.

x = [1,2,3]
y = x
print(x == y) # Prints out True. Same values.
print(x is y) # Prints out True too. Same memory address.

x = 1
y = 1
print(x == y)       # Prints out True. Same values.
print(x is y)       # Prints out.. True.
print(id(x), id(y)) # Print out.. same memory addresses!

# not
print(not False) # Prints out True
print((not False) == (False)) # Prints out False
