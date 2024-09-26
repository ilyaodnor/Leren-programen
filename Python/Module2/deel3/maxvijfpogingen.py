wachtwoord = 1999

print('voer in het wachtwoord:')

aantalpogingen = 5

while aantalpogingen> 0:
    a = int(input('Wachtwoord: '))
    
    if a == wachtwoord:
            break

    else:
            aantalpogingen-=1
            print(f'U heeft nog {aantalpogingen} pogingen')
if a == wachtwoord:
        print('Juist!')
else:
    print('U Hebt geen pogingen meer')

