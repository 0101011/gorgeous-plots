import numpy as np
import matplotlib.pyplot as plt

N = 5
men_means = (20, 35, 30, 35, 27)
women_means = (25, 32, 34, 20, 25)
men_std = (2, 3, 4, 1, 2)
women_std = (3, 5, 2, 3, 3)

# The x locations for the groups
ind = np.arange(N)

# Width of the bars: can also be len(x) sequence
width = 0.35

p1 = plt.bar(ind, men_means, width, yerr=menStd)
p2 = plt.bar(ind, women_means, width,
             bottom=men_means, yerr=women_std)

plt.ylabel('Scores')
plt.title('Scores by group and gender')
plt.xticks(ind, ('G1', 'G2', 'G3', 'G4', 'G5'))
plt.yticks(np.arange(0, 81, 10))
plt.legend((p1[0], p2[0]), ('Men', 'Women'))

plt.show()
