import matplotlib.pyplot as plt
from matplotlib import animation

#write code here, then call traction_limit function (template below)

def traction_limits(speeds, front_forces, rear_forces, max_front_force, max_rear_force):
   
    fig, ax = plt.subplots(figsize=(9, 6))

    ax.plot(speeds, front_forces, label="Front Demand ($F_{yf}$)", color="blue")
    ax.plot(speeds, rear_forces, label="Rear Demand ($F_{yr}$)", color="orange")

    ax.axhline(y=max_front_force, color="blue", linestyle="--", alpha=0.7, label=f"Front Max ({max_front_force:.1f} N)")
    ax.axhline(y=max_rear_force, color="orange", linestyle="--", alpha=0.7, label=f"Rear Max ({max_rear_force:.1f} N)")

    ax.set_title("Lateral Force Demand vs. Available Friction Capacity")
    ax.set_xlabel("Speed (m/s)")
    ax.set_ylabel("Lateral Force (N)")
    ax.set_xlim(min(speeds), max(speeds))
    
    y_max = max(max(front_forces), max(rear_forces), max_front_force, max_rear_force) * 1.15
    ax.set_ylim(0, y_max)
    ax.grid(True)
    ax.legend(loc="upper left")

    vertical_line = ax.axvline(x=speeds[0], color="gray", linestyle=":")
    dot_front, = ax.plot([], [], "o", color="green", markersize=8)
    dot_rear, = ax.plot([], [], "o", color="green", markersize=8)
    status_text = ax.text(0.5, 0.85, "", transform=ax.transAxes, fontsize=11, fontweight="bold",
                          bbox=dict(boxstyle="round,pad=0.5", facecolor="white", alpha=0.8))

    def update(frame):
        current_speed = speeds[frame]
        current_fyf = front_forces[frame]
        current_fyr = rear_forces[frame]
        
        vertical_line.set_xdata([current_speed, current_speed])
        dot_front.set_data([current_speed], [current_fyf])
        dot_rear.set_data([current_speed], [current_fyr])
        
        front_exceeded = current_fyf > max_front_force
        rear_exceeded = current_fyr > max_rear_force
        
        if front_exceeded and rear_exceeded:
            dot_front.set_color("red")
            dot_rear.set_color("red")
            status_text.set_text(f"CRITICAL: Both Limits Exceeded at {current_speed:.1f} m/s!")
            status_text.set_color("darkred")
        elif front_exceeded:
            dot_front.set_color("red")
            dot_rear.set_color("green")
            status_text.set_text(f"WARNING: Front Axle Traction Limit Exceeded at {current_speed:.1f} m/s")
            status_text.set_color("crimson")
        elif rear_exceeded:
            dot_front.set_color("green")
            dot_rear.set_color("red")
            status_text.set_text(f"WARNING: Rear Axle Traction Limit Exceeded at {current_speed:.1f} m/s")
            status_text.set_color("crimson")
        else:
            dot_front.set_color("green")
            dot_rear.set_color("green")
            status_text.set_text(f"Normal Operation: Speed {current_speed:.1f} m/s (Traction OK)")
            status_text.set_color("darkgreen")
            
        return vertical_line, dot_front, dot_rear, status_text

    global anim 
    anim = animation.FuncAnimation(fig, update, frames=len(speeds), interval=30, blit=True)
    plt.show()

'''traction_limits(
    speeds= # Your list of speed values 
    front_forces= # Your list of calculated front axle forces 
    rear_forces= # Your list of calculated rear axle forces 
    max_front_force= # Result from your available_front_force method 
    max_rear_force= # Result from your available_rear_force method 
)'''