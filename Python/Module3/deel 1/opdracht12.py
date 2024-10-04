from fruitmand import fruitmand
laangste = max(fruitmand,key = lambda fruit: len(fruit['name']))
print(f'De {laangste['name']} ({len(laangste['name'])}) heeft een {laangste['color']} en een gewicht van {str(laangste['weight']/1000)} kg.')