#main program
phonebook = {'Chris':'555-1111','katie':'555-2222','Joanne':'555-3333'}
#print(phonebook)
#print(phonebook['Chris'])
#print(phonebook['katie'])
#print(phonebook['cris'])

for key in phonebook:
    print(key ,phonebook[key])

print("values only")
for value in phonebook.values():
    print(value)
print("dictionary items")
for item in phonebook.items():
    print(item)