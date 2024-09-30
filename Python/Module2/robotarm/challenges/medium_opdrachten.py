import sys
sys.path.insert(0,'/Users/ilya/Documents/GitHub/School/Softwere dev./python/Leren-programen/Python/Module2/robotarm')
from RobotArm import RobotArm
from medium import challenges
robotArm = RobotArm(challenges[3],3)
for e in range(9): robotArm.moveRight()
for i in range(9):
    for _ in range(d=1):robotArm.moveLeft()
    robotArm.grab()
    if robotArm.scan()!= 'white':
        robotArm.drop()
    elif robotArm.scan() == 'white': 
        index = robotArm.stackIndex()
        while robotArm.stackIndex()!=9:
            robotArm.moveRight()
        robotArm.drop()
        while robotArm.stackIndex() != index:
            robotArm.moveLeft()
robotArm.report()
