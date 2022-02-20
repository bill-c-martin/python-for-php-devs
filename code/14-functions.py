# regular function
def my_function():
    print('this is a function')
my_function()

# function with args
def func_with_args(user, greeting):
    print('Hello %s, I wish you %s' %(user, greeting))
func_with_args('John', 'happy birthday')

# function with return
def sum(a,b):
    return a+b
print( sum(2,2) )
