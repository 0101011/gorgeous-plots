''' In this quick and sweet example you will find out about matplotlib basic functions
to create a sample plot which shows your curiosity in learning matplotlib.
Read along and have fun!''' 

import matplotlib
import matplotlib.pyplot as plt # A rich collection of command style functions
import numpy as np

# Insert some data to play with below using Numpy
t = np.arange(0.0, 2.0, 0.01)

# Trigonometric sine
s = 1 + np.sin(6 * np.pi * t)

fix, ax = plt.subplots()

# Make sure you plot the data indicated
ax.plot(t, s)

# Add some labels for x and y axes
ax.set(xlabel='time (s)', ylabel='interest (points)',
	title='Your interest in Matplotlib ')

# Add a marvelous grid
ax.grid()

# This functions show everything you've added so far in your plot. Enjoy the curvies!
plt.show()