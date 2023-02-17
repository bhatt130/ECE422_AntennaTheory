import matplotlib.pyplot as plt
import numpy as np

# Define the data points
degrees = np.array([0, 15, 30, 45, 60, 75, 90, 105, 120, 135, 150, 165, 180, 195, 210, 225, 240, 255, 270, 285, 300, 315, 330, 345, 360])
dB = np.array([-35.452,-36.904,-37.604,-38.901,-42.780,-43.440,-43.899,-47.320,-50.097,-53.740,-44.510,-42.672,-43.973,-45.327,-44.447,-46.110,-50.547,-52.147,-42.203,-39.220,-39.423,-38.330,-36.344,-32.257,-39.907])
# Convert degrees to radians
theta = degrees * np.pi / 180

# Set up the polar plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='polar')
ax.set_theta_offset(np.pi/2)
ax.set_theta_direction(-1)

# Plot the data points
ax.scatter(theta, dB, s=20, c='b')

# Set the title and labels
ax.set_title("H Plane Polar Scatter Plot")
ax.set_rlabel_position(180)
ax.set_ylabel("dB")
ax.set_xlabel("Angle (degrees)")

# Set the y-axis limits
ax.set_ylim(bottom=-60, top=-40)

# Show the plot
plt.show()
