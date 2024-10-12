
mensen = int(input('hoeveel mensen is  er?'))

minuten = int(input('Hoelang?'))
prijs = 7.45
kosten = prijs * mensen + round((minuten / 5) * 5) * 0.37

print (f"Dit geweldige dagje-uit met {mensen} mensen in de Speelhal met {minuten} minuten VR kost je maar {kosten} euro")