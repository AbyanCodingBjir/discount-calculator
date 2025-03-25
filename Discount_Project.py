print('\n=== DISCOUNT CALCULATOR===\n')

currency = input('Insert the currency here: ') #Example: Rp, $, etc

try:
    price = int(input('Insert the actual price here: ')) #The Actual Price
    percent = int(input('Then insert discount precent target: ')) #discount percent
except ValueError:
    print('the numbers not the letters >:()')
    exit()

discount = (price / 100) * percent #discount formula math :3

the_price_discount = price - discount #the price after discount with the formula UwU
print('')
print('The Price w/ discount: ', currency,the_price_discount)
print('You saved: ',currency,discount)

#Note: this is just my simple project, if the calculator doesn't accurate with this, welp tell in the comments :3 