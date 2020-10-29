# -*- coding: utf-8 -*-

# Zadanie 5 ---------------------------------

print('\nJakiego typu mają byc podane liczby?')
print('\nZmiennoprzecinkowe - wpisz float \nCałkowite - wpisz int')

typ = input('Proszę podać rodzaj: ')

if typ == 'float' :
    x = float(input('Proszę podać pierwszą liczbę: '))
    y = float(input('Proszę podać drugą liczbę: '))
    
    if x > y:
        print('\nLiczba', x, 'jest większa od liczby', y)
    elif y > x:
        print('\nLiczba', y, 'jest większa od liczby', x)
    elif x == y:
        print('\nPodane liczby są równe - obie mają wartość', x)
    
elif typ == 'int':
    x = int(input('Proszę podać pierwszą liczbę: '))
    y = int(input('Proszę podać drugą liczbę: '))
    
    if x > y:
        print('\nLiczba', x, 'jest większa od liczby', y)
    elif y > x:
        print('\nLiczba', y, 'jest większa od liczby', x)
    elif x == y:
        print('\nPodane liczby są równe - obie mają wartość', x)
    
else:
    print('\nNie podano prawidłowego rodzaju.')
