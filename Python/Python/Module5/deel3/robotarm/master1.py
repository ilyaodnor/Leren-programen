import sys
sys.path.insert(0,'/Users/ilya/Documents/GitHub/School/Softwere dev./python/Leren-programen/Python/Module2/robotarm')
from RobotArm import RobotArm
from master import challenges
robotArm = RobotArm(challenges[1],2)
kleuren = {'red':0,'green':0,'blue':0,'yellow':0,'purple':0,'orange':0,'white':0,'n':0,'l':0, 'gray': 0, 'black':0,}
robotArm.showSolution()
for i in range(9):
    robotArm.grab()
    kleur = robotArm.scan()
    kleuren[kleur] += 1

    a = robotArm.scan()
    if a != max(kleuren, key=kleuren.get) and i >=2:
        robotArm.report()

    robotArm.drop()
    robotArm.moveRight()

for i in range(9):
    robotArm.grab()
    a = robotArm.scan()
    if a == max(kleuren, key=kleuren.get):
        robotArm.report()
    robotArm.drop()
    robotArm.moveLeft()
