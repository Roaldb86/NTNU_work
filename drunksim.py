import math
import random
import pylab

class Location(object):
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def move(self, xc, yc):
        return Location(self.x + float(xc), self.y + float(yc))

    def getCoords(self):
        return self.x, self.y

    def getDist(self, other):
        ox, oy = other.getCoords()
        xDist = self.x - ox
        yDist = self.y - oy
        return math.sqrt(xDist**2 + yDist**2)


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
        # This variabel is set to to global because it is needed in the Drunk.moveAfterCrash method
        # if two drunks ends up in the same location
        global lastStep
        x = 0.0
        y = 0.0
        # A function within the method to limit the movement of the drunk to stay between
        # -10 and 10 for both x and y values, this makes the field in effect to be 20 x 20 meters
        def check(var, val):
            if abs(var + val) >= 10: return 0
            else: return val

        # For loop based on a random generated number of iterations. X and y values are added
        # based on the random direction the drunk will take
        for i in range(steps):
            step = random.choice(['N', 'W', 'S', 'E'])
            if step == 'N':
                y += check(y, 0.5)
            elif step == 'S':
                y += check(y, -0.5)
            elif step == 'E':
                x += check(x, 0.5)
            elif step == 'W':
                x += check(x, -0.5)

        # Last direction is saved to a global variabel to be used if the drunk collides with another
        lastStep = step
        return x, y

    def  moveAfterCrash(self, Loc):
        """
        If two drunks end up in the same location, this method will take newLoc (x, y) as input
        and make the drunk that crahes into another take a step back in the opposite direction.
        """
        # Coordinates where the collision occured is the foundation and based on the
        # direction of the last step, the drunk will take a step back
        x, y = Loc
        if lastStep == 'N':
            y -= 0.5
        elif lastStep == 'W':
            x += 0.5
        elif lastStep == 'E':
            x -= 0.5
        elif lastStep == 'S':
            y += 0.5
        return x, y


def visualplot(size, step_size):
    """
    Takes size of required field and step size as input and initializes
    a plot for x and y coordinates
    """
    fig = pylab.figure()
    ax = fig.add_subplot(1,1,1)
    pylab.ylim(size/-2, size/2)
    pylab.xlim(size/-2, size/2)
    pylab.title("multiple drunks in the same field")
    pylab.xlabel(" <-- 20 meters --> ")
    pylab.ylabel(" <-- 20 meters --> ")
    loc = pylab.MultipleLocator(base=step_size)
    ax.xaxis.set_major_locator(loc)
    ax.yaxis.set_major_locator(loc)
    pylab.grid()

def getDist(finalLocation):
    """ Returns distance from start (0,0) based on the location the drunk ends up in """
    x, y = finalLocation
    return math.sqrt(x**2 + y**2)


def performSim(number_of_drunks, trials):
    """ Does not work"""

    for i in range(trials):
        main(number_of_drunks)

    pylab.figure()
    pylab.title("Distances against trials")
    pylab.plot(distances, trials)
    pylab.show()




def main(number_of_drunks):


    trials = random.randint(1, 500)
    means = []
    distances = list()
    locations = list()
    drunks = list()
    number_of_crashes = 0

    # Call the plot function to initialize a plot
    visualplot(20, 0.5)

    # Initiate drunk objects
    for i in range(number_of_drunks):
        drunks.append(Drunk(i))

    # Move all the drunks, how many steps each drunk will take is a random number
    # between 1 and 500. the Drunk.move() method is used to move the drunkself.
    # If a drunk ends up in the same position as another drunk, he will take 1 step
    # back in the opposite direction as he came.
    for i in drunks:
        newLoc = i.move(trials)
        if newLoc in locations:
            newLoc = i.moveAfterCrash(newLoc)
            print("Collision with another drunk, last move was to the :", lastStep)
            number_of_crashes += 1

        else:
            locations.append(newLoc)

        distances.append(getDist(newLoc))
    print("Number of collisions between drunks :", number_of_crashes)

    # Plot all coordinates as a scatter diagram
    for i in locations:
        pylab.scatter(*zip(i),s=100, c=random.choice(['r','g','y','b']))
        # print(drunk.name,/ newLoc)


    pylab.figure()
    pylab.title("Ditance travelled for each drunk")
    pylab.xlabel("Drunk number:")
    pylab.ylabel("Distance from start")
    pylab.plot(distances)
    pylab.plot()
    pylab.show()

if __name__ == '__main__':
    main(100)

"""Jævla to-do lista"""
# <--2--> Skriv sim method/function
