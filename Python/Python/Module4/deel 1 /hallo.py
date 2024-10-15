def hello(hoeveelheid: int):
    for i in range(1, hoeveelheid +1):
        print(f'Hello from function town {i}!!')
    return
    
hello(int(input('integer:')))