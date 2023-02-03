def Game():
    import random
    computer = random.randint(1,3)
    print("Let's play!")
    print('''PLAYERS CHANTING: sicsor ,paper,rock!
    Enter "1" for sicsor
    Enter "2" for paper
    Enter "3" for rock
    YOU'RE PLAYING WITH COMPUTER!''')
    player=int(input())
    if(player != 1 and player != 2 and player != 3):
        print("YOU can only choose betn 1 and 3(including).")
    elif(player==1 and computer==1):
        print("Player : sicsor and Computer: sicsor")
        print("Nobody wins!") 
    elif(player==2 and computer==2):
        print("Player : paper and Computer: paper")
        print("Nobody wins!")     
    elif(player==3 and computer==3):
        print("Player : rock and Computer: rock")
        print("Nobody wins!") 
    elif(player==1 and computer==2):
        print("Player : sicsor and Computer: paper")
        print("YOU WIN!") 
    elif(player==1 and computer==3):
        print("Player : sicsor and Computer: rock")
        print("COMPUTER WIN!") 
    elif(player==2 and computer==1):
        print("Player : paper and Computer: sicsor")
        print("COMPUTER WIN!")
    elif(player==2 and computer==3):
        print("Player : paper and Computer: rock")
        print("YOU WIN!")
    elif(player==3 and computer==1):
        print("Player : rock and Computer: sicsor")
        print("YOU WIN!") 
    elif(player==3 and computer==2):
        print("Player : rock and Computer: paper")
        print("COMPUTER WIN!")                     
print('''Sicsor,Paper and Rock Game:
You are going to play sicsor,paper & rock game with SARDUL.
SICSOR=1
PAPER=2
ROCK=3''')
Game()
    