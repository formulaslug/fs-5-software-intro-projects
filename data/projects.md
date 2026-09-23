# Intro Project
This project is a step by step idea of how a data project would work. Using a parquet file provided, you must either derive or graph what is asked of you. All the necessary information is provided either in this or the parquet file. Submit your work on a PDF. If you are stuck on a step, please write down your approach and where you got stuck.

1. Using parquet logic, forward fill and print all the values in a table format from the file. Provide a screenshot from the time stamp 15s-30s. 
2. a) Using matplotlib, graph the speed vs time. Refer to the [data_columns.csv](https://github.com/formulaslug/fs-5-software-intro-projects/blob/main/data/data_columns.csv) to know which column means what. Use that to find the speed of the car at 10s.
3. Find out how many laps the car drove as well as the start and end time for each lap. Provide a screenshot of your method along with an explanation of how you went about finding this.
4. Give a time frame for when the car is accelerating, braking, and coasting. Explain how you found these values out. Then plot those states over time (either on three different graphs or one with different colors).
5. Using the lap times found from part 3, determine the max speed, max acceleration, time spent accelerating, and time spent coasting. 
6. From the coasting data (from all laps), remove anything below 5 m/s and anything below a second. 
7. Use that coast down data to determine vehicle drag + rolling resistance. If you do not have a background in physics, you can research how to go about doing this and include it in your work. Provide both values as well as an explanation on how you did this.

## **Information you might need**
Gear ratio: 12/41 (sprocket ratio, motor-to-wheel)  
Wheel radius: 0.2 m  
Car mass: 221.4 kg  
Air density: 1.225 kg/m³  
Rotational inertia adder: 22.68 kg

