from random import choice

kleuren = ('oranje', 'blauw', 'groen', 'bruin')
aantal = int(input('Hoeveel M&M’s er aan de zak toegevoegd moeten worden? '))

MnMs = []
MnMs_inhoud = {kleur: 0 for kleur in kleuren}
for _ in range(aantal):
    MnMs.append(choice(kleuren))
for kleur in MnMs:
    MnMs_inhoud[kleur] += 1


print('De inhoud van de zak met M&M’s:')
print(MnMs_inhoud)