import sys
sys.path.insert(0,'/Users/ilya/Documents/GitHub/School/Softwere dev./python/Leren-programen/Python/Module2/robotarm')
from RobotArm import RobotArm
from master import challenges
robotArm = RobotArm(challenges[2],2)
kleuren = {'red':0,'green':0,'blue':0,'yellow':0,'purple':0,'orange':0,'white':0,'n':0,'l':0, 'gray': 0, 'black':0,}
robotArm.showSolution()
for i in range(4):
    robotArm.moveRight()
for i in range(6):
    robotArm.grab()
    kleur = robotArm.scan()
    kleuren[kleur] += 1
    robotArm.drop()
    if i !=5: robotArm.moveRight()

sorted_keys = sorted(kleuren, key=kleuren.get, reverse=True)

print(sorted_keys)
for i in range(6):
    robotArm.grab()
    a = robotArm.scan()
    if a == sorted_keys[0]:

        if i == 0:
            robotArm.drop()
            robotArm.moveLeft()
        elif i >=1:
            index1 = robotArm.stackIndex()
            print('stack index : ', index)
            while robotArm.stackIndex()!=9: 
                robotArm.moveRight()
                index+=1
            robotArm.drop()
            while robotArm.stackIndex()!= index1: robotArm.moveLeft()
            if i!= 6: robotArm.moveLeft()
    
    elif a == sorted_keys[1]:
        index = robotArm.stackIndex()
        while robotArm.stackIndex()!=0: robotArm.moveLeft()    
        robotArm.drop()
        while robotArm.stackIndex()!= index: robotArm.moveRight()
        robotArm.moveLeft()

    elif a == sorted_keys[2]:
        index = robotArm.stackIndex()
        while robotArm.stackIndex()!= 1: robotArm.moveLeft()
        robotArm.drop()
        while robotArm.stackIndex() != index: robotArm.moveRight()
        robotArm.moveLeft()

for i in range(2):
    while robotArm.stackIndex()!= 0:robotArm.moveLeft()
    robotArm.grab()
    while robotArm.stackIndex()!=8:
        robotArm.moveRight()
    robotArm.drop()
while robotArm.stackIndex()!=1:
    robotArm.moveLeft()
robotArm.grab()
while robotArm.stackIndex()!= 7:
    robotArm.moveRight()
robotArm.drop()
    

robotArm.report()




