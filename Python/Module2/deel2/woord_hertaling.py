a = ('In het hart van de grot zagen ze Draganthor,met zijn glimsterende schubben en vurige ogen. De draak brulde en spuwde een vlommenzee die hen bedreigde, maar Rurik beschermde hen met een krachtig schild van magie.')
print(a)

dict = {
    'In het hart': 'Bij de ingang',
    'schubben en vurige': 'teennagels en waterende ',
    'draak': 'geit',
    'vlammenzee ': 'golf van water',
    'schild van magie': 'zwemvliezen van plastic.',

}

for key, value in dict.items():
    a = a.replace(key, value)
print(a)