def game():
    """
    -----------------------------------------------------
    generates a random integer to be guessed in a number of tries
    Use: game(tries)
    -----------------------------------------------------
    Parameters:
        None
    Returns:
        None
    -----------------------------------------------------
    """

    from random import randrange
    replay = True

    while bool(replay) == True:
        tries = int(input("Enter number of tries: "))
        increment = int(input("Enter increment number: "))

        difficulty = input("easy or hard? ")

        if difficulty == "easy":
            num = randrange(1, 10+1, increment)
        elif difficulty == "hard":
            num = randrange(10, 100+1, increment)
        else:
            validity = False
            while validity == False:
                print(f'Invalid input')
                difficulty = input("easy or hard? ")
                if difficulty == "easy":
                    validity = True
                    num = randrange(1, 10 + 1, increment)
                    break
                elif difficulty == "hard":
                    validity = True
                    num = randrange(10, 100+1, increment)
                    break

        for x in range(1, tries+1):
            guess = int(input(f'Enter guess{x}: '))
            if guess == num:
                print(f'You won! The number was {num}')
                break
            if x == tries:
                print(f'You lost, number was {num}')

        replay = input("Would you like to play again (Y/N)? ")

        if replay == "Y":
            replay = True
        elif replay == "N":
            replay = False
            print(f'Thanks for playing')
        else:
            valid = False
            while valid == False:
                print(f'Invalid input')
                replay = input("Would you like to play again (Y/N)? ")
                if replay == "Y":
                    replay = True
                    break
                elif replay == "N":
                    print(f'Thanks for playing')
                    replay = False
                    break

game()
