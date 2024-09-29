import sys
sys.path.insert(0,'/Users/ilya/Documents/GitHub/School/Softwere dev./python/Leren-programen/Python/Module2/robotarm')
from RobotArm import RobotArm
from beginner import challenges
robotArm = RobotArm(challenges[3],3)
for i in range(5):
    robotArm.grab()
    for i in range(4): robotArm.moveRight()
    robotArm.drop()
    for i in range(4): robotArm.moveLeft()
robotArm.report()