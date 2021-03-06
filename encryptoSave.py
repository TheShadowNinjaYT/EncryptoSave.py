"""
EncryptoSave: Fast Loading At Your Fingertips! (GIT REPO: https://github.com/TheShadowNinjaYT/EncryptoSave.py)
"""

from itsdangerous import URLSafeSerializer
import os
import sys

key1 = ""

#sets the key from another file
def setKey(key):

  global key1

  key1 = key

encryptkey1 = key1
encryptkey2 = key1

#it is not neccessary to call these! they are already at work
def encrypt(data):
  auths=URLSafeSerializer(encryptkey1,encryptkey2)
  return auths.dumps(data)

def decrypt(data):
  auths=URLSafeSerializer(encryptkey1,encryptkey2)
  return auths.loads(data)

class player():

  #you can call internal functions from here (e.g: self.function)

  def __init__(self):

     #Don't touch this! It is required to track all data!
     self.variables = {
       
     }

#you can make your own player object by calling encryptoSave.player()
p = player()

def addVar(player, varname, value):

  player.variables[varname] = value

#call encryptoSave.save(p) to save the player's state
def save(player):

  data = player.variables

  with open("save.txt", "w") as f:
      f.write(encrypt(data))
      f.close()

#call encryptoSave.load(p) to load saved data
def load(player):

  if os.path.exists("save.txt"):

        with open("save.txt", "r") as f:

            savedData = decrypt(f.read())

            #here it will retrieve any variables you have saved

            player.variables = savedData

  else:

    sys.exit("ERROR: No Save File Detected, Please Start A New Game")
