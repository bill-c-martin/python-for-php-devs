# Create a basic class
class Foo:
    def __init__(self, x=5):
        self.x = x
    def bar(self, y = 10):
        self.y = y
        print('baz sets 10')

# Init it
foo = Foo()
foo.bar(10)

# dir() only shows properties and values, but not structure, methods, types
print('dir("test") looks like: ', dir('test'), end='\n\n')
print('dir([1,2,3]) looks like: ', dir([1,2,3]), end='\n\n')
print('dir({"foo": "bar", "biz": "baz"}) looks like: ', dir({'foo': 'bar', 'biz': 'baz'}), end='\n\n')
print('print a Foo class with bar() and an x=5 property looks like: ', dir(foo), '\n\n')

# vars() only shows properties and methods, but not structure, values, types
print('vars(foo) class/obj looks like: ', vars(foo), end='\n\n')

# pprint() only shows structure, state, types, but not methods
from pprint import pprint
pprint('test')
pprint([1,2,3])
pprint({'foo': 'bar', 'biz': 'baz'})
pprint(foo)

from inspect import getmembers
pprint(getmembers(foo))

# But this var_dump pip package shows everything like in PHP: structure, methods, properties, types, keys, values, lengths
# Run this first: pip install var_dump
from var_dump import var_dump
var_dump('test', [1,2,3], {'foo': 'bar', 'biz': 'baz'}, foo)
