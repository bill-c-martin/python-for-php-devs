class MyClass:
    variable="foo"

    # constructor
    def __init__(self, number):
        # dynamically declared class member..
        self.number = number

    def do_thing(self):
        print('doing things')

test = MyClass(2)
print(test.variable)
test.do_thing()

print(test.number)

