import matplotlib
matplotlib.use("agg")

import matplotlib.pyplot as plt
import numpy as np


# Create the curve data.
x = np.linspace(-6, 6, 500)
y = np.sinc(x)

# Vary the line width.
fig = plt.figure()
ax = fig.gca()
ax.plot(x, y, linewidth=15)
fig.savefig("images/wide_line.png")

# Vary the line color.
fig = plt.figure()
ax = fig.gca()
ax.plot(x, y, color="pink", linewidth=5)
fig.savefig("images/pink_line.png")

# Vary the line style.
fig = plt.figure()
ax = fig.gca()
ax.plot(x, y, linewidth=2, linestyle="--")
fig.savefig("images/dashed_line.png")

# Make multiple lines.
fig = plt.figure()
ax = fig.gca()
ax.plot(x, y, linewidth=4)
ax.plot(x, y + .1, linewidth=2)
ax.plot(x, y + .2, linewidth=1)
ax.plot(x, y + .3, linewidth=.5)
ax.plot(x, y + .4, linewidth=.2)
fig.savefig("images/multiple_lines.png")
