#visualize PI with 1 mio digits
#import turtle graphics module

import turtle as tu

#lines = 500_000

with open('1_mio_digits_of_PI.txt','r') as f:
    pi = f.read()

# print('PI auf {:,} Stellen'.format(len(pi)))
# print('Test der ersten 9 Stellen', pi[0:9],'   und die letzten 4 Stellen: ',pi[999_997:1_000_001],'\
#      oder die letzten 10 Stellen: ', pi[-10:])
# print()

# set turtle graphics modes

tu.mode('logo')
tu.tracer(False)
tu.screensize(12_000,16_000,'black')
#tu.pencolor('red')
tu.colormode(255)

# read string and convert single digits to integer for drawing the lines

lines=len(pi)
for n in range(lines):
    color=int((n/(lines/255)))
    zahl = int(pi[n])
    rotation = zahl * 36
    tu.pencolor(0+color,255-color,color)
    tu.setheading(rotation)
    tu.forward(8)

tu.done()

