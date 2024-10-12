#import hier je functie "from [bestandsnaamZonderExtentie] import [functieNaam]"
from test_lib import test, report
from vergelijken import vergelijken
expected = (1,1) #resultaat
result = vergelijken(1,1)
test('TEST nr1=nr2', expected, result)

expected = (2,1) #resultaat
result = vergelijken(2,1)
test('TEST nr1>nr2', expected, result)

expected = (1,4)
result = vergelijken(1,4)
test('TEST nr1<nr2', expected, result)

if __name__ == "__main__":
    report()