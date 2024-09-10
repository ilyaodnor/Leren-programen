from random import randint
score=20
for i in range(1,4):
    te_raden = randint(1,5)
    print(te_raden)
    while True:
        gok = int(input('Kies een getal van 1 t/m 5: '))
        if (te_raden == gok):
            print("Je hebt het getal goed geraden!")
            break
        else:
            print("Je hebt het getal niet goed geraden!")
            score-=1
print(f'Score {score}')