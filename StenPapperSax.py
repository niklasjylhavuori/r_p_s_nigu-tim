#-- coding: utf-8 --
#Då man kör det här programmet kommer man att få spela det klassiska spelet "Sten, Sax, Påse!" mot datorn.
#Spelaren får själv välja hur många poäng som krävs för att vinna.
#Spelet håller på tills antingen spelaren eller datorn har fått den mängd poäng som krävs för att vinna.

#Det kommer att behövas random som måste importeras. Det kommer att krävas att resultaten sparas mellan rundorna.



import random


print "*******************"
print "ROCK PAPER SCISSORS"
print "*******************"
#-- coding: utf-8 --
import random

HUMAN    = "H"
CPU      = "C"
TIE      = "T"

def checkResults(user, computer):
    if user == computer:
        print("It's a tie!")
        return TIE

    elif user == 0 and computer == 1:
        print "Du vann!"
        return HUMAN
    elif user == 1 and computer == 2:
        print "Du vann!"
        return HUMAN
    elif user == 2 and computer == 0:
        print "Du vann!"
        return HUMAN

    print "Du förlorade."
    return CPU

def printWinner( humanCount, computerCount ):
    if humanCount > computerCount:
        print( "Du vann spelet!" )
    else:
        print( "Du förlorade spelet." )



def main():
    winningScore = input("Hur många poäng krävs för att vinna?   ")
    # counters for winning rounds
    humanCount = 0
    computerCount = 0


    while humanCount < winningScore and computerCount < winningScore:
        user = input("Välj:   1:Sten,   2:Sax   3:Papper")
        computer = random.randint(0, 2)
        winner = checkResults(user, computer)
        if winner == HUMAN:
            humanCount += 1
        if winner == CPU:
            computerCount += 1

    printWinner(humanCount, computerCount)


main()
