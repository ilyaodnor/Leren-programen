def input_check(text, type):
    while True:
        if type == int:
            try:
                getal = int(input(text))
                return getal
            except ValueError:
                print('Voer in een integer! ')
        elif type == str:
            string = input(text)
            return string
        elif type == bool:
            try:
                getal = bool(input(text))
                return getal
            except ValueError:
                print('Voer in een getal!')



def fibonacci_getallen():
    getal_1 = input_check('Van welk getal wilt u de tafel zien:', int)
    getal_2 = input_check('Voer in twede getaal: ', int)
    lengte = input_check('Hoe lang moet de tafel zijn?', int)
    fibonacci_lijst = [getal_1,getal_2]
    
    for i in range(lengte):
        fibonacci_lijst.append(fibonacci_lijst[i+1]+fibonacci_lijst[i])
    
    return f'{', '.join(map(str,fibonacci_lijst))}'

print(fibonacci_getallen())