from fruitmand import fruitmand
mand = {}
for fruit in fruitmand:
    mand[fruit['name']] = fruit['weight'] / 1000
# sorted_mand = sorted(mand.items(), key=lambda x: x[1], reverse=True)
# for name, weight in sorted_mand:
#     print(f'{name}: {weight} kg')
def sort2(fruit):
    return fruit[1]
sorted_mand = sorted(mand.items(),key = sort2, reverse= True)
print(sorted_mand)
