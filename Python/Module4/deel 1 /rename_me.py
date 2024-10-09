def even_of_oneven(getaal:int) -> bool:
    return getaal % 2 == 0

def omgekierdelijst(text:str) -> str:
    woordenlijst = text.split()
    lijst2 = woordenlijst[::-1]
    omgekierde_lijst = ' '.join(lijst2)
    return omgekierde_lijst

def karaktertelling(getaal:str) -> int:
    lijst = set(getaal)
    lengte_van_set = len(lijst)
    return lengte_van_set

def gemmiddeld_lengte(string:str) -> float:
    lijst = string.split()
    
    summa = 0
    for woord in lijst:
        summa += len(woord)

    gemmiddeld_lengte = summa / len(lijst)
    return gemmiddeld_lengte

def vermenigvuldiging(getaal:int, range:int=10) -> None:
    for number in range(1, range+1):
        result = number * getaal
        print(f'{number} x {getaal} = {result}')

