import functions
from test_lib import test, report

result1 = functions.start() # voer in 3 bolletjes , in bak
expected1 = 'Hier is uw bakje met 3 bolletje(s).'
test('test 1: ', expected1, result1)


result2 = functions.start() #voer in 2 bolletjes, in hoorn
expected2 = 'Hier is uw hoorntje met 2 bolletje(s).'
test(f'test2: ', expected2, result2)


result3 = functions.start() #voer in 5 bolletjes
expected3 = 'Dan krijgt u van mij een bakje met 5 bolletjes.'
test('test3: ', expected3, result3)

expected4 = 'Sorry, zulke grote bakken hebben we niet.'
result4 = functions.start()#voer in meer dan 8
test('test4: ', expected4, result4)

report()