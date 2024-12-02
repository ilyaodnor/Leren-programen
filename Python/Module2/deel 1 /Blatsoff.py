import time
print('de raket lanceert in 30 seconden')
time.sleep(1)
a = 29

for i in range(29):
    print(f'{a} seconden')
    a-=1
    time.sleep(1)
print('GO!!!')