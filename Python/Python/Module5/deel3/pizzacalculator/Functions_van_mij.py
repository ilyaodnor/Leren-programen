def input_check(text, type, expect_string = ''):

    while True:
        if type == int:
            try:
                getal = int(input(text))
                return getal
            except ValueError:
                print('Voer in een integer! ')
        elif type == str:
            string = input(f'{text} ({expect_string})')
            if string in expect_string:     
                return string
            else:
                print(f'voer in ({expect_string})')
        elif type == bool:
            try:
                getal = bool(input(text))
                return getal
            except ValueError:
                print('Voer in een getal!')

