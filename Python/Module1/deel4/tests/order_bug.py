def vraag_getal(getal):
    getal = int(input("Voer het getal in: "))
    return getal

def deel_getallen(nr1, nr2):

    return  nr1/nr2
def minmax(nr1, nr2):
    if nr1 > nr2:
        maximum, minimum = nr1, nr2
    elif nr1 < nr2:
        maximum, minimum = nr2, nr1
    else:
        print('Beide getallen zijn even groot')
        return nr1, nr2

    print(f'Maximum: {maximum} en minimum: {minimum}')
    return maximum, minimum

getal_1 = vraag_getal("eerste")
getal_2 = vraag_getal("tweede")



if getal_2 == 0:
    print("Kan niet delen door 0")
else:
    ant = deel_getallen(getal_1, getal_2)
    print(f'{getal_1} gedeeld door {getal_2} is gelijk aan {ant}')
    minmax(getal_1,getal_2)

