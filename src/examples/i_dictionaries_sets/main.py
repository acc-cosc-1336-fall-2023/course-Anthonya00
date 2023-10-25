import dictionaries

#main program
phonebook = {}#empty dictionary

dictionaries.add_friend_phonebook('Chris','555-1111', phonebook)
dictionaries.add_friend_phonebook('Chris','555-1111', phonebook)


for name,value in phonebook.items():
    print(name,value)