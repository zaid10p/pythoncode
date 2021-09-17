import random
import re

while True:
    print()
    print("Rock, Paper, Scissors - Shoot! , q for quit")
    userChoice = input(
        "Choose your weapon [R]ock], [P]aper, or [S]cissors: ")
    if userChoice in ('q', 'Q'):
        break
    if not re.match("[SsRrPp]", userChoice):
        print("Please choose a letter: [R]ock, [S]cissors or [P]aper.")
        continue

    choices = ['R', 'P', 'S']
    opponenetChoice = random.choice(choices)
    print("CPU chose: " + opponenetChoice)
    if opponenetChoice == str.upper(userChoice):
        print("Tie! ")
    elif opponenetChoice == 'R' and userChoice.upper() == 'S':
        print("Scissors beats rock, I win! ")
        continue
    elif opponenetChoice == 'S' and userChoice.upper() == 'P':
        print("Scissors beats paper! I win! ")
        continue
    elif opponenetChoice == 'P' and userChoice.upper() == 'R':
        print("Paper beat rock, I win! ")
        continue
    else:
        print("You win!")
