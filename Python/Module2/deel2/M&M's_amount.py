import random


kleuren = ['orange', 'blauw', 'groen','bruin', 'paars']

toevoegen = int(input('Hoeveel M&M\'s er aan de zak toegevoegd moeten worden?'))
returned_arr=[]
for i in range(toevoegen):
    returned_arr.append(random.choice(kleuren))
print(returned_arr)