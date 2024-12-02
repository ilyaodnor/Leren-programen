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
print(milk)
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
print(f'* {str_amount_fraction(eggs)} {str_single_plural(eggs,TXT_EGGS)} ')
print(f'* {str_amount_fraction(milk)} {str_units(milk,TXT_MILK)} ({unit2ml(milk, 'cup')} ml)')
print(f'* {str_amount_fraction(salt)} {str_units(salt,TXT_SALT)} ({ml2gram(unit2ml(salt, 'teaspoon'), GRAM_PER_ML_SALT)})')
print(f'* {str_amount_fraction(pepper)} {str_units(pepper,TXT_PEPPER)} ({ml2gram(unit2ml(pepper, 'teaspoon'), GRAM_PER_ML_PEPPER)} )')
print(f'* {str_amount_fraction(oil)} {str_units(oil,TXT_OIL)} ({unit2ml(oil, 'spoon')} ml)')
print(f'* {str_amount_fraction(onion)} {str_single_plural(onion,TXT_ONIONS)}')
print(f'* {str_amount_fraction(garlics)} {str_single_plural(garlics,TXT_GARLICS)}')
print(f'* {str_amount_fraction(paprika)} {str_single_plural(paprika,TXT_PAPRIKAS)}')
print(f'* {str_amount_fraction(spinach)} {str_units(spinach,TXT_SPINACH)} ({ml2gram(unit2ml(spinach, 'cup'), GRAM_PER_ML_SPINACH)})')
print(f'* {str_amount_fraction(cheese)} {str_units(cheese,TXT_CHEESE)} ({ml2gram(unit2ml(cheese, 'cup'), GRAM_PER_ML_CHEESE)})')

# print (formatted) all amounts and units combined with their ingrediënt descriptions
print('-----------------------------------------------')