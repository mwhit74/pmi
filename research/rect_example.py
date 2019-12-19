import math
import matplotlib.pyplot as plt

c_start = 0.0
c_end = 30.0
num_steps = 100
c_step = (c_end-c_start)/num_steps

eu = 0.003
Es = 29000000
fy = 60000
fc = 3000
Ec = 57000*math.sqrt(3000)
h = 30.
b = 30.
d1 = 26.865
d2 = 3.135
d3 = 15.
As1 = 3.*1.27
As2 = 3.*1.27
As3 = 2.*1.27

P = []
M = []

for x in range(num_steps):
    if x == 0:
        c = c_step
    else:
        c = c + c_step

    phi = math.log(eu/c, 10)

    a = 0.85*c
    es1 = eu*(d1-c)/c
    fs1 = min(Es*es1,fy)
    es2 = eu*(c-d2)/c
    fs2 = min(Es*es2,fy)
    es3 = eu*(c-d3)/c
    fs3 = min(Es*es3, fy)
    C = 0.85*fc*a*b
    Pn = C-fs1*As1+fs2*As2+fs3*As3
    Mn = C*(h/2-a/2)+As2*fs2*(h/2-d2)+As1*fs1*(d1-h/2)+As3*fs3*(d3-h/2)
    
    if Mn >= 0.0:
        out = ('c: {8}\na: {0}\nes: {1}\nfs: {2}\nesp: {3}\nfsp: {4}\nC: {5}\nPn:'
        '{6}\nMn: {7}'.format(a,es1,fs1,es2,fs2,es3,fs3,C,Pn,Mn,c))

        Pn = Pn/1000.0
        Mn = Mn/1000.0/12.0

        #print(Pn, ",", Mn)
        P.append(Pn)
        M.append(Mn)
    
plt.plot(M,P,".")

plt.show()
    
def beta1(fc):
    return 0.85-0.05*(fc-4000)/1000

