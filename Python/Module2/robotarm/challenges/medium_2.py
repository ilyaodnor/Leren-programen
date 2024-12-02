import sys
sys.path.insert(0,'/Users/ilya/Documents/GitHub/School/Softwere dev./python/Leren-programen/Python/Module2/robotarm')
from RobotArm import RobotArm
from medium import challenges
robotArm = RobotArm(challenges[2],3)
a = 2
for i in range(5):
    for j in range(6):
            robotArm.moveRight()
            robotArm.grab()
            robotArm.moveLeft()
            robotArm.drop()
    for d in range(a):
        if i!=4 :robotArm.moveRight()
robotArm.report()