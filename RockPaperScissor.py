import random as rd

choices = {'r': 'ROCK', 'p': 'PAPER', 's': 'SCISSOR'}

# costom functions
def validateUserInput(choice):
    while(True):
        if choice in choices.keys():
            break
        choice = input('Please enter a valid choice :  ')
    return choice

# custom function
def gameMechanism(com, player) -> None:
    if(com == player):
        print('Match draw!')
    elif (com == 'r' and player == 's') or (com == 'p' and player == 'r') or (com == 's' and player == 'p'):
        print('Computer Woned!')
    else: print('Player Woned!')
    print()
    print(f'Computer choosed : {choices.get(com)}\nPlayer choosed   : {choices.get(player)}\n\n')
        
# give an integer as input that represents how many times you want to play
totalChance = int(input('How many times do you want to pley? :  '))

print("You can choose any of this\n['ROCK', 'PAPER', 'SCISSOR']\n")
choiceKeys = tuple(choices.keys())

while(bool(totalChance)):
    computerChoice = rd.choice(choiceKeys)
    playerChoice = validateUserInput(choice= input("Type 'r'=ROCK, 'p'=PAPER, 's'=SCISSOR :   "))
    gameMechanism(com= computerChoice, player= playerChoice)
    totalChance = totalChance - 1

print("TKANKS! FOR PLAYING THIS GAME\n")