import random

MAX_LINES = 3
MIN_BET = 1
MAX_BET = 100

ROWS=3
COLS=3

symbols_count={
    "A": 3,
    "B": 4,
    "C": 6,
    "D": 8
}

symbols_value={
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


def check_winnings(columns, lines, bet,values):
    winning=0
    winning_lines=[]
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol !=symbol_to_check:
                break
        else:
            winning += values[symbol] * bet
            winning_lines.append(line+1)
    return winning,winning_lines

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        
        columns.append(column)
    return columns

def print_slot_machines(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) -1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()

def deposit():
    while True:
        amount=input("\n-> How much would you like to deposit? $")
        if amount.isdigit():
            amount=int(amount)
            if amount > 0:
                break
            else:
                print("-> amount must be greater than 0.")
        else:
            print("-> Please enter a number.")
    
    return amount

def get_number_of_lines():
    while True:
        line=input(f"\n-> Enter the number of lines to bet on (1-{MAX_LINES})? ")
        if line.isdigit():
            line=int(line)
            if 1<=line<=MAX_LINES:
                break
            else:
                print("-> Enter the valid number of lines")
        else:
            print("-> Please enter a number.")
    
    return line

def get_bet():
    while True:
        bet=input(f"\n-> How much would you like to bet on each line(${MIN_BET}-${MAX_BET})? $")
        if bet.isdigit():
            bet=int(bet)
            if MIN_BET<=bet<=MAX_BET:
                break
            else:
                print("-> Enter the valid amount to bet.")
        else:
            print("-> Please enter a number.")
    
    return bet

def main():
    balance=deposit()
    while True:
        print(f"Current Balance is ${balance}")
        answer= input("Press enter to play (q to quit).")
        if answer =="q":
            break
        balance += spin(balance)
    
    print(f"You left with ${balance}")

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet*lines
        if total_bet>balance:
            print(f"-> you donot have enough to bet that amount, your balance is ${balance}.")
        else:
            break
    print(f"\n-> You are betting ${bet} on {lines} lines. Total bet is eqal to: ${total_bet}.")
    slot = get_slot_machine_spin(ROWS,COLS,symbols_count)
    print_slot_machines(slot)
    winnings,winning_lines = check_winnings(slot, lines, bet, symbols_count)

    print(f"\nYou won ${winnings}.")
    print(f"You won on lines: ", *winning_lines )
    return winnings-total_bet


main()