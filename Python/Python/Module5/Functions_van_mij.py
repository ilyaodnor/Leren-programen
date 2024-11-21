def input_check(text, type,expected: list):

    while True:
        if type == int:
            try:
                getal = int(input(text))
                return getal
            except ValueError:
                print('Voer in een integer! ')
        elif type == str:
            string = str(input(f'{text} '))
            if string in expected:     
                return string
            else:
                print(f'voer in ({expected})')
        elif type == bool:
            try:
                getal = bool(input(text))
                return getal
            except ValueError:
                print('Voer in een getal!')

