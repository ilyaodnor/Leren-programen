import sys
sys.path.insert(0,'/Users/ilya/Documents/GitHub/School/Softwere dev./python/Leren-programen/Python/Module2/robotarm')
from RobotArm import RobotArm
from master import challenges
robotArm = RobotArm(challenges[1],2)

blok_1 = None
blok_2 = None
blok_3 = 0

basis_kleur  = 0
afwijkende_kleur = 0

for i in range(9):
    robotArm.grab()
    if i == 0:  
        blok_1 = robotArm.scan()
    elif i==1:
        blok_2 = robotArm.scan()
    elif i == 2:
        blok_3 = robotArm.scan()
        if blok_1!= blok_2:
            robotArm.drop()
            if blok_3 == blok_1:
                for i in range(1):robotArm.moveLeft()
                robotArm.grab()
                break
            elif blok_3 == blok_2:
                for i in range(2):robotArm.moveLeft()
                robotArm.grab()
                break
        elif blok_1!= blok_3 and blok_3 != blok_2:
            break
        else:
            robotArm.drop()
            robotArm.moveRight()
            continue

    else:  
        if i==3:
            basis_kleur=3
        kleur = robotArm.scan()
        if kleur != blok_1:
            afwijkende_kleur = kleur
            if i >=2 : break

    robotArm.drop()
    if i != 9: robotArm.moveRight()


robotArm.report()