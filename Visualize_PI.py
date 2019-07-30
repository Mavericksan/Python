#visualize PI with 1 mio digits

with open('1_mio_digits_of_PI.txt','r') as f:
    pi = f.read()

print('PI auf {:,} Stellen'.format(len(pi)))
print(pi[0],pi[1],'   ',pi[1000000])
