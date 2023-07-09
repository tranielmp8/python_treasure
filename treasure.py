import random
print("------------------------------------")
print("          Treasure Game             ")
print("------------------------------------")

print("Make the right choice and get the Treasure")

coin = ["heads", "tails" ]
coin_toss = random.choice(coin)


die = ["odd", "even"]
die_toss = random.choice(die)

spinner = ["black", "white"]
color_spin = random.choice(spinner)

# print(f"{coin_toss} - - {die_toss} - - {color_spin}")

choice1 = input("1st trial! choose between heads or tails \n").lower()
print("***** toss coin in the air ***** ")
if choice1 == coin_toss:
    choice2 = input(f"{coin_toss}! Great choice. Now guess if the die will be odd or even \n").lower()
    print("***** toss die in the air *****")
    if choice2 == die_toss:
        choice3 = input(f"{die_toss}! Great job! I see you are sweating. Last trial choose a color - black or white \n").lower()
        print("***** spins the spinner *****")
        if choice3 == color_spin:
            print(f"{color_spin}! You win, Like I knew you would. Come get the treasure")
        else:
            print(f"{color_spin.upper()}! I knew you were a loser. SORRY fam!")
    else:
        print(f"{die_toss.upper()}! Tough, you lose!")
else:
    print(f"{coin_toss.upper()}! better luck next time LOSER!!! MWAHAHAHA")