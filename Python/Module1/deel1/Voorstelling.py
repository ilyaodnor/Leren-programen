naam = input("Wat is je naam? ")
leeftijd = int(input("Hoe oud ben je? "))
geslaagd = input("Ben je een A) een jonge of B) een meisje? ").lower()
kleur = input("Wat is je favoriete kleur? ")
favoriete_getal= int(input("Wat is je favoriete getal? "))
verschil = abs(leeftijd-favoriete_getal)
Voornaamwoord = 'haar' if geslaagd == 'b' else 'zijn'

print("")
print("Mag ik je voorstellen aan", naam)
print(f"{Voornaamwoord.capitalize()} leeftijd is:", leeftijd)
print(f"{naam.capitalize()}'s favoriete kleur is:", kleur)
print(f"Het verschil tussen {Voornaamwoord} leeftijd en {favoriete_getal} is:", verschil)
