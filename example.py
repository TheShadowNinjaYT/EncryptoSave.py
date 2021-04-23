#this is the example file which demonstrates some basic functionality

import encryptoSave
import random

p = encryptoSave.player()

#IF YOU PUBLICALLY RELEASE YOUR CODE, DO NOT USE THIS FUNCTION HERE! FIND ANOTHER WAY
encryptoSave.setKey("example key")

encryptoSave.addVar(p, "xp", random.randint(1,1000))

print(p.variables)

encryptoSave.save(p)

encryptoSave.load(p)

print(p.variables["xp"])
