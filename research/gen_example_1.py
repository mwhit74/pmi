import math
import matplotlib.pyplot as plt

def fc(ec):
    fpp_c = 
    ec0 =
    ecu = 0.003
    gamma = 1.0

    if ec <= ec0:
        return fpp_c*(2*ec/ec0-math.pow(ec,2)/math.pow(ec0,2))
    else:
        return fpp_c*(1-gamma*((ec-ec0)/(ecu-ec0)))

def fs(es):
    Es = 29000 #ksi
    fy = 60 #ksi
    return min(Es*es, fy)

def e(phi, y, yc):
    eu = 0.003
    return eu + phi*(y-yc)

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



h = 30.
b = 30.
y_prev = 0.0

Ni = []
Mxi = []

for phi in range(0,90,1):
    Ncy = 0.0
    Mxcy = 0.0
    Nsy = 0.0
    Mxsy = 0.0
    for y in range(0,h,0.1):
        ey = e(phi, y, yc)
        fcy = fc(ey)
        Ncy = Ncy + fcy*(y-y_prev)*(b)
        Mxcy = Mxcy + fcy*(y-y_prev)*(b)*((y-y_prev)/2+y_prev)
    for bar in rebar:
        ey = e(phi, y_rebar, yc)
        fsy = fs(ey)
        Nsy = Nsy + fsy*A_rebar
        Mxsy = Mxsy + fsy*A_rebar*y_rebar

    N = Ncy + Nsy
    Mx = Mxcy + Mxsy

    Ni.append(N)
    Mxi.append(Mx)
