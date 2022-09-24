
# c-like, but prepend the tuple set of vars with %..
name = 'john'
print('Hello, %s' % name)

# multiple substitutions look like this
first = 'john'
last = 'smith'
age=22
print('Hello, %s %s, who is %s years old.' % (first, last, age))

# same thing, but with str.format()
first = "John"
last = "Smith"
age = 22
print("Hello, {first} {last}, who is {age} years old.".format(first=first, last=last, age=age) )

# same thing, with f-strings
first = "John"
last = "Smith"
age = 22
print(f'Hello, {first} {last}, who is {age} years old.')

# int vs float vs string
one = 1
two = 2.0
three = 'three'
print("Counting: %d, %f, %s" % (one, two, three))

# floats with fixed digits. Rounds
y = 1.15656565656
print("More: %.8f, Less: %.4f, Even less: %.1f" % (y,y,y))

x = 14
print('Int: %d, lowercase x: %x, uppercase x: %X' % (x,x,x))
