# pip install matplotlib 
# python pentagono.py

import numpy as np
import matplotlib.pylab as plt
import matplotlib.animation as anim

r1, r2, r3 = 4, 4, 1.3
w1, w2, w3 = 44, -17, -54
p1, p2, p3 = 0, 0, 0

def initFigureWindow():
    fig, ax = plt.subplots(figsize=(5,5))
    fig.canvas.manager.set_window_title('Spirograph Animation')
    fig.patch.set_facecolor('black')
    ax.set_facecolor('black')
    ax.axis([-10, 10, -10, 10])
    return fig, ax

def initLine(ax):
    return ax.plot([], [], color='white')[0]

def spiroanimation(frame, trace, z):
    trace.set_data(np.real(z[:frame]), np.imag(z[:frame]))
    return trace,

fig, ax = initFigureWindow()
trace = initLine(ax)
theta = np.linspace(0, 2 * np.pi, 1000)

z = (r1 * np.exp(1j * (theta * w1 + p1)) +
     r2 * np.exp(1j * (theta * w2 + p2)) +
     r3 * np.exp(1j * (theta * w3 + p3)) )

myanimation = anim.FuncAnimation(fig, spiroanimation, frames=1000, interval=0.1, fargs=(trace, z))

plt.show()
