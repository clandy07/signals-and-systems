import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 4 * np.pi, 1000)
y = np.zeros_like(t)

num_harmonics = 100

for i in range(num_harmonics):
    k = 2 * i + 1 # k = 1, 3, ,5...
    y += (-4 / (k * np.pi)**2) * np.cos(k * t)

plt.plot(t, y)
plt.title(f'Triangle Wave Synthesis ({num_harmonics} terms)')

plt.show()
