import matplotlib.pyplot as plt
import math

x = [i for i in range(1,100)]
y = [math.log(0.1/x[i],10) for i in range(len(x))]

plt.plot(x,y,".")

plt.show()