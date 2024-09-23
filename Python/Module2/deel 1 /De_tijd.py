uuren = 1
dag_nacht = 'AM'
for i in range(24):
    print(f'{uuren} {dag_nacht}')
    if uuren>=11:
        dag_nacht = 'PM'
    else:
        pass
    uuren +=1