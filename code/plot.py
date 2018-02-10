import matplotlib
matplotlib.use('Agg')

def show():
   return matplotlib.pyplot.show(block=True)

import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot([1,2,3])
fig = ax.get_figure()
fig.savefig('myplot.png')


import numpy as np
import matplotlib.pyplot as plt


fig, (ax0) = plt.subplots(1, figsize=(14, 7))
samples = range(1,9)

# Default Color Cycle

for i in samples:
    ax0.plot([0, 10], [0, i], label=i, lw=3)

# Annotation

ax0.set_title('Default color cycle')
ax0.legend(loc='upper left')
fig = ax0.get_figure()
fig.savefig('myplot.png')
# plt.show()

# future help link: https://github.com/rasbt/matplotlib-gallery/blob/master/ipynb/lineplots.ipynb
