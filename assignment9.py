import math
from random import *
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


class CompassPt(object):
    possibles = ('N', 'S', 'E', 'W')

    def __init__(self, pt):
        if pt in self.possibles:
            self.pt = pt
        else:
            raise ValueError('in CompassPt.__init__')

    def move(self, steps, start):
        x, y = start
        condition1 = False
        condition2 = False

        while condition1 == False and condition2 == False:
            for i in range(steps):
                if x <= (-20.0):
                    condition1 = True
                elif x >= 20.0:
                    condition1 = True
                elif y <= (-20.0):
                    condition2 = True
                elif y >= 20.0:
                    condition2 = True
                else:
                    step = choice(['N', 'W', 'S', 'E'])
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
            return x,y
        return x, y


class Field(object):
    def __init__(self, drunk, loc):
        self.drunk = drunk
        self.loc = loc

    def move(self, cp, dist):
        oldLoc = self.loc
        xc, yc = cp.move(dist)
        self.loc = oldLoc.move(xc, yc)

    def getLoc(self):
        return self.loc

    def getDrunk(self):
        return self.drunk


class Drunk(object):
    def __init__(self, name):
        self.name = name

    def move(self, field, time=1):
        if field.getDrunk() != self:
            raise ValueError('Drunk.move called with drunk not in field')
        for i in range(time):
            pt = CompassPt(choice(CompassPt.possibles))
            field.move(pt, 1)

    def performTrial(time, f):
        start = f.getLoc()
        distances = [0.0]
        for t in range(1, time + 1):
            f.getDrunk().move(f)
            newLoc = f.getLoc()
            print(newLoc)
            distance = newLoc.getDist(start)
            distances.append(distance)
        return newLoc

for i in range(1):
    drunk = Drunk(i)

    f = Field(drunk, Location(0, 0))
    location = Drunk.performTrial(10, f)

    # pylab.plot()
    pylab.title('Drunk students')
    pylab.xlabel('Time')
    # pylab.grid(1,1)
    pylab.ylabel('Distance from Origin')
    pylab.scatter(newLoc)
    # pylab.plot(location)

def performSim(time, numTrials):
    distLists = []
    for trial in range(numTrials):
        d = Drunk('Drunk' + str(trial))
        f = Field(d, Location(0, 0))
        distances = Drunk.performTrial(time, f)
        distLists.append(distances)
    return distLists


def ansQuest(maxTime, numTrials):
    means = []
    distLists = performSim(maxTime, numTrials)
    for t in range(maxTime + 1):
        tot = 0.0
        for distL in distLists:
            tot += distL[t]
        means.append(tot / len(distL))
    pylab.figure()
    pylab.plot(means)
    pylab.ylabel('distance')
    pylab.xlabel('time')
    pylab.title('Average Distance vs. Time (' + str(len(distLists)) + ' trials)')


# ansQuest(500, 300)
pylab.show()
