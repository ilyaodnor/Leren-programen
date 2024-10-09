def hello(hoeveelheid):
    
    for i in range(1, int(hoeveelheid)+1):
        print(f'Hello from function town{i}!!')
    return
    
hello(input('integer:'))