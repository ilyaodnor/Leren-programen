import sys
sys.path.insert(0,'/Users/ilya/Documents/GitHub/School/Softwere dev./python/Leren-programen/Python/Module2/robotarm')
from RobotArm import RobotArm
from basic import challenges
robotArm = RobotArm(challenges[2],3)
robotArm.moveRight()
robotArm.grab()
robotArm.moveLeft()
robotArm.drop()
for i in range(2): robotArm.moveRight()
robotArm.grab()
robotArm.moveLeft()
robotArm.drop()
robotArm.moveLeft()
robotArm.grab()
for i in range (2): robotArm.moveRight()
robotArm.drop()
robotArm.report()
