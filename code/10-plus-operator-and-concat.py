one = 1
two = 2
three = one + two
print(three)

# + for stirngs is concat
hello = "hello"
world = "world"
print(hello + world)

# but you can't mix and match
try:
    print(one + hello)
except:
    print("cannot do string + int")
