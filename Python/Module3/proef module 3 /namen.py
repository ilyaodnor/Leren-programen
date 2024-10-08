import random

namen = {}  
while True:
    name = input('Voer in een naam: ').lower()

    if name not in namen:
        namen[name] = name  
        
        if len(namen) >= 3:  
            ja_nee = input('Wilt u nog een naam invoeren? (ja/nee)').lower()
            if ja_nee == 'nee':
                break  
    else:
        print('Voer een nieuwe naam in!!')

namen_kopie = namen.copy()

keys = list(namen_kopie.keys())  
random.shuffle(keys)  

print("\nOriginele namen en hun koppelingen:")
for key in namen:
    print(f"{key} heeft zichzelf")

print("\nWillekeurig gekoppelde namen (na shuffelen):")
for i, key in enumerate(namen):
    print(f"{key} trekt -- {keys[i]}")
print(f'kopie namen: {namen_kopie}')
