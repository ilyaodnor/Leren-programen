fruiten = ['banan', ' kiwi', 'dragonfruit', 'appel', 'sinasappel', 'druiven']
print(fruiten)
vraag = int(input('welke fruit wilt u? (1,2,3,4,5,6,)'))
fruiten.pop(vraag + 1)
print(fruiten)