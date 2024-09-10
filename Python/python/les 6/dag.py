woord_1 = input("Wat voor soort dag moet het zijn? ")
stad_1 = input("Welke stad is het? ")
naam_1 = input("Wat is de naam van de hoofdpersoon? ")
woord_3 = input("Waar is de hoofdpersoon naar op zoek? ")
woord_4 = input("Hoe ziet de man/vrouw eruit? ")
woord_5 = input("Wat verkoopt de man/vrouw? ")
woord_6 = input("Bij wat voor soort plek komt de hoofdpersoon aan? ")
woord_zin_7 = input("Wat doet de groep mensen? ")


verhaal = (
    f" Het was een {woord_1} dag in {stad_1}. \n {naam_1} liep door de straten, op zoek naar een {woord_3}. "
    f"Plotseling zag {naam_1} een {woord_4} man/vrouw die een {woord_5} verkocht. \n "
    f"{naam_1} besloot om het te kopen en liep verder. \n Toen {naam_1} bij een {woord_6} kwam, "
    f"zag hij/zij een groep mensen die {woord_zin_7}. \n {naam_1} besloot om mee te doen en had de tijd van zijn/haar leven."
)

# Stap 4: Print het verhaal
print(verhaal)
