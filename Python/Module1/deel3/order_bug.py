
def vraag_getal(aantal):
    getal = int(input("Voer het getal in: "))
    return getal

def deel_getallen(a, b):

    return  a/b


getal_1 = vraag_getal("eerste")
getal_2 = vraag_getal("tweede")



if getal_2 == 0:
    print("Kan niet delen door 0")
else:
    ant = deel_getallen(getal_1, getal_2)
    print(f'{getal_1} gedeeld door {getal_2} is gelijk aan {ant}')

