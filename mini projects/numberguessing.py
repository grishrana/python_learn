import random
print("""\n\nWelcome to number guessing game.
This game auto selects a number and you need to guess it.
you got 5 chances to correctly guess the numnber.
the number will be within 0-100\n""")
num = random.randrange(100)
chances = 5
while(chances>0):
    print(f"no. of chances left: {chances}\n")
    guess=int(input("guess the number:"))
    if(guess>num):
        print("smaller\n")
    elif(guess<num):
        print("greater\n")
    elif(guess==num):
        print("Congo!! you have correctly guessed the number!!.")
        break
    chances=chances-1

if(chances==0):
    print(f"correct num: {num}\ntry again.better luck next time.")
