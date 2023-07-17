import random

die_value = [1, 2, 3, 4, 5, 6]

# This function generates random value of each die
def dice_roll_generator(number_of_dice):
    while True:
        rolled = []
        for _ in range(number_of_dice):
            rolled.append(random.choice(die_value))
        result = ", ".join(list(map(str, rolled))).strip()
        print(f"You rolled {result}")
        answer = input('Press enter if you want to roll again (q to quit) ')
        if answer != 'q':
            pass
        else:
            return result

# This function receives how many dice a player wants to roll
def number_of_dice():
    print('The rule is simple: you cannot roll more than 5 dice')
    while True:
        number_of_dice = input('How many dice do you want to roll? ')
        if number_of_dice.isdigit() and int(number_of_dice) < 6 and int(number_of_dice) > 0:
            if int(number_of_dice) == 1:
                print('You want to roll 1 die')
            else:
                print(f'You want to roll {number_of_dice} dice')
                number_of_dice = int(number_of_dice)
            return number_of_dice, dice_roll_generator(number_of_dice)
        else:
            print('Please, enter valid number of dice')

def main():
    number_of_dice()
    while True:
        answer = input('Do you want to change the number of dice and roll again? Press enter (or q to quit) ')
        if answer != 'q':
            number_of_dice()
        else:
            print('I know it was not the most exciting game you have played')
            break

main()