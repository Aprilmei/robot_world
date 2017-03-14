from world2.world import *

import matplotlib.pyplot as plt
import numpy as np

my_world=created_world('world1.dat')
matrix=np.matrix(my_world)

fig = plt.figure(figsize=(6, 3.2))

ax = fig.add_subplot(111)
ax.set_title('Robot_world')
plt.imshow(matrix)
ax.set_aspect('equal')

plt.colorbar()
plt.show()
