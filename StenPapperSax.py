#-- coding: utf-8 --
#Då man kör det här programmet kommer man att få spela det klassiska spelet "Sten, Sax, Påse!" mot datorn.
#Spelaren får själv välja hur många poäng som krävs för att vinna.
#Spelet håller på tills antingen spelaren eller datorn har fått den mängd poäng som krävs för att vinna.




import random


print "*******************"
print "ROCK PAPER SCISSORS"
print "*******************"


#De här variablerna existerar för att lätta upp koden, värdena i form av strings har ingen betydelse för programmet.
HUMAN    = "H"
CPU      = "C"
TIE      = "T"

"""Koden granskar vilken spelare som vann. Man behöver endast skriva ut villkoren för spelarens vinst
i och med att om de inte uppfylls och det inte blir oavgjort så leder det automatiskt till datorns vinst"""
def checkResults(user, computer):
    if user == computer:
        print("Oavgjort!")
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

#Funktionen som printar ut den rätta vinnaren.
def printWinner( humanCount, computerCount ):
    if humanCount > computerCount:
        print( "Du vann spelet!" )
    else:
        print( "Du förlorade spelet." )


#Huvudkoden för spelet som tar hand om de andra funktionerna
def main():
    winningScore = input("Hur många poäng krävs för att vinna?   ")
    
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
