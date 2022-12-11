import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
# This data is no longer necessary
# surface_temp = [3100, 11000, 9500, 25000,
#                 3600, 3200, 4700, 3300, 6200, 7500, 16000, 12000]
# luminocity = [0.0017, 66000, 25.4,
#               0.026, 350, 65000, 250, 135000, 8, 0.0005, 800, 0.013]
# radial_velocity = [22.2, 21.5, 16, 16, 54, 20, -5.24, 30, -3.2, -3.2, 8.2, -21]

# Below are the coordinates and annotations for the Main-Sequence stars
surface_temp_main_sequence = [3100, 9500, 25000, 6200, 7500, 16000]
luminocity_main_sequence = [0.0017, 25.4, 0.026, 8, 0.0005, 800]
radial_velocity_main_sequence = [22.2, 16, 16, -3.2, -3.2, 8.2]
annotations_main_sequence = ["Proxima Centauri", "Sirius A",
                             "Sirius B", "Procyon A", "Procyon B", "Pi Andromedae A"]

# Below are the coordinates and annotations for the Supergiant stars
surface_temp_supergiant = [11000, 3200, 3300]
luminocity_supergiant = [66000, 65000, 135000]
radial_velocity_supergiant = [21.5, 20, 30]
annotations_supergiant = ["Rigel", "Antares", "Betelgeuse"]

# Below are the coordinates and annotations for the Red Giant stars
surface_temp_red_giant = [3600, 4700]
luminocity_red_giant = [350, 250]
radial_velocity_red_giant = [54, -5.24]
annotations_red_giant = ["Aldebaran", "Arcturus"]

# Below are the coordinates and annotations for the White Dwarf stars
surface_temp_white_dwarf = [12000]
luminocity_white_dwarf = [0.013]
radial_velocity_white_dwarf = [-21]
annotations_white_dwarf = ["40 Eridani B"]

# This data is no longer necessary
# annotations = ["Proxima Centauri", "Rigel", "Sirius A", "Sirius B", "Aldebaran", "Antares",
#                "Arcturus", "Betelgeuse", "Procyon A", "Procyon B", "Pi Andromedae A", "40 Eridani B"]


# Add all points to the scatter plot
ax.scatter(surface_temp_main_sequence, luminocity_main_sequence,
           radial_velocity_main_sequence, c="r", marker="o")
ax.scatter(surface_temp_supergiant, luminocity_supergiant,
           radial_velocity_supergiant, c="b", marker="^")
ax.scatter(surface_temp_red_giant, luminocity_red_giant,
           radial_velocity_red_giant, c="g", marker="x")
ax.scatter(surface_temp_white_dwarf, luminocity_white_dwarf,
           radial_velocity_white_dwarf, c="y", marker="*")

# Label the sides
ax.set_xlabel('Surface Temperature (°C)')
ax.set_ylabel('Luminocity (L☉)')
ax.set_zlabel('Radial Velocity (km/s)')

# Add annotations to all points
for x1, y1, z1, i1 in zip(surface_temp_main_sequence, luminocity_main_sequence, radial_velocity_main_sequence, range(len(surface_temp_main_sequence))):
    ax.text(x1, y1, z1, annotations_main_sequence[i1])
for x1, y1, z1, i1 in zip(surface_temp_supergiant, luminocity_supergiant, radial_velocity_supergiant, range(len(surface_temp_supergiant))):
    ax.text(x1, y1, z1, annotations_supergiant[i1])
for x1, y1, z1, i1 in zip(surface_temp_red_giant, luminocity_red_giant, radial_velocity_red_giant, range(len(surface_temp_red_giant))):
    ax.text(x1, y1, z1, annotations_red_giant[i1])
for x1, y1, z1, i1 in zip(surface_temp_white_dwarf, luminocity_white_dwarf, radial_velocity_white_dwarf, range(len(surface_temp_white_dwarf))):
    ax.text(x1, y1, z1, annotations_white_dwarf[i1])

# Display the graph
plt.show()
