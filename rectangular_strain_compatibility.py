
import math
import matplotlib.pyplot as plt

#input
f_c = 4000
Ec = 57000*math.sqrt(f_c)

b = 12
h = 20.0

fy = 60
Es = 29000

As = [2.0,2.0]
ys = [2.5,17.5]

#fiber mesh construction
num_elements = 30
#num_elements_x = 30

dy = h/num_elements

#strain limits
ecu = 0.003
ey = 0.005

#initialize variables
pm = []

#curvature limits
psy_start = ecu/0.01
psy_end = 0.0
num_step = 10000
psy_step = (psy_start - psy_end)/num_step

psy = psy_start

c = []
psy = []

#iteration
for x in range(num_step):
    if x == 0:
        psy.append(psy_start)
    else:
        psy.append(psy[x-1] - psy_step)
    c.append(math.log(ecu/(psy[x]),10))    #neutral axis
    
plt.plot(c,psy,".")
plt.show()

'''    
    #initialize variables
    dyc = []
    yc = [0.0]
    ec = []
    fc = []
    Pc = []
    Mc = []
    Pct = 0.0
    Mct = 0.0

    es = []
    fs = []
    Ps = []
    Ms = []
    Pst = 0.0
    Mst = 0.0
    
    #concrete
    for m in range(0,num_elements):
        #print "m: " + str(m)
        #strain on each element
        dyc.append(dy)
        if m > 0:
            yc.append(yc[m-1] + dy/2)
        #print "yc: " + str(yc[m])
        ec.append((c-yc[m])*math.tan(phi*180/math.pi))
        #print "ec: " + str(ec[m])
        
        #concrete material model
        if ec[m] > 0 and ec[m] < ecu: #compressive strain (+), concrete can't support tension
            fc.append(ec[m]*Ec)
        elif ec[m] >= 0.003:
            fc.append(0.85*f_c)
        elif ec[m] < 0: 
            fc.append(0.0)
            
        #axial force
        #print "fc: " + str(fc[m])
        #print "dyc: " + str(dyc[m])
        #print "b: " + str(b)
        #print "\n"
        Pc.append(fc[m]*dyc[m]*b)
        Pct = Pc[m] + Pct
        
        #moment        
        Mc.append(Pc[m]*(c-yc[m]))
        Mct = Mc[m] + Mct
        
    raw_input(">")
    
    #steel
    for n in range(0,len(As)):
        #stain on each element
        es.append((c-ys[n])*math.tan(phi*180/math.pi))
        
        #steel material model
        if abs(es[n]) < ey:
            fs.append(es[n]*Es)
        else:
            fs.append(fy)
        
        #axial force
        Ps.append(fs[n]*As[n])
        Pst = Ps[n] + Pst
        
        #moment
        Ms.append(Ps[n]*(c-ys[n]))
        Mst = Ms[n] + Mst
        
    Pt = Pct + Pst
    Mt = Mct + Mst
        
    pm.append([Pt, Mt])
    
for g in pm:
	print str(g[0]) + "    " + str(g[1])
'''