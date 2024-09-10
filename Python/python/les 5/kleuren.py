lijst = ['rood', 'geel', 'paars', 'blauw', 'grijs', 'wit']

naam = input('Wat is jouw naam? ')


print(f'Hoi {naam}, wat is jouw favoriete kleur? ')

while True:
    kleur = input('(rood, geel, paars, blauw, grijs, wit): ').strip().lower()
    if kleur in lijst:
        print(f"{kleur.capitalize()} is echt een mooie kleur, {naam}! Het straalt helemaal jouw karakter uit!")
        break
    else:
        print(f'Psst {naam}, deze kleur is niet zo geweldig als: {", ".join(lijst)}.')
        print('Probeer het nog eens!')