import random


field = [0, 0, 0,
         0, 0, 0,
         0, 0, 0]


def display():
    ele = 0
    external = field.copy()
    for i, value in enumerate(external):
        if value == 1:
            external[i] = "X"
    for i, value in enumerate(external):
        if value == 2:
            external[i] = "O"
    for i, value in enumerate(external):
        if value == 0:
            external[i] = " "
    ele = 0
    shown = [external[0], "|", external[1], "|", external[2],
             "-", "-", "-", "-", "-",
             external[3], "|", external[4], "|", external[5],
             "-", "-", "-", "-", "-",
             external[6], "|", external[7], "|", external[8]]
    for i in range(5):
        for x in range(5):
            print(shown[ele], end="")
            ele += 1
        print()


def computer():
    options = [i for i, x in enumerate(field) if x == 0]
    choice = random.choice(options)
    field[choice] = 2
    display()


def player():
    while True:
        options = [i for i, x in enumerate(field) if x == 0]
        play = int(input("Select an index to place your X: "))
        if play in options:
            field[play] = 1
            break


def checkend():
    if field[0] and field[1] and field[2] == 1:
        print("The player has won!")
        return False
    elif field[0] and field[1] and field[2] == 2:
        print("The computer has won!")
        return False
    elif field[0] and field[3] and field[6] == 1:
        print("The player has won!")
        return False
    elif field[0] and field[3] and field[6] == 2:
        print("The computer has won!")
        return False
    elif field[0] and field[4] and field[8] == 1:
        print("The player has won!")
        return False
    elif field[0] and field[4] and field[8] == 2:
        print("The computer has won!")
        return False
    elif field[1] and field[4] and field[7] == 1:
        print("The player has won!")
        return False
    elif field[1] and field[4] and field[7] == 2:
        print("The computer has won!")
        return False
    elif field[2] and field[4] and field[6] == 1:
        print("The player has won!")
        return False
    elif field[2] and field[4] and field[6] == 2:
        print("The computer has won!")
        return False
    elif field[2] and field[5] and field[8] == 1:
        print("The player has won!")
        return False
    elif field[2] and field[5] and field[8] == 2:
        print("The computer has won!")
        return False
    elif field[3] and field[4] and field[5] == 1:
        print("The player has won!")
        return False
    elif field[3] and field[4] and field[5] == 2:
        print("The computer has won!")
        return False
    elif field[6] and field[7] and field[8] == 1:
        print("The player has won!")
        return False
    elif field[6] and field[7] and field[8] == 2:
        print("The computer has won!")
        return False
    else:
        return True


def main():
    print("Bean's Tic-Tac-Toe Game")
    print("Created by: Brandon Gillis")
    print("2021-10-07")
    while True:
        if input("Play? Y/N: ").lower() == "y":
            first = int(input("1 to go first, 0 for computer to go first: "))
            display()
            if first == 1:
                while True:
                    x = checkend()
                    if x:
                        player()

                    else:
                        break



main()