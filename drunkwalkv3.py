
import math
import random
import pylab

# step = ''

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
        global step
        x = 0.0
        y = 0.0

        withinField = True
        while withinField == True:
            if (10.0 <= x <= -10.0) or (10.0 <= y <= -10.0):
                withinField = False
            else:
                for i in range(steps):
                    # print("before field test; ", x, y)
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

            # print("After step choice: ", x, y)
            return x, y
        print("If field test is met: ", x, y)
        return x, y

    def  moveAfterCrash(self, newLoc):
        """
        If two drunks end up in the same location, this method will take newLoc (x, y) as input
        and make the drunk that crahes into another take a step back in the opposite direction.
        """
        global step
        x, y = newLoc

        if step == 'N':
            y -= 0.5
        elif step == 'W':
            x += 0.5
        elif step == 'E':
            x -= 0.5
        elif step == 'S':
            y += 0.5
        return x, y




def visualplot(size, step_size):
    """Takes size of required field and step size as input and initializes a plot"""
    fig = pylab.figure()
    ax = fig.add_subplot(1,1,1)
    pylab.ylim(size/-1, size/1)
    pylab.xlim(size/-1, size/1)
    pylab.title("multiple drunks in the same field")
    pylab.xlabel(" <-- 20 meters --> ")
    pylab.ylabel(" <-- 20 meters --> ")
    loc = pylab.MultipleLocator(base=step_size)
    ax.xaxis.set_major_locator(loc)
    ax.yaxis.set_major_locator(loc)
    pylab.grid()

def getDist(finalLocation):
    x, y = finalLocation
    return math.sqrt(x**2 + y**2)



def main():
    # global step
    locations = list()
    distances = list()
    drunks = list()
    number_of_crashes = 0
    visualplot(20, 0.5)

    # How many drunks in the field
    for i in range(100):
        drunks.append(Drunk(i))

    for i in drunks:

        newLoc = i.move(random.randint(0, 500))

        if newLoc in locations:
            newLoc = i.moveAfterCrash(newLoc)
            print("Collision with another drunk, last move was to the :", step)
            number_of_crashes += 1


        else:
            locations.append(newLoc)
        distances.append(getDist(newLoc))
    print(distances)
    print(number_of_crashes)

    # Plot all coordinates as a scatter diagram
    for i in locations:
        pylab.scatter(*zip(i),s=100, c=random.choice(['r','g','y','b']))
        # print(drunk.name,/ newLoc)
    pylab.figure()
    pylab.plot(distances)
    pylab.show()

if __name__ == '__main__':
    main()

"""Jævla to-do lista"""
# <--1--> Fix Fixed field limit
# <--2--> Skriv sim method/function
#
