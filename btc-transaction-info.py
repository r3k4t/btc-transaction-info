from bitcoin import *

os.system("clear")

print ("============================================")
print ("           Btc Transaction Info             ")
print ("============================================")
print ("      Author : Rahat Khan Tusar(rkt)        ")
print ("      Github : https://github.com/r3k4t     ")
print ("============================================")

a_valid_bitcoin_address = raw_input("Enter a valid bitcoin address :")
print (history(a_valid_bitcoin_address))
