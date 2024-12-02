hoeveelheid=int(input('Hoeveel lijstje wilt u zien?'))
vollijst = []
a = 1
for i in range(1, hoeveelheid+1):
    lengte_lijst = int(input(f'Hoelang moet lijst {i} zijn?'))

    lijst = list(range(i, i * lengte_lijst+1, i))
    vollijst.append(lijst)
print(f'{vollijst}')

    

