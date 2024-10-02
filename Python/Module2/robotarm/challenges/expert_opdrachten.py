import sys
sys.path.insert(0,'/Users/ilya/Documents/GitHub/School/Softwere dev./python/Leren-programen/Python/Module2/robotarm')
from RobotArm import RobotArm
from expert import challenges
robotArm = RobotArm(challenges[2],3)
aantaal = 1
for i in range(9):
    robotArm.grab()
    if robotArm.scan() == 'red':
        while robotArm.stackIndex()!=9:
            robotArm.moveRight()
            aantaal+=1
        robotArm.drop()
        for i in range(aantaal-1):
            print(aantaal)
            robotArm.moveLeft()
    else:
        robotArm.drop()
        robotArm.moveRight()   
    aantaal=0
robotArm.report()
