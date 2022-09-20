import math
num_of_pennies = int(input("How many pennies would you like me to make change for? "))

def change_maker(pennies):
    dollar_change = 0
    quarter_change = 0
    dime_change = 0
    nickel_change = 0
    penny_change = 0
    
    if(num_of_pennies >= 100):
        dollar_change = math.floor(num_of_pennies / 100)
        change = num_of_pennies % 100
        print(change)
    if(change >= 25):
        quarter_change = math.floor(change / 25)
        change = change % 25
    if(change >= 10):
        dime_change = math.floor(change / 10)
        change = change % 10
    if(change >= 5):
        nickel_change = math.floor(change / 5)
        change = change % 5
    penny_change = change
    
    return dollar_change, quarter_change, dime_change, nickel_change, penny_change
       
dollar_change, quarter_change, dime_change, nickel_change, penny_change = change_maker(num_of_pennies)       

print(f"For {num_of_pennies} pennies, you'll have: \nDollars: {dollar_change}\nQuarters: {quarter_change}\nDimes: {dime_change}\nNickels:{nickel_change}\nPennies: {penny_change}")

# print(change_maker(num_of_pennies))
       