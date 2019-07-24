# Wie viele Reiskoerner passen auf ein Schachbrett

print()
summe = 0

for feld in range(64):
    reis=2**feld
    summe += reis
    print('Auf {}. Feld sind {:>27,} Körner - auf dem Schachbrett {:>28,} \
        Körner'.format(feld+1,reis,summe))

for i in range(3):
        print()
    