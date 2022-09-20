import math
num_of_pennies = int(input("How many pennies would you like me to make change for? "))

def change_maker(pennies):
    dollars = math.floor(num_of_pennies / 100)
    change = num_of_pennies % 100
    print(dollars)
    quarters = math.floor(change / 25)
    change = change % 25
    print(quarters)
    dimes = math.floor(change / 10)
    change = change % 10
    print(dimes)
    nickels = math.floor(change / 5)
    change = change % 5
    print(nickels)
    pennies = change
    print(pennies)


change_maker(num_of_pennies)
       