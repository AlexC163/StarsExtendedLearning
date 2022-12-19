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
mass_main_sequence = [0.123, 2.02, 0.98, 1.42, 0.53, 1.93]
solar_radius_main_sequence = [0.15, 1.7, 0.0084, 1.5, 0.6, 1.5]
annotations_main_sequence = ["Proxima Centauri", "Sirius A",
                             "Sirius B", "Procyon A", "Procyon B", "Pi Andromedae A"]

# Below are the coordinates and annotations for the Supergiant stars
surface_temp_supergiant = [11000, 3200, 3300]
luminocity_supergiant = [66000, 65000, 135000]
radial_velocity_supergiant = [21.5, 20, 30]
mass_supergiant = [17.0, 15.0, 20.0]
solar_radius_supergiant = [78, 880, 1200]
annotations_supergiant = ["Rigel", "Antares", "Betelgeuse"]

# Below are the coordinates and annotations for the Red Giant stars
surface_temp_red_giant = [3600, 4700]
luminocity_red_giant = [350, 250]
radial_velocity_red_giant = [3.5, -5.24]
mass_red_giant = [1.7, 1.1]
solar_radius_red_giant = [44, 26]
annotations_red_giant = ["Aldebaran", "Arcturus"]

# Below are the coordinates and annotations for the White Dwarf stars
surface_temp_white_dwarf = [12000]
luminocity_white_dwarf = [0.013]
radial_velocity_white_dwarf = [-21]
mass_white_dwarf = [0.6]
solar_radius_white_dwarf = [0.6]
annotations_white_dwarf = ["40 Eridani B"]

# This data is no longer necessary
# annotations = ["Proxima Centauri", "Rigel", "Sirius A", "Sirius B", "Aldebaran", "Antares",
#                "Arcturus", "Betelgeuse", "Procyon A", "Procyon B", "Pi Andromedae A", "40 Eridani B"]

surface_temperatures = [surface_temp_main_sequence,
                        surface_temp_supergiant, surface_temp_red_giant, surface_temp_white_dwarf]
luminocities = [luminocity_main_sequence, luminocity_supergiant,
                luminocity_red_giant, luminocity_white_dwarf]
radial_velocities = [radial_velocity_main_sequence, radial_velocity_supergiant,
                     radial_velocity_red_giant, radial_velocity_white_dwarf]
masses = [mass_main_sequence, mass_supergiant,
          mass_red_giant, mass_white_dwarf]
solar_radii = [solar_radius_main_sequence, solar_radius_supergiant,
               solar_radius_red_giant, solar_radius_white_dwarf]
z_labels = ['Surface Temperature (°C)',
            'Luminocity (L☉)', 'Radial Velocity (km/s)', 'Mass (M☉)', 'Solar Radii (R☉)']
# Add all points to the scatter plot
ax.scatter(surface_temperatures[0], luminocities[0],
           solar_radii[0], c="r", marker="o")
ax.scatter(surface_temperatures[1], luminocities[1],
           solar_radii[1], c="b", marker="^")
ax.scatter(surface_temperatures[2], luminocities[2],
           solar_radii[2], c="g", marker="x")
ax.scatter(surface_temperatures[3], luminocities[3],
           solar_radii[3], c="y", marker="*")

# Label the sides
ax.set_xlabel(z_labels[0])
ax.set_ylabel(z_labels[1])
ax.set_zlabel(z_labels[4])

# Add annotations to all points
for x1, y1, z1, i1 in zip(surface_temperatures[0], luminocities[0],
                          solar_radii[0], range(len(surface_temp_main_sequence))):
    ax.text(x1, y1, z1, annotations_main_sequence[i1])
for x1, y1, z1, i1 in zip(surface_temperatures[1], luminocities[1],
                          solar_radii[1], range(len(surface_temp_supergiant))):
    ax.text(x1, y1, z1, annotations_supergiant[i1])
for x1, y1, z1, i1 in zip(surface_temperatures[2], luminocities[2],
                          solar_radii[2], range(len(surface_temp_red_giant))):
    ax.text(x1, y1, z1, annotations_red_giant[i1])
for x1, y1, z1, i1 in zip(surface_temperatures[3], luminocities[3],
                          solar_radii[3], range(len(surface_temp_white_dwarf))):
    ax.text(x1, y1, z1, annotations_white_dwarf[i1])

# Display the graph
plt.show()
