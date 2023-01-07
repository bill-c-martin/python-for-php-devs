# only two loops: for, and while

# for
primes = [2,3,5,7]
for prime in primes:
    print(prime)

# print 0-4
for x in range(5):
    print(x)

# print 3-9
for x in range(3,10):
    print(x)

# print 3,5,7,9
for x in range(3,10,2):
    print(x)

# Print some odd numbers
for i in range(1, 11, 2):
    print(i)

# Iterate each character in a string
for letter in "hello world":
    print(letter)

# Iterate over a list, etc
for name in ["John", "Jane", "Bob"]:
    print(name)

# Print first & last names
person = {"first": "Jane", "last": "Doe"}
for key in person:
    print(person[key])

# while 
count = 0
while count < 5:
    print(count)
    count += 1

# "do" while
while True:
    print(count)
    
    if count < 10:
        break

# breaks
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

# continue
for x in range(10):
    # Check if x is even
    if x % 2 == 0:
        continue
    print(x)

# "else" in for loops
# Prints out 0,1,2,3,4 and then it prints "count value reached 5"
count=0
while(count<5):
    print(count)
    count +=1
else:
    print("count value reached %d" %(count))

# Prints out 1,2,3,4
for i in range(1, 10):
    if(i%5==0):
        break
    print(i)
else:
    print("this is not printed because for loop is terminated because of break but not due to fail in condition")
