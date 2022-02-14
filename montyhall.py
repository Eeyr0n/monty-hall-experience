import random
import time


win = 0
lose = 0

def getPlayerDoor():
    global pick
    pick = ''
    while not (pick == 1 or pick == 2 or pick == 3):
        print('Please pick what door you would like to pick.')
        pick = int(input())
        
def getPlayerName():
    print('Welcome to the famous Monty Hall problem\nToday we are joined by uhh, What\'s your name again?')
    name = input()
    print('Oh yes, how could I forget your name '+ name.title() +' hahaha. Now, shall we get on with the game then.')
    
def revealGoat():
    global door
    global goat
    door = [1, 2, 3]
    goat = [1, 2, 3]
    door = random.choice(door)
    goat = random.choice(goat)
    door = int(door)
    goat = int(goat)
    if goat != pick and goat != door:
        goat = str(goat)
        print('Behind door number ' + goat + ' ,lies a goat.')
    else:
        revealGoat()


def whereIsCar():
    global lose
    global win
    print('Now, I am giving you the chance to switch, would you like to? y/n')
    switch = input()
    # In here, I just used common knowledge wherein if the choice is equal to the car but then the player switches, he will get the goat and vice versa.
    if switch.lower().startswith('y'):
        if door == pick:
            print('You took the switch and...')
            time.sleep(1)
            print('you got yourself a goat.')
            lose += 1
        elif pick != door:
            print('You took the switch and...')
            time.sleep(1)
            print('you got yourself a car.')
            win += 1
    elif switch.lower().startswith('n'):
        if pick != door:
            print('You stuck with your choice and...')
            time.sleep(1)
            print('you got yourself a goat.')
            lose += 1
        elif door == pick:
            print('You stuck with your choice and...')
            time.sleep(1)
            print('you got yourself a car.')
            win += 1
            
def playAgain():
    play = ''
    while not (play.startswith('n') or play.startswith('y')):
        print('Would you like to play again?')
        play = input()
    if play.lower().startswith('y'):
        True
    elif play.lower().startswith('n'):
        global win
        global lose
        win = str(win)
        lose = str(lose)
        print('In total, you won ' + win + ' times and you lost ' + lose + ' times.')
        exit()

while True:
    getPlayerName()
    getPlayerDoor()
    revealGoat()
    whereIsCar()
    playAgain()