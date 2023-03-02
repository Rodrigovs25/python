"""from calendar import monthcalendar
# print(monthcalendar(2020, 11))
for semana in monthcalendar(2020, 11):
    for dia in semana:
        print('%s\t' % dia,)"""
from string import join
# join = transformar listas em strings
from calendar import monthcalendar
s = monthcalendar(2020, 3)
join(map(str, s), '\t')
for semana in monthcalendar(2000, 3):
    print(join(map(str, semana), '\t'))
