#visualize PI with 1 mio digits
#import turtle graphics module

import turtle as tu

lines = 10_000

with open('1_mio_digits_of_PI.txt','r') as f:
    pi = f.read()

# print('PI auf {:,} Stellen'.format(len(pi)))
# print('Test der ersten 9 Stellen', pi[0:9],'   und die letzten 4 Stellen: ',pi[999_997:1_000_001],'\
#      oder die letzten 10 Stellen: ', pi[-10:])
# print()

tu.mode('logo')
tu.tracer(False)
tu.screensize(5000,5000,'black')
tu.pencolor('red')



for n in range(lines):
    zahl = int(pi[n])
    rotation = zahl * 36
    tu.setheading(rotation)
    tu.forward(3)

tu.done()

