import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle

flag_length = 3; flag_height = 2
band_height = flag_height / 3

SAFFRON = "#FF671F"; WHITE = "#FFFFFF"; GREEN = "#046A38"; NAVY_BLUE = "#06038D"

fig, ax = plt.subplots(figsize=(12, 8))

ax.add_patch(Rectangle((0, 4/3), flag_length, band_height, facecolor=SAFFRON, edgecolor="none"))
ax.add_patch(Rectangle((0, 2/3), flag_length, band_height, facecolor=WHITE, edgecolor="none"))
ax.add_patch(Rectangle((0, 0), flag_length, band_height, facecolor=GREEN, edgecolor="none"))

center_x = flag_length / 2; center_y = flag_height / 2

chakra_diameter = band_height * 0.75; chakra_radius = chakra_diameter / 2
ax.add_patch(Circle((center_x, center_y), chakra_radius, fill=False, edgecolor=NAVY_BLUE, linewidth=3))

inner_radius = chakra_radius * 0.12
ax.add_patch(Circle((center_x, center_y), inner_radius, fill=False, edgecolor=NAVY_BLUE, linewidth=2))

for i in range(24):
    angle = 2 * np.pi * i / 24

    x1 = center_x + inner_radius * np.cos(angle)
    y1 = center_y + inner_radius * np.sin(angle)
    x2 = center_x + chakra_radius * np.cos(angle)
    y2 = center_y + chakra_radius * np.sin(angle)
    ax.plot([x1, x2], [y1, y2], color=NAVY_BLUE, linewidth=1.5)

ax.set_xlim(0, flag_length); ax.set_ylim(0, flag_height)
ax.set_aspect("equal"); ax.axis("on")

plt.tight_layout(); plt.show()