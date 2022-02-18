# array like
# use append() to add new elements
mylist = []
mylist.append(1)
mylist.append('two')
mylist.append(3.0)

for x in mylist:
    print(x)

# or inline it
thatlist = [1,2,3,4]

for x in thatlist:
    print(x)

try:
    print(mylist[5])
except:
    print('but accessing elements that don\'t exist throws exceptions')

# + operator concat's list
even = [2,4,6,8]
odd = [1,3,5,7]
print(even + odd)

# repeat lists
print([1,2,3] * 10)
