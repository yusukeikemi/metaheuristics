import unittest
import random
import time

import numpy as np

import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../'))

from codes.problems.AirPID import AirPID

class Test(unittest.TestCase):

    def test_1(self):
        p = AirPID(10)
        p.init("C:/Users/YIkemi.DESKTOP-1O5DLKF/source/repos/FluidicAnalysys/FluidicSystem_AirPID/FluidicSystemServer/bin/x64/Debug")

        arr = np.asarray([0.015, 0.003, 0.01, 1, 5, 0.055, 0.05, 0.02, 1, 5])
        score = p.eval(arr)
        self.assertEqual(score, -7.1542450698630855)

        #p.view(arr)
        

if __name__ == "__main__":
    unittest.main()