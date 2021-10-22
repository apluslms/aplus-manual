import random


def init_dice(seed):
    random.seed(seed)


def roll_dice_once(num_dice):
    rolls = []
    for i in range(num_dice):
        rolls.append(random.randint(1, 6))
    return rolls


def print_results(all_rolls):
    num_rolls = len(all_rolls)
    num_dice = len(all_rolls[0])
    heading = "Roll"
    for i in range(num_dice):
        heading += "    Die {:d}".format(i + 1)
    print("-" * len(heading))
    print(heading)
    print("-" * len(heading))
    for roll in range(num_rolls):
        roll_data = "{:d}.".format(roll + 1)
        for die in range(num_dice):
            roll_data += "      {:d}  ".format(all_rolls[roll][die])
        print(roll_data)
    print("-" * len(heading))


def save_results(all_rolls):
    num_rolls = len(all_rolls)
    num_dice = len(all_rolls[0])
    try:
        with open("results.csv", "w") as file:
            heading = "roll"
            for i in range(num_dice):
                heading += ",die{:d}".format(i + 1)
            file.write(heading)
            for roll in range(num_rolls):
                file.write("\n")
                roll_data = "{:d}".format(roll + 1)
                for die in range(num_dice):
                    roll_data += ",{:d}".format(all_rolls[roll][die])
                file.write(roll_data)
    except OSError:
        print("Could not write to file 'results.csv'.")


def main():
    seed = int(input("Give seed\n")) # <-- mistake here
    init_dice(seed)
    num_dice = int(input("How many dice are rolled?\n"))
    num_rolls = int(input("How many times should the dice be rolled?\n"))
    if num_dice > 0 and num_rolls > 0:
        print("Rolling dice...")
        all_rolls = []
        for i in range(num_rolls):
            all_rolls.append(roll_dice_once(num_dice))
        input("Press Enter to see the results.\n")
        print_results(all_rolls)
        print("Saving results to file 'results.csv'...")
        save_results(all_rolls)
    #print("Done!") # <-- mistake here


main()
