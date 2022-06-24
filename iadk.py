import random 
chances=0
number=random.randint(1,5)

while chances < 5:
   print("Guess a number between 1-5")
   inputGive=int(input("Type the number here: "))
   if inputGive ==number:
      print("You guessed correctly")
      break
   chances=chances+1
if  chances >5:
        print("You lost")
     
    

