import hangman
import rock_paper_scissor

run = True
while run:
    choice = int(input("1-->Rock-Paper-Scissor\n2-->Hangman\nWill add more games soon\nGame You want to play: "))
    print()
    print("====================================================================================")
    if choice == 1:
        rock_paper_scissor.start()
    elif choice == 2:
        hangman.start()
    print("====================================================================================")
    answer = input("Want to play another game ? Press any key to select game except q to exit: ")
    if answer.lower() == 'q':
        run = False
    print("=====================================================================================")
