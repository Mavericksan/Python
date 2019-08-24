# Wie viele Reiskoerner passen auf ein Schachbrett

import matplotlib.pyplot as plt
import numpy as np

print()
summe = 0
teile_per_feld = []


for feld in range(64):
    reis=2**feld
    teile_per_feld.append(reis)
    summe += reis
    print('Auf {}. Feld sind {:>27,} Körner - auf dem Schachbrett {:>28,} \
        Körner'.format(feld+1,reis,summe))

#print(teile_per_feld)
plt.plot(teile_per_feld)
plt.show()
    