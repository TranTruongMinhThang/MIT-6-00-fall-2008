def performSim(time, numTrials):
    distLists = []
    for trial in range(numTrials):
        d = Drunk('Drunk' + str(trial))
        f = Field(d, Location(0, 0))
        distances = performTrial(time, f)
        distLists.append(distances)
    return distLists

def ansQuest(maxTime, numTrials):
    means = []
    distLists = performSim(maxTime, numTrials)
    for t in range(maxTime + 1):
        tot = 0.0
        for distL in distLists:
            tot += distL[t]
        means.append(tot/len(distL))
    pylab.figure()
    pylab.plot(means)
    pylab.ylabel('distance')
    pylab.xlabel('time')
    pylab.title('Average Distance vs. Time (' + str(len(distLists)) + ' trials)')
ansQuest(500, 100)
pylab.show()

