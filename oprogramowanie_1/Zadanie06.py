# -*- coding: utf-8 -*-

import math

# Zadanie 6 ---------------------------------

rad = float(input('Proszę podać promień okręgu: '))

circ = 2 * rad * math.pi
area = rad**2 * math.pi

print('\nOkrąg o promieniu', rad, 'ma: \n obwód równy', circ, '\n pole równe', area)
