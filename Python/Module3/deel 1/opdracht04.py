import fruitmand, random
getaal = int(input('Voer in aantaal: '))
for i in range(getaal):
   print(random.choice(fruitmand.fruitmand)['name'])