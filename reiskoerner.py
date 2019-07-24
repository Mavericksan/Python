# Wie viele Reiskoerner passen auf ein Schachbrett

print()
summe = 0

for feld in range(64):
    reis=2**feld
    summe=summe+reis
    print('Auf Feld: {} befinden sich {} Reiskörner und damit auf dem Schachbrett {} \
        Reiskörner'.format(feld+1,reis,summe))

for i in range(3):
        print()
    