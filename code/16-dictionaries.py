# dictionaries, ie associate arrays, ie json
phonebook = {}
phonebook["John"] = 1231231234
phonebook["Jane"] = 2342342345
phonebook["Bob"] = 3453453456
print(phonebook)

# Better syntax
phonebook2 = {
    "John": 1231231234,
    "Jane": 2342342345,
    "Bob": 3453453456
}
print(phonebook2)

# Iteration over key/val pairs, using .items()
for name, number in phonebook.items():
    print("Phone number of %s: %s" % (name,number))

# Deletions are either "del" or .pop()
del phonebook['John']
phonebook.pop('Jane')
print(phonebook)

