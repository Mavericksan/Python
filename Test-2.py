#Test 2

import sys
from random import shuffle

Liste = 'excellent super'.upper().split()
shuffle(Liste)
print()
print(sys.platform)

print()
print()


for strophe in range(2):
    for zeile in range(2):
        for worte in range(4):
            print('SPAM ',end='')
        print()
print(Liste[0]+' SPAM '+Liste[1]+' SPAM')


