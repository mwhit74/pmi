import math
import matplotlib.pyplot as plt

#for a circle the coordinat system needs to be defined with respect to the
#centroid (center) of the circle

dia = 8.0

c_start = dia/2
c_end = -dia/2
num_steps = 100
c_step = abs((c_end-c_start)/num_steps)

eu = 0.003
Es = 29000000
fy = 60000
fc = 4000
Ec = 57000*math.sqrt(4000)



P = []
M = []

for x in range(num_steps):
    if x == 0:
        c = c_step
    else:
        c = c + c_step

    phi = math.log(eu/c, 10)

    es = eu*(d-c)/c
    fs = min(Es*es,fy)
    esp = eu*(c-dp)/c
    fsp = min(Es*esp,fy)
    a = 0.85*c
    A = 2*math.acos(1-a/(dia/2))
    C = 0.85*fc*A
    Pn = C-fs*As+fsp*Asp
    Mn = C*(h/2-a/2)+Asp*fsp*(h/2-dp)+As*fs*(d-h/2)

    out = ('c: {8}\na: {0}\nes: {1}\nfs: {2}\nesp: {3}\nfsp: {4}\nC: {5}\nPn:'
        '{6}\nMn: {7}'.format(a,es,fs,esp,fsp,C,Pn,Mn,c))
    #print out

    #pause = raw_input(">")

    P.append(Pn)
    M.append(Mn)
    
    
plt.plot(M,P,".")

plt.show()
    
def beta1(fc):
    return 0.85-0.05*(fc-4000)/1000

class Rebar(object):
    def __init__(self, iden, x, y, size=None, area=None):
        self.x = x
        self.y = y
        if size == None and area == None:
            raise 
        elif size == None:
            self.area = area
            self.size = get_size(self.area)
        elif area == None:
            self.size = size
            self.area = get_area(self.size)
        else:
            self.area = area
            self.size = size

class RebarLayout(object):
    def __init__(self, layout):
        self.layout = layout

    def add_rebar(rebar):
        self.layout.append(rebar)


