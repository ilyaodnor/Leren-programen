import sys
sys.path.insert(0,'/Users/ilya/Documents/GitHub/School/Softwere dev./python/Leren-programen/Python/Module2/robotarm')
from RobotArm import RobotArm
from master import challenges
robotArm = RobotArm(challenges[3],2)
kleuren = {'red':0,'green':0,'blue':0,'yellow':0,'purple':0,'orange':0,'white':0,'n':0,'l':0, 'gray': 0, 'black':0,}
lijst = []
for i in range(2): robotArm.moveRight()
for i in range(2):
     robotArm.moveRight()
     for i in range(4):
        robotArm.grab()
        a = robotArm.scan()
        if a not in lijst:
           lijst.append(a)
        robotArm.moveLeft()
        robotArm.drop()
        robotArm.moveRight()
for i in range(2):
     robotArm.moveLeft()
     for i in range(4):
        robotArm.grab()
        a = robotArm.scan()
        if a not in lijst:
           lijst.append(a)
        robotArm.moveRight()
        robotArm.drop()
        robotArm.moveLeft()

robotArm.moveRight()
for i in range(4):
    for j in  range(4):
        robotArm.grab()
        a = robotArm.scan()
        if a == lijst[0]:
           index = robotArm.stackIndex()
           while robotArm.stackIndex()!= 0: robotArm.moveLeft()
           robotArm.drop()
           while robotArm.stackIndex()!=index: robotArm.moveRight()
        elif a == lijst[1]:
           index = robotArm.stackIndex()
           while robotArm.stackIndex()!= 1: robotArm.moveLeft()
           robotArm.drop()
           while robotArm.stackIndex()!=index: robotArm.moveRight()
        elif a == lijst[2]:
           index = robotArm.stackIndex()
           while robotArm.stackIndex()!= 9: robotArm.moveRight()
           robotArm.drop()
           while robotArm.stackIndex()!=index: robotArm.moveLeft()
        elif a == lijst[3]:
           index = robotArm.stackIndex()
           while robotArm.stackIndex()!= 8: robotArm.moveRight()
           robotArm.drop()
           while robotArm.stackIndex()!=index: robotArm.moveLeft()
    robotArm.moveRight()
robotArm.report()
