# string length
x = 'Hello world'
print(len(x))

# character location
print(x.index('o'))

# character counts in a string
print(x.count('l'))

# string slicing
print(x[3:7])

# capture single character
print(x[3])

# slice till end-of-string
print(x[3:])

# slice from beginning-of-string
print(x[:7])

# slicing ends of string
print(x[-3:])

# slicing while stepping
print(x[1:7:2])

# string reverse, using stepping
print(x[::-1])

# upper/lower
print(x.upper())
print(x.lower())

# starts/end with tests
print(x.startswith('Hello'))
print(x.endswith('rld'))

# splitting
print(x.split(" "))
print(len(x.split(" ")))
