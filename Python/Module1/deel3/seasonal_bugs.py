while True:
    try:
        print('Welk seizoen vind jij het fijnst?', 
            "A) Lente", 
            "B) Zomer", 
            "C) Herfst", 
            "D) Winter")
        gekozen_seizoen = input('? ')
        weer_type = 'koud'

        if gekozen_seizoen == 'a' or gekozen_seizoen== 'c':
            print('Dus jij vindt een tussenseizoen het fijnst...')

        elif gekozen_seizoen == 'b':
            weer_type = 'warm'
            print(f'Dus jij houd van {weer_type} weer!')
        elif gekozen_seizoen == 'd':
            weer_type = 'koud'
            print(f'Dus jij houd van {weer_type} weer!')
    except ValueError:
        print('error')