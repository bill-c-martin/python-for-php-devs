
# c-like, but prepend the tuple set of vars with %..
name = 'john'
print('Hello, %s' % name)

# multiple substitutions look like this
first = 'john'
last = 'smith'
print('Hello, %s %s' % (first, last))

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
