import sys
sys.path.insert(0,'/Users/ilya/Documents/GitHub/School/Softwere dev./python/Leren-programen/Python/Module2/robotarm')
from RobotArm import RobotArm
from medium import challenges
robotArm = RobotArm(challenges[1],3)
for i in range(8): robotArm.moveRight()
for j in range(9):
    robotArm.grab()
    for d in range(1): robotArm.moveRight()
    robotArm.drop()
    if j!= 8:
        for b in range (2): robotArm.moveLeft()
    d+=1
    b+=1
robotArm.report()