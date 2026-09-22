import matplotlib.pyplot as plt
from pid import Car1D

K_P = 0.1
K_I = 0.1
K_D = 0.1
 
STEPS = 550
 
car = Car1D(des_v=20.0, dt=0.1)

#WRITE CODE HERE