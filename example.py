import encryptoSave

p = encryptoSave.player()

encryptoSave.save(p)

encryptoSave.load(p)

print(p.xp)
