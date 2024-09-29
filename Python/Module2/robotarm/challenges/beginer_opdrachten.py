import sys
sys.path.insert(0,'/Users/ilya/Documents/GitHub/School/Softwere dev./python/Leren-programen/Python/Module2/robotarm')
from RobotArm import RobotArm
from beginner import challenges
robotArm = RobotArm(challenges[1],3)
for i in range(4):
    robotArm.grab()
    robotArm.moveRight()
    robotArm.drop()
    if i != 3: robotArm.moveLeft()
robotArm.report()