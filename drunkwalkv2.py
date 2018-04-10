import numpy as np
import math
import random
import pylab


class Field(object):
    def __init__(self, drunk, loc):
        self.drunk = drunk
        self.loc = loc

    def move(self, cp, dist):
        oldLoc = self.loc
        xc, xy = cp.move(dist)
        self.loc = oldLoc.move(xc, xy)

    def getLoc(self):
        return self.loc

    def getDrunk(self):
        return self.drunk

class Drunk(object):
    def __init__(self, name):
        self.name = name

    def name(self):
        return self.name

    def move(self, steps):
        """
        Takes steps as arguments and returns x and y coordinates after number of steps,
        but with -20 and 20 as a limit for both x and y
        """

        x = 0.0
        y = 0.0
        condition1 = False
        condition2 = False

        while condition1 == False and condition2 == False:
            for i in range(steps):
                if 10 <= x <= -10:
                    condition1 = True
                elif 10 <= y <= -10.:
                    condition2 = True
                else:
                    step = random.choice(['N', 'W', 'S', 'E'])
                    if step == 'N':
                        y += 0.5
                    elif step == 'S':
                        y -= 0.5
                    elif step == 'E':
                        x += 0.5
                    elif step == 'W':
                        x -= 0.5
                    else:
                        raise ValueError ("In Drunk.move")

            return x, y
        return x, y

def visualplot(size, step_size):
    """Takes size of required field and step size as input and initializes a plot"""
    fig = pylab.figure()
    ax = fig.add_subplot(1,1,1)
    pylab.ylim(size/-2, size/2)
    pylab.xlim(size/-2, size/2)
    loc = pylab.MultipleLocator(base=step_size) # this locator puts ticks at regular intervals
    ax.xaxis.set_major_locator(loc)
    ax.yaxis.set_major_locator(loc)
    pylab.grid()



def main():
    locations = list()
    objects = list()
    number_of_crash = 0
    visualplot(20, 0.5)

    # How many drunks in the field
    for i in range(100):
        objects.append(Drunk(i))
    for i in objects:

        newLoc = i.move(random.randint(0, 500))
        if newLoc in locations:
            # newLoc = i.move(random.randint(1, 5))
            number_of_crash += 1
            pass

        else:
            locations.append(newLoc)



        # Unpack coordinates for plotting
        # x, y = newLoc
        # Debugging

    print(number_of_crash)

    for i in locations:
        pylab.scatter(*zip(i),s=100, c=random.choice(['r','g','y','b']))
        # print(drunk.name,/ newLoc)

    pylab.show()

if __name__ == '__main__':
    main()
