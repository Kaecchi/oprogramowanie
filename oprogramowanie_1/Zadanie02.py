# -*- coding: utf-8 -*-

# Zadanie 2 ---------------------------------

print('\nJakiego typu mają byc podane liczby?')
print('\nZmiennoprzecinkowe - wpisz float \nCałkowite - wpisz int')

typ = input('Proszę podać rodzaj: ')

if typ == 'float' :
    x = float(input('Proszę podać pierwszą liczbę: '))
    y = float(input('Proszę podać drugą liczbę: '))
    suma = x + y
    
    print('\n', x, '+', y, '=', suma)
    
elif typ == 'int':
    x = int(input('Proszę podać pierwszą liczbę: '))
    y = int(input('Proszę podać drugą liczbę: '))
    suma = x + y
    
    print('\n', x, '+', y, '=', suma)
    
else:
    print('\nNie podano prawidłowego rodzaju.')
    