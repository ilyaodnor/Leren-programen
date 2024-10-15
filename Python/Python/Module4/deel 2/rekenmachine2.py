from functions import addition, substracrion, multiplication, division, add, sub, mult, div
from test_lib import test, report

operations = {
    'A': lambda num1,num2: num1+num2,
    'B': lambda num1,num2: num1-num2,
    'C': lambda num1,num2: num1*num2,
    'D': lambda num1,num2: num1/num2,
    'E': lambda num1: num1+1,
    'F': lambda num1: num1-1,
    'G': lambda num1: num1*2,
    'H': lambda num1: num1/2
}

while True:
    gebr_operation = input(
        'Wat wilt u doen? \nA) getallen optellen, \nB) getallen aftrekken, \nC) getallen vermenigvuldigen, \nD) getallen delen, \nE) getal ophogen, \nF) getal verlagen, \nG) getal verdubbelen\nH) getal halveren?\n Kies:'
    ).capitalize()
    
    if gebr_operation in operations:
        break
    else:
        print('Voer in een letter!!')

if gebr_operation in ['A', 'B', 'C', 'D']:
    num1 = int(input('Voer in eerste getal: '))
    num2 = int(input(f'Welk getal {["optellen", "aftrekken", "vermenigvuldigen", "delen"][["A", "B", "C", "D"].index(gebr_operation)]} bij {num1}: '))
    result = operations[gebr_operation](num1, num2)
elif gebr_operation in ['E', 'F', 'G', 'H']:
    num1 = int(input('Voer in nummer 1: '))
    result = operations[gebr_operation](num1)

while True:
    print('---------------------------------------')
    gebr_operation = input(
        f'Wil je wat met de uitkomst ({result}) doen? \nA) iets optellen, \nB) iets aftrekken, \nC) met iets vermenigvuldigen, \nD) ergens door delen, \nE) ophogen, \nF) verlagen, \nG) verdubbelen, \nH) halveren of \nI) niets?\n Kies: ').capitalize()
    
    if gebr_operation == 'I':
        break
    elif gebr_operation in operations:
        if gebr_operation in ['A', 'B', 'C', 'D']:
            num2 = int(input(f'Welk getal {["optellen", "aftrekken", "vermenigvuldigen", "delen"][["A", "B", "C", "D"].index(gebr_operation)]} bij {result}: '))
            if num2 == 0 and gebr_operation == 'D':
                    print('Dat kan niet. ')
                    continue
            result1 = operations[gebr_operation](result, num2)
            if gebr_operation == 'A':
                print(f'{result} + {num2} = {result1}')
            elif gebr_operation == 'B':
                print(f'{result} - {num2} = {result1}')
            elif gebr_operation == 'C':
                print(f'{result} * {num2} = {result1}')
            elif gebr_operation == 'D':
                print(f'{result} / {num2} = {result1}')
            result = result1

        elif gebr_operation in ['E', 'F', 'G', 'H']:
            result1 = operations[gebr_operation](result)
            if gebr_operation == 'E':
                print(f'{result} + 1 = {result1}')
            elif gebr_operation == 'F':
                print(f'{result} - 1 = {result1}')
            elif gebr_operation == 'G':
                print(f'{result} * 2 = {result1}')
            elif gebr_operation == 'H':
                print(f'{result} : 2 = {result1}')
            result = result1
        else:
            print('Voer in een letter. ')

print(f'Jouw resultaat is: {result}')
expect = 22 * 33+1-2/2
test('result 22 * 33+1-2/2: ', expect, result)
report()
