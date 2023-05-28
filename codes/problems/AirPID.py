import numpy as np
import os
import sys
sys.path.append("C:/Users/YIkemi.DESKTOP-1O5DLKF/source/repos/metaheuristics/codes")
from problem import Problem

sys.path.append("C:/Users/YIkemi.DESKTOP-1O5DLKF/source/repos/FluidicAnalysys")
import airpidadjust as apa

class AirPID(Problem):
    def __init__(self, size):
        super().__init__(self, size)
        self.MIN_VAL = 0
        self.MAX_VAL = 1
        # Default path
        self.base_path="C:/Users/YIkemi.DESKTOP-1O5DLKF/source/repos/FluidicSystem_AirPID/FluidicSystemServer/bin/x64/Debug"
    

    def init(self, base_path):
        self.base_path = base_path

    
    def eval(self, np_arr):
        #base_path="C:/Users/YIkemi.DESKTOP-1O5DLKF/source/repos/FluidicSystem/FluidicSystemServer/bin/x64/Debug"
        self.base_path="C:/Users/YIkemi.DESKTOP-1O5DLKF/source/repos/FluidicSystem_AirPID/FluidicSystemServer/bin/x64/Debug"
    
        apasimu = apa.AirPIDAdjust(self.base_path,debug = True)
        #base params = 0.015, 0.003, 0.01, 1, 5, 0.055, 0.05, 0.02, 1, 5
        # np_arr comes as a numpy array with 0~1 values
        # scale the values to the range of the problem
        if self.size == 5:
            scaled_arr = np.tile(np_arr, 2)
        scaled_arr = self.scaleparam(scaled_arr)
        print("Simulation input ki, kd, kp, Td, Ti, ki_i, kd_i, kp_i ,Td_i, Ti_i = ")
        print(str(scaled_arr))
        
        # testparams take tuple as input
        # simlation_output will be None if simulation fails
        simulation_output = apasimu.testparams(tuple(scaled_arr))
        if simulation_output is None:
            # return the worst score
            simulation_output = 1000
        # maximize the output
        print("Simulation output = " + str(-simulation_output))
        return -simulation_output
    
    def scaleparam(self, np_arr):
        # np_arr comes as a numpy array with 0~1 values
        # scale the values to the range of the problem
        # 0~1 -> 0~0.1
        np_arr[0]= np_arr[0]*0.5
        np_arr[1]= np_arr[1]*0.5
        np_arr[2]= np_arr[2]*0.5
        np_arr[3]= np_arr[3]*10
        np_arr[4]= np_arr[4]*10
        np_arr[5]= np_arr[5]*0.5
        np_arr[6]= np_arr[6]*0.5
        np_arr[7]= np_arr[7]*0.5
        np_arr[8]= np_arr[8]*10
        np_arr[9]= np_arr[9]*10
        return np_arr


