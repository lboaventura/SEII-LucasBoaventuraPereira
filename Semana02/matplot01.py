import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4]
y = [0, 2, 4, 6, 8]

plt.figure(figsize=(8, 5), dpi=100)

# Line 1
plt.plot(x, y, 'b^--', label='2x')

# Line 2
x2 = np.arange(0, 4.5, 0.5)
plt.plot(x2[:6], x2[:6]**2, 'r', label='X^2')
plt.plot(x2[5:], x2[5:]**2, 'r--')

# Title
plt.title('Our First Graph!', fontdict={'fontname': 'Comic Sans MS', 'fontsize': 20})

# X and Y labels
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

# X, Y axis tickmarks
plt.xticks([0, 1, 2, 3, 4, ])

# Legend
plt.legend()

# Save figure
plt.savefig('mygraph.png', dpi=300)

# Show plot
plt.show()
