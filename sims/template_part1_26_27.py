import matplotlib.pyplot as plt
from matplotlib import animation

class Car:
    def __init__():
        pass
    
    def required_front_force():
        pass

    def required_rear_force():
        pass

#define a Car object:


#Initializing lists to store speeds and axle forces:
speeds = []
front_axle_force = []
rear_axle_force = []


for i in range(): # the range of speeds you want to try out
    velocity = i/10.0 

    # calculate front and rear force for the car object you created
    #  append lists created above


#animation below, DONT edit
fig, ax = plt.subplots(figsize=(8, 5))


line_front, = ax.plot(speeds, front_axle_force, label="Front Axle Force ($F_{yf}$)", color="blue")
line_rear, = ax.plot(speeds, rear_axle_force, label="Rear Axle Force ($F_{yr}$)", color="orange")


ax.set_title("Lateral Axle Demand vs. Vehicle Speed")
ax.set_xlabel("Speed (m/s)")
ax.set_ylabel("Lateral Force (N)")
ax.set_xlim(min(speeds), max(speeds))
max_force = max(max(front_axle_force), max(rear_axle_force))
ax.set_ylim(0, max_force * 1.1 if max_force > 0 else 1)
ax.grid(True)
ax.legend()

vertical_line = ax.axvline(x=speeds[0], color="red", linestyle="--")
dot_front, = ax.plot([], [], "ro", label="Front Marker")
dot_rear, = ax.plot([], [], "go", label="Rear Marker")

def update(frame):
    current_speed = speeds[frame]
    current_fyf = front_axle_force[frame]
    current_fyr = rear_axle_force[frame]
    
    vertical_line.set_xdata([current_speed, current_speed])
    dot_front.set_data([current_speed], [current_fyf])
    dot_rear.set_data([current_speed], [current_fyr])
    
    return vertical_line, dot_front, dot_rear

anim = animation.FuncAnimation(
    fig, update, frames=len(speeds), interval=30, blit=True
)

plt.show()


