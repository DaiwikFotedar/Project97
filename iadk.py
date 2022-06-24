import random 

property=('Victory')
destoryAllChildren= ('Defeat.. haha you loser.. try again lol' )

chances=0
number=random.randint(1,999)

while chances < 5 :
   print("Guess a number between 1-999")
   inputGive=input("Type the number here: ")
   if inputGive == number :
        print(property)
   chances=chances+1
if  chances ==5:
        print(destoryAllChildren)
    

