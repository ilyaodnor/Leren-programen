import sys
sys.path.insert(0,'/Users/ilya/Documents/GitHub/School/Softwere dev./python/Leren-programen/Python/Module2/robotarm')
from RobotArm import RobotArm
from medium import challenges
robotArm = RobotArm(challenges[5],2)
for i in range(4): robotArm.moveRight()
a = 1
b=2
for i in range(5):
    robotArm.grab()
    for _ in range(a): robotArm.moveRight()
    a+=2
    robotArm.drop()
    if i!=4:
        for _ in range(b):robotArm.moveLeft()
    b+=2
robotArm.showSolution()
robotArm.report()
