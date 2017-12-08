# Team Members: YOUR NAMES HERE

import numpy as np

# Your M/K ratio that achieves at least 95% probability of successful recovery.
RATIO = 1.500

def strategy(active_colors, d, ratio):
	"""Your strategy function for specifying where to throw the d balls of each active color.

	Arguments:
		active_colors: an array of indices of 'active' colors.
		d: the number of balls for each color.
		ratio: the M/K ratio to determine how many bins to use.

	Returns:
		You should return a dictionary, where the keys are the indices of the 'active' colors, and
		the values are M-dimensional numpy arrays of 0's and 1's, with the 1's indicating the bins
		that contain balls of this color.
	"""
    M = int(len(active_colors) * ratio)
    dist = {}
    for color in active_colors:
        bins = np.random.choice(np.arange(M), d, replace=False)
        color_dist = np.zeros(M)
        color_dist[bins] = 1
        dist[color] = color_dist
    return dist
