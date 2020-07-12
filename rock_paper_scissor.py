import random
import time

rock = 1
paper = 2
scissors = 3

names = {rock:"Rock", paper:"Paper", scissors:"Scissors"}
rules = {rock:scissors, paper:rock, scissors:paper}

player_score = 0
computer_score = 0

def start():
    print("Let's play a game of Rock, Paper, Scissors.")
    while game():
        pass
    scores()

def game():
    player = move()
    computer = random.randint(1,3)
    result(player, computer)
    return play_game()

def move():
    while True:
        print()
        player = (input("Rock = 1\nPaper = 2\nScissors = 3\nMake a move: "))

        try:
            player = int(player)
            if player in (1,2,3):
                return player
        except:
            pass
        print("Oops! I didn't understand that. Please enter 1,3 or 3.")

def result(player, computer):
    print()
    print("1...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("3!")
    time.sleep(0.5)
    print("Computer threw {} !".format(names[computer]))

    global player_score, computer_score

    if player == computer:
        print("Tie game")
    else:
        if rules[player] == computer:
            print("Your Victory has been assured")
            player_score+=1
        else:
            print("The computer laughts as you realise you have been defeated.")
            computer_score += 1

def play_game():
    answer = input("Would you like to play again? Press any key to continue except q to exit:")
    if answer.lower() == 'q':
        print("Thank you very much for playing our game.See you next time.")
        return False
    else:
        return True

def scores():
    global player_score, computer_score
    print("HIGH SCORES")
    print("Player: ",player_score)
    print("Computer: ",computer_score)

if __name__ == "__main__":
    start()
