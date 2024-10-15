def even_of_oneven(getal:int) -> bool:
    return getal % 2 == 0

def omgekeerdelijst(text:str) -> str:
    woordenlijst = text.split()
    lijst2 = woordenlijst[::-1]
    omgekeerde_lijst = ' '.join(lijst2)
    return omgekeerde_lijst

def karaktertelling(getaal:str) -> int:
    lijst = set(getaal)
    lengte_van_set = len(lijst)
    return lengte_van_set

def gemmiddelde_lengte(string:str) -> float:
    lijst = string.split()
    
    summa = 0
    for woord in lijst:
        summa += len(woord)

    gemmiddeld_lengte = summa / len(lijst)
    return gemmiddeld_lengte

def vermenigvuldiging(getaal:int, base:int=10) -> None:
    for number in range(1, base+1):
        result = number * getaal
        print(f'{number} x {getaal} = {result}')
vermenigvuldiging(5, 20)

