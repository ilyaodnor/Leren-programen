import sys
sys.path.insert(0,'/Users/ilya/Documents/GitHub/School/Softwere dev./python/Leren-programen/Python/Module2/robotarm')
from RobotArm import RobotArm
from medium import challenges
robotArm = RobotArm(challenges[1],3)
for _ in range(8): robotArm.moveRight()
for i in range(9):
    robotArm.grab()
    for _ in range(1): robotArm.moveRight()
    robotArm.drop()
    if i != 8: 
        for e in range(2): robotArm.moveLeft()
robotArm.showSolution()
robotArm.report()
