#this is the example file which demonstrates some basic functionality

import encryptoSave

p = encryptoSave.player()

#IF YOU PUBLICALLY RELEASE YOUR CODE, DO NOT USE THIS FUNCTION HERE! FIND ANOTHER WAY
encryptoSave.setKey("example key")

name = str(input("What is your name?\n").lower())

encryptoSave.addVar(p, "name", name)

print(p.variables)

encryptoSave.save(p)

encryptoSave.load(p)

print(p.variables["name"])
