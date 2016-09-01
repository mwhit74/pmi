import math
import matplotlib.pyplot as plt

c_start = 0.0
c_end = 20.0
num_steps = 100
c_step = (c_end-c_start)/num_steps

c = []
phi = []

for x in range(num_steps):
    if x == 0:
        c.append(c_step)
    else:
        c.append((c[x-1] + c_step))
    phi.append(math.log(0.003/c[x],10))
    
plt.plot(c,phi,".")

plt.show()
    

    
    