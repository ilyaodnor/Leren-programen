from order_bug import deel_getallen
from test_lib import test, report

def minmax(nr1,nr2):
    if nr1>nr2:
        print(f'Maximum: {nr1} en minimum: {nr2}' )
    elif nr1<nr2:
        print(f'Maximum: {nr2} en minimum: {nr1}' )
    else:
        print('Beide getallen zijn even groot')

expected = '' #resultaat
result = None #roep hier je functie aan met 2 dezelfde getallen
test('TEST nr1=nr2', expected, result)

expected = '' #resultaat
result = None #roep hier je functie aan waar nr1 groter is dan nr2
test('TEST nr1>nr2', expected, result)

expected = '' #resultaat
result = None #roep hier je functie aan  waar nr1 kleiner is dan nr2
test('TEST nr1<nr2', expected, result)

if __name__ == "__main__":
    report()