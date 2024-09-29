import sys
sys.path.insert(0,'/Users/ilya/Documents/GitHub/School/Softwere dev./python/Leren-programen/Python/Module2/robotarm')
from RobotArm import RobotArm
from beginner import challenges
robotArm = RobotArm(challenges[5],3)
robotArm.moveRight()
for i in range(7):
    robotArm.grab()
    for b in range(8): robotArm.moveRight()
    robotArm.drop()
    if i != 6:
        for d in range(8): robotArm. moveLeft()
robotArm.report()