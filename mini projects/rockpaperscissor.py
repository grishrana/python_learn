import random
choices=['rock','paper','scissor']
usr_wins=0
comp_wins=0
while True:
    usr_input=str(input("\nEnter 'rock','paper','scissor' or 'q' tp quit: \n"))
    if usr_input=='q':
        break
    if usr_input not in choices:
        continue
    
    rand_number=random.randint(0,2)
    comp_input=choices[rand_number]
    print(f"computer chose {comp_input}")
    if usr_input=='rock' and comp_input=='scissor':
        usr_wins+=1
        print("You won!!")
    
    elif usr_input=='paper' and comp_input=='rock':
        usr_wins+=1
        print("You won!!")

    elif usr_input=='scissor' and comp_input=='paper':
        usr_wins+=1
        print("You won!!")

    elif usr_input==comp_input:
        print("it was a tie!!")
    else:
        print("You lose!!")
        comp_wins+=1
    
print("user_wins:",usr_wins)
print("compuer_wins:",comp_wins)
print("Goodbye!!")