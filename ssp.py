#Då man kör det här programmet kommer man att få spela det klassiska spelet "Sten, Sax, Påse!" mot datorn.
#Spelaren får själv välja hur många poäng som krävs för att vinna.
#Spelet håller på tills antingen spelaren eller datorn har fått den mängd poäng som krävs för att vinna.

#Det kommer att behövas random som måste importeras. Det kommer att krävas att resultaten sparas mellan rundorna.


#-- coding: utf-8 --
import random
import time

print "*******************"
print "ROCK PAPER SCISSORS"
print "*******************"
print
print "Regler:"
print "Välj först hur många poäng som krävs för att vinna."
print "Välj sedan 1 för sten, 2 för sax eller 3 för påse."
print "Kom ihåg, sten vinnar sax, sax vinner påse och påse vinner sten."
print 
total_score = input("Hur många poäng krävs för att vinna? ")

user_score = 0
computer_score = 0

def checkResults(user,computer):
    while user_score <= total_score or computer_score <= total_score :
        #Spelaren vinner:
        if user_choice == 0 and computer_choice == 1:
            user_score += 1
            print "Du vann!"
        elif user_choice == 1 and computer_choice == 2:
            user_score += 1
            print "Du vann!"
        elif user_choice == 2 and computer_choice == 0:
            user_score += 1
            print "Du vann!"
        #Datorn vinner:
        else:
            print "Du förlorade."
            computer_choice +=1

def round(): 
user_choice = input("1:Sten, 2:Sax, 3:Påse")
#Kolla om spelarens input är mellan 1-3 (0=sten, 1=sax, 2= påse)
computer_choice = random.randint(0,2)
