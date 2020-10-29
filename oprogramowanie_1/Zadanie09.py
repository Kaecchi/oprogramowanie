# -*- coding: utf-8 -*-

# Zadanie 9 ---------------------------------

kwota = float(input('Proszę podać kwotę pieniężną: '))

kwota_temp = kwota
temp = 0.0

tekst = ''

ile_200 = int(kwota_temp/200)
kwota_temp -= 200 * ile_200

ile_100 = int(kwota_temp/100)
kwota_temp -= 100 * ile_100

ile_50 = int(kwota_temp/50)
kwota_temp -= 50 * ile_50

ile_20 = int(kwota_temp/20)
kwota_temp -= 20 * ile_20

ile_10 = int(kwota_temp/10)
kwota_temp -= 10 * ile_10

ile_5 = int(kwota_temp/5)
kwota_temp -= 5 * ile_5

ile_1 = int(kwota_temp/1)
kwota_temp -= 1 * ile_1

print('\nIlość potrzebnych nominałów: ')
print('\n200 zł:', ile_200, '\n100 zł:', ile_100, '\n50  zł:', ile_50, '\n20  zł:', ile_20, '\n10  zł:', ile_10, '\n5   zł:', ile_5, '\n1   zł:', ile_1)
