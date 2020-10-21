# -*- coding: utf-8 -*-

# Zadanie 7 ---------------------------------

print('\nW jakiej skali chcesz podać temperaturę?')
print('\nW °C i dostać wartość w °F - wpisz cel \nW °F i dostać wartość w °C - wpisz fah')

typ = input('Proszę podać odpowiedź: ')

if typ == 'cel' :
    cel = float(input('Proszę podać temperaturę w °C: '))
    fah = (cel * (9/5)) + 32

    print(cel, '°C =', fah, '°F')
    
elif typ == 'fah':
    fah = float(input('Proszę podać temperaturę w °F: '))
    cel = (fah - 32) * 5/9

    print('\n', fah, '°F =', cel, '°C')
    
else:
    print('\nNie podano prawidłowej skali.')
