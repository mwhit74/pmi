import math
import matplotlib.pyplot as plt

c_start = 0.0
c_end = 20.0
num_steps = 100
c_step = (c_end-c_start)/num_steps

eu = 0.003
Es = 29000000
fy = 60000
fc = 4000
Ec = 57000*math.sqrt(4000)
h = 20
b = 12
d = 17.5
dp = 2.5
As = 2.0
Asp = 2.0

P = []
M = []

for x in range(num_steps):
    if x == 0:
        c = c_step
    else:
        c = c + c_step

    phi = math.log(eu/c, 10)

    a = 0.85*c
    es = eu*(d-c)/c
    fs = min(Es*es,fy)
    esp = eu*(c-dp)/c
    fsp = min(Es*esp,fy)
    C = 0.85*fc*a*b
    Pn = C-fs*As+fsp*Asp
    Mn = C*(h/2-a/2)+Asp*fsp*(h/2-dp)+As*fs*(d-h/2)

    out = ('c: {8}\na: {0}\nes: {1}\nfs: {2}\nesp: {3}\nfsp: {4}\nC: {5}\nPn:'
        '{6}\nMn: {7}'.format(a,es,fs,esp,fsp,C,Pn,Mn,c))
    print out

    pause = raw_input(">")

    P.append(Pn)
    M.append(Mn)
    
    
plt.plot(M,P,".")

plt.show()
    
def beta1(fc):
    return 0.85-0.05*(fc-4000)/1000

