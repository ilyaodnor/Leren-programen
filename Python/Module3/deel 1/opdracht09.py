from fruitmand import fruitmand
fruitmand.remove(fruitmand[4])
kleuren = []
for i in fruitmand:
    if i['color'] not in kleuren:
        kleuren.append(i['color'])
print(kleuren)