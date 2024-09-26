import random


cijfers = [2,3,4,5,6,7,8,9,10,'boer', 'vrouw', 'heer', 'aas']
kaartpakken = ['harten', 'klaveren', 'schoppen','ruiten']
deck = []

gekeuzen_kaarten = []
for i in cijfers:
    for j in kaartpakken:
        deck.append((i,j))
deck.append('joker')
for i in range(6):
    random_element = random.choice(deck)
    gekeuzen_kaarten.append(random_element)
    deck.remove(random_element)
print('Gekeuzen karten:')
a = 0
for i in gekeuzen_kaarten:
    a+=1
    print(f'                  kaart{a}: {i[0]} {i[1]}')
print(deck)
print('')

