from recipe_lib import *
from frittata_ingredients import *
from math import ceil
def round_up_to_nearest_quarter(number):
    return ceil(number * 4) / 4

def round_up_to_nearst_half(number):
    return ceil(number*2) /2

print('=============== Frittata recept ===============')
while True:
    try:
        nr_persons = int(input('Hoeveel persoonen? \n'))
        if nr_persons>0:
            break
        else:
            print('voer in personen amount!!')
    except ValueError:
        print('voer in personen amount!!')

# ----- CALCULATIONS ----
# calculate factor 
# calculate amount_eggs
eggs = ceil(AMOUNT_EGGS/4*nr_persons)


# calculate amount_milk
milk = round_quarter(AMOUNT_MILK/4*nr_persons)
# calculate amount_salt
salt = round_quarter(AMOUNT_SALT/4*nr_persons)
# calculate amount_pepper
pepper = round_quarter(AMOUNT_PEPPER/4*nr_persons)
# calculate amount_oil
oil = round_quarter(AMOUNT_OIL/4*nr_persons)
# calculate amount_onions
onion = ceil(AMOUNT_ONIONS/4*nr_persons)
# calculate amount_garlics
garlics = ceil(AMOUNT_GARLICS/4*nr_persons)
# calculate amount_spinach
spinach = round_quarter(AMOUNT_SPINACH/4*nr_persons)
# calculate amount_paprikas

paprika = ceil(AMOUNT_PAPRIKAS/4*nr_persons)
# calculate amount_cheese

cheese = round_quarter(AMOUNT_CHEESE/4*nr_persons)

# -------- OUTPUT -------
print('=============== Frittata recept ===============')
print(f'Ingrediënten voor {nr_persons} {TXT_PERSONS}:')
print('-----------------------------------------------')
print(f'{eggs} {TXT_EGGS}')
print(f'{milk} {TXT_MILK}')
print(f'{salt} {TXT_SALT}')
print(f'{pepper} {TXT_PEPPER}')
print(f'{oil} {TXT_OIL}')
print(f'{onion} {TXT_ONIONS}')
print(f'{garlics} {TXT_GARLICS}')
print(f'{paprika} {TXT_PAPRIKAS}')
print(f'{spinach} {TXT_SPINACH}')
print(f'{cheese} {TXT_CHEESE}')

# print (formatted) all amounts and units combined with their ingrediënt descriptions
print('-----------------------------------------------')