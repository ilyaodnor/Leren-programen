start = 50
sum1 = 0
numbers_added = []
a = '50'

while sum1<=1000:
    current_range = list(range(start, start+1))
    a+= ' + ' + str(start)
    sum1 += sum(current_range)
    
    print(f'{a[4:]} = {sum1}')
    start+=1
    if sum1>= 1000:
        break
