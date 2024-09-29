import sys
sys.path.insert(0,'/Users/ilya/Documents/GitHub/School/Softwere dev./python/Leren-programen/Python/Module2/robotarm')
from RobotArm import RobotArm
from beginner import challenges
robotArm = RobotArm(challenges[2],3)
robotArm.moveRight()
for i in range(6):
    robotArm.grab()
    if robotArm.scan() == 'blue':
        robotArm.moveLeft()
        robotArm.drop()
        robotArm.moveRight()
    else:
        robotArm.moveRight()
        robotArm.drop()
        robotArm.moveLeft()
robotArm.report()