import sys
sys.path.insert(0,'/Users/ilya/Documents/GitHub/School/Softwere dev./python/Leren-programen/Python/Module2/robotarm')
from RobotArm import RobotArm
from master import challenges
robotArm = RobotArm(challenges[5],3)

kleuren = {'red': 0, 'green': 0, 'blue': 0, 'yellow': 0, 'purple': 0, 'orange': 0, 'white': 0, 'n': 0, 'l': 0, 'gray': 0, 'black': 0}
dubbel_kleur = {}

for i in range(10):
    robotArm.grab()
    kleur = robotArm.scan()
    if kleur in kleuren:
        kleuren[kleur] += 1
    robotArm.drop()
    if i != 9:
        robotArm.moveRight()

maximum = max(kleuren, key=kleuren.get)
print("Цвет с максимальным количеством:", maximum)

for i in range(10):
    robotArm.grab()
    kleur = robotArm.scan()
    if kleur == maximum:
        if kleur not in dubbel_kleur: 
            dubbel_kleur[kleur] = robotArm.stackIndex()
        else: 
            while robotArm.stackIndex() != dubbel_kleur[kleur]:
                robotArm.moveRight()
            robotArm.drop()    
            robotArm.report()
    robotArm.drop()
    if robotArm.stackIndex() != 0:
        robotArm.moveLeft()
