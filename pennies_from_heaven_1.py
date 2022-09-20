import math

num_of_pennies = int(input("How many pennies would you like me to make change for? "))

dollars = 100
quarters = 25
dimes = 10
nickels = 5
penny = 1

p_remainder = 0

dollar_change = 0
quarter_change = 0
dime_change = 0
nickel_change = 0
penny_change = 0

def change_maker(pennies):
    global p_remainder
    global dollar_change
    global quarter_change
    global dime_change
    global nickel_change
    global penny_change
    
    if (pennies >= dollars):
       p_remainder = pennies % dollars
       dollar_change = math.floor(pennies / dollars)
       pennies = p_remainder
    if (pennies >= quarters):
        p_remainder = pennies % quarters
        quarter_change = math.floor(pennies / quarters)
        pennies = p_remainder
    if (pennies >= dimes):
        p_remainder = pennies % dimes
        dime_change = math.floor(pennies / dimes)
        pennies = p_remainder
    if (pennies >= nickels):
        p_remainder = pennies % nickels
        nickel_change = math.floor(pennies / nickels)
    penny_change = p_remainder
    
    

       
       
       
change_maker(num_of_pennies)

print(f"For {num_of_pennies}, you'll have {dollar_change} dollars, {quarter_change} Quarters, {dime_change} Dimes, {nickel_change} Nickels, {penny_change} Pennies")
       