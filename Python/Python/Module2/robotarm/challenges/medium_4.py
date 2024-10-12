import sys
sys.path.insert(0,'/Users/ilya/Documents/GitHub/School/Softwere dev./python/Leren-programen/Python/Module2/robotarm')
from RobotArm import RobotArm
from medium import challenges
robotArm = RobotArm(challenges[4],2)
for i in range(5):
    robotArm.grab()
    for d in range(2): robotArm.moveRight()
    robotArm.drop()
    if i !=4:
        for u in range(2): robotArm.moveLeft()
for i in range(5):
    robotArm.grab()
    for d in range(1): robotArm.moveLeft()
    robotArm.drop()
    if i!= 5:
        for u in range(1): robotArm.moveRight()
robotArm.report()