input_gastheer = input('Wat is de naam van de gastheer?').capitalize()
gastengetaal = int(input('hoeveel gasten?'))
gastheer = 'Ilya'
gastheer_slb_er = 'Runi'
gasten = range(4,21)
drank = True
chips = True

start_condition_1 = input_gastheer!= gastheer_slb_er or gastengetaal in gasten

if start_condition_1 and input_gastheer != gastheer_slb_er :
    if gastengetaal in gasten   and  drank and chips:
        print("Start the Party")
    elif gastheer and drank:
        print("Start the Party")
    elif gastheer and gastengetaal in gasten and drank and chips or gastheer and drank and chips:
        print("Start the Party")
else:
    print('No Party')

