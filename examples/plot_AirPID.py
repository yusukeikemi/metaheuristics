import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../'))

from codes.problems.AirPID import AirPID
from codes.algorithms.PfGA import PfGA
from codes.algorithms.PSO import PSO


def main():
    p = AirPID(5)
    a = PSO(3)

    p.init("C:/Users/YIkemi.DESKTOP-1O5DLKF/source/repos/FluidicSystem_AirPID/FluidicSystemServer/bin/x64/Debug")
    a.init(p)

    max_score = a.getMaxScore()
    for i in range(3):
        a.step()
        if max_score < a.getMaxScore():
            max_score = a.getMaxScore()
            print("{} {}".format(i, max_score))
    
    a.getMaxElement().view()

if __name__ == "__main__":
    main()
