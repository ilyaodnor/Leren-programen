def persoon(dicts = {}):
    naam = input('Voer in je naam: ').capitalize()
    
    while True:
        try:
            leeftijd = int(input('Hoe oud ben je? '))
            break
        except ValueError:
            print("Voer een geldig getal in voor de leeftijd.")
    
    woonplaats = input('Waar woon je? ').capitalize()
    
    if naam not in dicts:
        dicts[naam] = {'leeftijd': leeftijd, 'woonplaats': woonplaats}
    
    return dicts
