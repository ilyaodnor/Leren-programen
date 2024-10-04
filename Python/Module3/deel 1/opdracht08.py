import fruitmand
totaal = 0
for d in fruitmand.fruitmand:
    totaal+=d['weight']
print(totaal)

fruitmand.fruitmand.append({
    'name': 'watermeloen',
    'weight': 1000,
    'kleur': 'groen',
    'round': True

})
totaal = 0

for i in fruitmand.fruitmand:
    totaal+=i['weight']

    

print(totaal)
