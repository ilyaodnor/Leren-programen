import sys
sys.path.insert(0,'/Users/ilya/Documents/GitHub/School/Softwere dev./python/Leren-programen/Python/Module2/robotarm')
from RobotArm import RobotArm
from expert import challenges
robotArm = RobotArm(challenges[4],2)

for i in range(6):
    aantaal =0
    robotArm.grab()
    if robotArm.scan() == 'red':
        while robotArm.stackIndex()!=7:
            robotArm.moveRight()
            aantaal+=1
        robotArm.drop()
        for i in range(aantaal-1):robotArm.moveLeft()
        aantaal =0
    elif robotArm.scan() == 'blue':
        while robotArm.stackIndex()!=9:
            robotArm.moveRight()
            aantaal+=1
        robotArm.drop()
        for i in range(aantaal-1):robotArm.moveLeft()
        aantaal =0
    elif robotArm.scan() == 'green':
        while robotArm.stackIndex()!=8:
            robotArm.moveRight()
            aantaal+=1
        robotArm.drop()
        for i in range(aantaal-1):robotArm.moveLeft()
        aantaal =0
    else:
        break
robotArm.showSolution()
robotArm.report()
