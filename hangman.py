import random
def hangman():
    word = random.choice(["pickok",'little','tiger','superman','thor','pockemon','avenger','water','earth','cricket'])
    validlatters = 'abcdefghijklmnopqrstuvwxyz'
    turns = 10
    guessmade = ''
    while len(word) > 0:
        main = ""
        missed = 0
        for letter in word:
            if letter in guessmade:
                main = main + letter
            else:
                main = main + "_"+""
        if main == word:
            print(main)
            print("You win!")
            break

        print("Guess the word :",main)
        guess = input()

        if guess in validlatters:
            guessmade = guessmade + guess
        else:
            print("Enter a valid character")
            guess = input()

        if guess not in word:
            turns = turns - 1
            if turns == 9:
                print("9 turn left")
                print(" ----------")
            if turns == 8:
                print("8 turn left")
                print(" ----------")
                print("     O     ")
            if turns == 7:
                print("7 turn left")
                print(" ----------")
                print("     O     ")
                print("     |     ")
            if turns == 6:
                print("6 turn left")
                print(" ----------")
                print("     O     ")
                print("     |     ")
                print("    /      ")
            if turns == 5:
                print("5 turn left")
                print(" ----------")
                print("     O     ")
                print("     |     ")
                print("    / \    ")
            if turns == 4:
                print("4 turn left")
                print(" ----------")
                print("     O /   ")
                print("     |     ")
                print("    / \    ") 
            if turns == 3:
                print("3 turn left")
                print(" ----------")
                print("   \ O /   ")
                print("     |     ")
                print("    / \    ")
            if turns == 2:
                print("2 turn left")
                print(" ----------")
                print("   \ O /|  ")
                print("     |     ")
                print("    / \    ")
            if turns == 1:
                print("last breath counting, please play carefully...")
                print("1 turn left")
                print(" ----------")
                print("   \ O_|/  ")
                print("     |     ")
                print("    / \    ")
            if turns == 0:
                print("ohh! sorry u hangged..")
                print("0 turn left")
                print(" ----------")
                print(" |   O_|  |")
                print(" |  /|\   |")
                print(" |  / \   |")
                break

name = input("Enter your Name : ")
print("Welcome " , name)
print('-----------------------')
print('try to guess the word in less than 10 attempts')
hangman()