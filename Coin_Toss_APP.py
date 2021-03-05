# Coin Toss App:
import random;

print("Welcome to the coin Toss App")
print("I will fil a coin a set number of times.")

# Get user Input:
filp_number = int(input("How may times would you like me to flip the coin: "))
choice = input("Would you like to see the result of each flip (y/n): ").lower()

print("\nFlipping\n");

# Intialize variables
heads = 0;
tails = 0;

# The main loop:
for flips in range(filp_number):
    # create coin object
    coin = random.randint(0,1);

    if coin == 1:
        heads += 1;
        if choice.startswith('y'):
            print('Heads')
    else:
        tails += 1;
        if choice.startswith('y'):
            print('Tails')

    if heads == tails:
        print("At " + str(flips -1) + " flips , the number of heads and tails are equal at" + str(heads + 1))

# calculate percentage
heads_percentage = round(100*heads/filp_number,2)
tails_percentage = round(100*tails/filp_number,2)

# print the results
print("\nResults of flipping a coin " + str(filp_number) + " Times: ")
print("\nSide\t\tCount\t\tPercentage")
print("Heads\t\t" + str(heads) + "/" + str(filp_number) + "\t\t" + str(heads_percentage) + "%")
print("Tails\t\t" + str(tails) + "/" + str(filp_number) + "\t\t" + str(tails_percentage) + "%")

