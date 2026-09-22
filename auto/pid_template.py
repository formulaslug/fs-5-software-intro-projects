import numpy as np

class Car1D:
    def __init__(self, des_v=20.0, dt=0.1):
        self.v = 0 #velocity of your car 
        self.a = 0 #acceleration of your car
        self.t = 0 #time of your car
        self.x = 0 #position of your car
        self.dt = dt #time step of your car, how much the time changes every time you update/step
        self.des_v = des_v #desired velocity of your car, the velocity you want to maintain
        self.step = 0

        #hint: use these variables in the integral and derivative portion of your PID control (steps 5 and 6 )
        self.error_prev = None
        self.net_integral = 0.0

    def update(self, throttle_perc, mass = 1000, max_throttle_force = 5000,  friction=2.0): 
        force = throttle_perc * max_throttle_force 
        self.a = (force / mass) - friction
        self.v += self.a * self.dt
        self.x += self.v * self.dt
        self.t += self.dt
        self.step += 1


    def calculate_des_accel(self, K_P, K_I=0.0, K_D=0.0):
        pass # delete this line and write your PID code here




    def accel_to_throttle(self, a_des, mass = 1000, max_throttle_force = 5000):
        pass # delete this line and write your code to convert desired acceleration to throttle here