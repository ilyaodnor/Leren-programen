import Functions_van_mij, colorama, time
from data import *
from Functions_van_mij import *

Functions_van_mij.clear_screen()
print('Welkom bij Papi Gelato. je mag alle smaken kiezen zolang het maar vanille ijs is.')
time.sleep(1)
while True:
    try:
        hoeveelheid = Functions_van_mij.input_check("Hoeveel bolletjes wilt u? ", int)
        if 1 <= hoeveelheid <= 3:
            form_type = Functions_van_mij.input_check(
                f"Wilt u deze {hoeveelheid} bolletje(s) in een hoorntje of een bakje? ", str, SERVER_OPTIES
            )
            if form_type in ["een hoorntje", "hoorn", "een hoorn"]:
                form_type = "hoorntje"
            elif form_type in ["bak", "bakje", "een bak", "een bakje"]:
                form_type = "bakje"
            Functions_van_mij.serve_bolletje(hoeveelheid, form_type)
        elif 4 <= hoeveelheid <= MAX_BOLLETJES:

            print(f"Dan krijgt u van mij een bakje met {hoeveelheid} bolletjes.")
        else:
            print("Sorry, zulke grote bakken hebben we niet.")
            continue

        if not Functions_van_mij.input_check("Wilt u nog iets bestellen? (ja/nee) ", bool):
            break
    except ValueError:
        print("Sorry, dat snap ik niet.")

print("Bedankt en tot ziens!")