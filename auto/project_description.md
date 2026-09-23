# Project 1: PID controller

![PID Math](./pid-equation-all-terms.png)

The PID controller(above) uses 3 terms with 3 tuned constants, to compute a command that minimizes error. 

### Intro

This project is to give you an introduciton on part of what we do in autonomous. This will focus on the controls planning part of our software stack. We do many other projects in autonomous, so if you don't like this don't worry we have many more options. 

There are two templates in this folder that can help you start, the instructions will refer to parts of those specific templates although you're free to do your own thing. We have linked resources to help, but if you ever need more I defintely suggest just googling, the topics in this project are very well covered online and there are tons of helpful resources. 

### Brief on PID Controllers:

Before building I reccomend watching this [matlab video](https://www.mathworks.com/discovery/pid-control.html) on PID controllers once through, if you don't undertsnd it immediately don't worry. Completeing this project will help you have a solid grasp on PID controllers, which are a fundamental yet simple control method used in many machines. 

### If you haven’t taken Calculus:

Understanding what a derivative and integral are conceptually is important to fully understanding how PID controllers work. Here is a crash course by the [Organic Chemistry Tutor](https://www.youtube.com/watch?v=WsQQvHm4lSw&t=434s), I reccomend to skip to 17:00 and watch his description of the two.

The needed understanding for this project is: Integral is the TOTAL error throughout a run measured by the area accumulated under a curve measuring error at each time step. And the derivative is HOW FAST the error is increasing or decreasing measured by the slope.

### Project Instructions

**PROJECT GOAL**: Given a simplified 1-dimensional car model, `Car1D`. Build a PID controller which makes the car’s velocity converge toward a desired velocity. Use provided equation above for reference throughout this project. 

Here is a flow chart of the complete system. Please use this in combination with the provided equations in the top image. Each term in the flowchart is shown in the equation sheet. ![PID FLOW](./flowchart.drawio.png)

0. First make sure you have matplotlib in your enviroment, you can also use numpy if you want to, but it isn't needed. 

1. Using the desired velocity, `desired_vel`, and the current velocity, `self.v`, it’s useful to calculate the difference between the two, representing the error of our controller. This error is useful as it will be used to calculate how much acceleration we need to reach the desired velocity, given our current velocity. Your first controller iteration will use a constant, `K_P`, proportional to the error to find the required acceleration. 
    
    Write a function, `calculate_desired_acceleration`, that returns the error and desired acceleration, only using the proportional term of the controller( no `K_I` or `K_D` ). Please refer to the provided image for help. In the image C(command) is desired acceleration in our project.
    

2. For the car to reach the desired acceleration you calculated it needs to be converted to a value for the motor. In this simplified model we’ll convert it straight to a force using Newton’s second law, and then to a throttle percentage(-1 to 1) using a max throttle force. 
    
    Write a function, `accel_to_throttle`, that returns a throttle percentage as a float between -1 and 1.
    

3. Build a run script using matplotlib to make two plots one of your car’s velocity and one of the error over each time step. If you know another way to visualize data than the one described below go ahead, this is just to help.
    -  Create three lists to track your velocities, errors, and times.
    - Create a loop that fills your two lists with their correct data over the number of `STEPS`. Use methods you built of the `car` instance to get data. Make sure to use `car.update` with throttle as an input to update all the state variables.
    - Build two plots using [matplotlib.pyplot](https://matplotlib.org/stable/tutorials/pyplot.html) showing your data. 
        - Error over time and Velocity over Time 
    - Both of your graphs should converge to a specific value if done correctly. 

4. Use your run.py to tune the `K_P` constant so that your car’s velocity converges closest to the desired velocity. 
    - Start low, below 1 with constants. 
    - Note if you are able to get it to reach the desired velocity. In the first linked PID video, they talk about why this happens. 
    - Before moving on either think about it yourself or rewatch the video or google "Steady state error pid" until you understand what is causing the velocity to not reach the desired velocity. Hint: Look at the car model's code to see how it calculates acceleration at each step. 

5. Refer back to the PID equation to now implement the integral term of the controller. You’ll want to use the `self.net_integral` so you can track the error as it accumulates over multiple steps. 
    - Using run.py once more tune your controller towards the dseirev velocity. Note how is you graph is different this time.

6. Now implement the deritvative term. You’ll want to use `self.error_prev` .
    - Once more use run.py and mess around with the values of all three constants. Try and understand what each does.

7. Look up a PID tuning table to compare and contrast your observations to the actual functions of constants. 
    - Change the desired velocity, `des_v`, to multiple different values and use the table to help you tune the controller. 

8. **Extensions** ( Do 2-3, if you do #9 you don't need to do any )

    - Implement a stopping point into the PID controller, slows to a stop by a certain distance. 
    - Research gain scheduling for pid’s and implement into your system.
    - Research pid integral windup, find at what constants this happens in your controller and try to fix it.
    - Add in a additional forces against the car, increasing/decreaing the friction in intervals throughout the steps. Figure out how to minimize velocity instability during the increased friction. 

9.  **Optional Machine Learning Extension**
    
    **Goal**: Build a linear regression model trained on your PID data, to predict the desired acceleration given the current velocity and desired velocity. 

    - If you have a better/different machine learning application using PID data generated from your project you can defintely try that instead.

    - If you haven’t worked with machine learning before, I reccomend learning [here](https://www.learnpytorch.io/00_pytorch_fundamentals/). The first two sections 00 and 01 walk you through building a linear regression model. Build their training, plotting, and model first so you can understand everything. Then adapt it or build the pid data one. 
   
    **Hints:**
    
    - If you follow the linked resource to make a linear regression model, the next step to take are:
      - Adjusting your run.py or making a new script to generate tensors of your pid data
      - Change the model to work with your data shape 
      - Change the prediction's plotting to fit your data shape
    - Set `K_I` and `K_D` to zero when generating data, since both depend on variables outside v and v_des.
    - When creating PID data make sure to have the desried velocity change throughout the steps to get data with different values.
    - Adjust your learning rate if your loss isn't dropping, this was a change I made when testing