# This file describes the Physics class which is inherited by other classes in the simulation
import numpy as np


class Physics:
    '''
    The class stores a dict with the following values

    t0 : tight_binding parameter
    Delta : superconducting order paramter
    phase : phase-difference between the superconducting contacts
    (mu1,mu2) : chemical potential of the two contacts
    N_D : number of points in the device
    '''
    def __init__(self,param):
        self.param = param

    def create_Hamiltonian(self):
        t0 = self.param['t0']
        N_D = self.param['N_D']


        alpha = np.array([[2*t0,0],[0,2*t0]])
        beta = np.array([[-t0,0],[0,-t0]])
        
        H = np.zeros((N_D,N_D,2,2))
        # desperation, I can't find a better way than to loop over
        for i in range(N_D):
            H[i,i] = alpha

            if i > 0:
                H[i-1,i] = beta        

            if i < (N_D-1):
                H[i+1,i] = beta 

        self.H = H
    

        
        
         
     
        
    
        
