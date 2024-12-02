import math 
import random
def fight(player_attack, player_defense,player_health,zombie_attack,zombie_defense,zombie_health, zombie_name): 
    player_hit_damage = player_attack - zombie_defense
    zombie_hit_damage = zombie_attack - player_defense

    while True:
        player_health -= zombie_hit_damage
        zombie_health-= player_hit_damage
        if player_health>0 and zombie_health<=1:
            print('Je hebt gewonen!')
            print(f"Je hebt nu{player_health} HP")
            break
        elif zombie_health>0 and player_health<=0:
            print('Je hebt verloren  :(')
            print(f"Je hebt nu {player_health} HP")
            exit()
            break
        elif player_health<=0 and zombie_health<=0:
            print('Jullie heben samen doodgegaan.')
            print(f"Je hebt nu {player_health} HP")
            exit()
            break
    

    

            
       