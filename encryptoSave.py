"""
WELCOME TO ENCRYPTOSAVE. QUICK AND EASY SAVE/LOAD FOR PYTHON GAMES!
"""

from itsdangerous import URLSafeSerializer
import os
import sys

"""
Here you need to make a .env file and write (export encryptkey1="{random letters and numbers here}")
"""
encryptkey1 = os.environ['encryptkey1']
encryptkey2 = os.environ['encryptkey1']

def encrypt(data):
  auths=URLSafeSerializer(encryptkey1,encryptkey2)
  return auths.dumps(data)

def decrypt(data):
  auths=URLSafeSerializer(encryptkey1,encryptkey2)
  return auths.loads(data)

class player():

  #you can call internal functions from here (e.g: self.function)

  def __init__(self):

     #example variables
     self.xp = 198
     self.damage = 30
     self.health = 100

#you can make your own player object by calling encryptoSave.player()
p = player()

#call encryptoSave.save(p) to save the player's state
def save(player):

  data = {
    #put all variables you wish to save here
    "xp": player.xp,
    "damage": player.damage,
    "health": player.health
  }

  with open("save.txt", "w") as f:
      f.write(encrypt(data))
      f.close()

#call encryptoSave.load(p) to load saved data
def load(player):

  if os.path.exists("save.txt"):

        with open("save.txt", "r") as f:

            savedData = decrypt(f.read())

            #here you need to retrieve any variables you have saved

            player.xp = savedData['xp']

            player.health = savedData['health']

            player.damage = savedData['damage']

  else:

    sys.exit("ERROR: No Save File Detected, Please Start A New Game")
