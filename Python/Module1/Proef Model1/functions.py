import math, time, random

def gevecht(player_health, player_defense, player_attack, vijand_naam, vijand_attack, vijand_defense, vijand_health):
    print(f"Je begint een gevecht met {vijand_naam}!")
    time.sleep(1)
    
    while vijand_health > 0 and player_health > 0:

        schade_aan_vijand = max(0, player_attack - vijand_defense)
        vijand_health -= schade_aan_vijand
        print(f"Je valt {vijand_naam} aan en doet {schade_aan_vijand} schade!")
        

        if vijand_health <= 0:
            print(f"Je hebt {vijand_naam} verslagen!")
            break
        
        schade_aan_speler = max(0, vijand_attack - player_defense)
        player_health -= schade_aan_speler
        print(f"{vijand_naam} valt jou aan en doet {schade_aan_speler} schade!")
        

        if player_health <= 0:
            print("Je bent verslagen...")
            break
        
        time.sleep(1) 

    return player_health



def goblin_shop(rupee, player_defense, player_attack, sleutel):
    om_te_kopen = [1, 2, 3]  # 1: Schild, 2: Zwaard, 3: Sleutel
    if rupee >= 3:
        print('Je hebt genoeg rupees voor een schild, zwaard en sleutel.')
        player_defense += 1
        player_attack += 2
        sleutel = True
        print('*Je hebt nu een schild, zwaard en sleutel!*')
    elif rupee <= 0:
        print('Je hebt geen rupees om iets te kopen.')
    else:
        while rupee > 0 and om_te_kopen:
            try:
                print(f'Wat wil je kopen? Schild[1], Zwaard[2], Sleutel[3]')
                kopen = int(input(f'Je hebt {rupee} rupees. Maak je keuze: '))
                
                if kopen in om_te_kopen:
                    if kopen == 1:
                        rupee -= 1
                        player_defense += 1
                        om_te_kopen.remove(1)
                        print('*Je hebt nu een schild!*')
                    elif kopen == 2:
                        rupee -= 1
                        player_attack += 2
                        om_te_kopen.remove(2)
                        print('*Je hebt nu een zwaard!*')
                    elif kopen == 3:
                        rupee -= 1
                        sleutel = True
                        om_te_kopen.remove(3)
                        print('*Je hebt nu een sleutel!*')

                    if rupee == 0:
                        print('Je hebt geen rupees meer.')
                        break

                    if not om_te_kopen:
                        print('Er is niets meer om te kopen.')
                        break

                    verder_kopen = input('Wil je nog iets kopen? (ja/nee): ').lower()
                    if verder_kopen != 'ja':
                        break
                else:
                    print('Ongeldige keuze. Probeer opnieuw.')
            except ValueError:
                print('Voer een geldig nummer in.')
    return rupee, player_defense, player_attack, sleutel

