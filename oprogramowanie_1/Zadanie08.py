# -*- coding: utf-8 -*-

# Zadanie 8 ---------------------------------

tydzien = ['poniedziałek', 'wtorek', 'środa', 'czwartek', 'piątek', 'sobota', 'niedziela']

dzien = int(input('Proszę podać numer dnia tygodnia (cyfra od 1 do 7): '))

if dzien > 7 or dzien < 1:
    print('\nPodano nieprawidłowy numer')
elif dzien >= 1 and dzien <= 7:
    print('\nDzień tygodnia pod numerem', dzien, 'to', tydzien[dzien-1])
