
# coding: utf-8

# # Phase and Group Velocity and Dispersive and Non-Dispersive Waves
# ## Leslie Orozco, Phiona Vall, Ryan Williams
# 

# The group velocity is the speed of the envelope. Group velocity is defined by the equation: 
# \begin{align}
# v=\frac{dω(k)}{dk}
# \end{align}
# Where ω is the wave's angular frequency, and k is the angular wavenumber (magnitude of the wave vector). For waves:
# 
# \begin{align}
# k = \frac{2\pi}{\lambda} = \frac{2\pi\nu}{v_p} = \frac{w}{v_p} 
# \end{align}
# 
# For a non-dispersive sound wave traveling in air: the phase velocity is a constant and is the famous speed of sound, 343 m/s
# 
# 
# The function ω(k) is known as the dispersion relationship. The dispersion relationship relates the wavelength of the wave to its frequency. 
# 
# The Phase velocity of a wave is the rate at which the phase of the wave propagates in space, the speed of the individual ripples. 
# Phase velocity is given in terms of wavelength or λ and time period T. The ratio between the speed of light c and the phase velocity v_p is known on the refraction index as:
# \begin{align}
# n = \frac{c}{v_p} = \frac{ck}{w}
# \end{align}
# 

# In[8]:


import numpy as np
import matplotlib.pyplot as plt 
import sympy as sym
sym.init_printing()
w = sym.Symbol('w')
k = sym.Symbol('k')
r = range(20)
w = [343*q for q in r]
plt.figure(figsize = (10,5))
plt.plot(r,w, color = 'red')
plt.xlabel('k (Wave Number)')
plt.ylabel('w (Angular Frequency)')
plt.title('Wave Number versus Frequency for a non-dispersive air wave traveling in air')
plt.grid()
plt.show()


# In[9]:


#calculating the derivative with respect to the wave number of the angular frequncy 
w = 343*k
sym.diff(w,k)


# \begin{align}
# V_g = \frac{dw}{dk} \\
# \end{align}
# For a non-dispersive sound wave traveling through air:
# \begin{align}
# V_g = 343 m/s \\
# \end{align}

# In[10]:


dw = [343 for q in r]
plt.figure(figsize = (10,5))
plt.plot(r,dw, color = 'blue')
plt.xlabel('k (Wave Number)')
plt.ylabel('Vg (Group Velocity)')
plt.title('Group Velocity versus Wave Number for a non-dispersive sound wave traveling in air')
plt.grid()
plt.show()


# In[ ]:


import numpy 

import matplotlib.pyplot as plot

import matplotlib.animation as animation

from IPython.display import HTML

figure=plot.figure()

plot.xlim(0, 2*numpy.pi),plot.ylim(-4,4)

line,=plot.plot([])


def animate(i):

x=numpy.arange(0, 2*numpy.pi, 0.001)

y=numpy.sin(10*2*numpy.pi*(x-0.0005*i))+numpy.sin(9*2*numpy.pi*(x-0.0001*i))

'''y=sin(10*2*pi*x)+sin(9*2*pi*x), with different speed'''

line.set_data(x,y)

return line,


wave= animation.FuncAnimation(figure, animate, frames=1000, interval=10, blit=True)


HTML(wave.to_html5_video)

