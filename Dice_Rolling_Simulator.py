# import random
# import string
# define a function to roll the dice
# Create a dictionary that will have the drawings of the dice
# ask the user how he wants it
# Watch video 1:38:42
import random
import string


def roll_dice(dice_drawing=None):



    roll = input("Roll the dice? (Yes/No): ")

    while roll.lower() == "Yes".lower():
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)

        print("dice rolled: {} and {}".format(dice1, dice2))
        print("\n". join(dice_drawing(dice1)))
        print("\n".join(dice_drawing(dice2)))

        roll = input("Roll again? (Yes/No): ")


roll_dice()
