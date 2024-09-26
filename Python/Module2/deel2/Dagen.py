dagen = ['maandag','dinsdag','woensdag','donderdag','vrijdag','zaterdag','zondag']
werkdagen = dagen[0:5]
weekenddagen = dagen[5:7]


print('Alle dage van de week zijn:')
print(f"-{'\n-'.join(dagen)}")
print('')
print(f'{','.join(werkdagen[0:4])} & {werkdagen[4]}')
print('')
print(f'de weekend dagen zijn: {weekenddagen[0]} & {weekenddagen[1]}')
print('')
print(f"Alle dagen van de week in omgekeerde volgorde zijn: {' -> '.join(list(reversed(dagen)))}")
print('')
print('De werkendagen in omgekeerde volgorde zijn:')
print(f'\n -{'\n -'.join(list(reversed(werkdagen)))}')
print('')
print(f"De weekenddagenn in omgekeerde volgorde zijn: {' + '.join(list(reversed(weekenddagen)))}")
print('')