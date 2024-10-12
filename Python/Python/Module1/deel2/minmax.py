a = int(input('getaal a:   '))
b = int(input('getaal b:   '))


if a > b :
    min_getaal = min(a, b) 
    max_getaal = max(a, b)
    print(f'Getaal a is groter dan b:\n         max: {max_getaal}>min: {min_getaal}')


elif b>a:
    min_getaal = min(a, b) 
    max_getaal = max(a, b)
    print(f'getal b is groter dan a:\n          max: {max_getaal}>min: {min_getaal}')
else:
    print(f'a en b zijn even groot:    {a} ==  {b}')