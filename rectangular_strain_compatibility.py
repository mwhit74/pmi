
import math

#input
fc = 4000
Ec = 57000*math.sqrt(fc)

b = 12
h = 20

fy = 60
Es = 29000

As = [2.0,2.0]
ys = [2.5,17.5]

#fiber mesh construction
num_elements_y = 30
#num_elements_x = 30

dy = h/num_elements

#strain limits
ecu = 0.003
ey = 0.005

#iteration
for phi in range(1,90):
    c = ecu/math.tan(phi) #neutral axis
	for m in range(1,num_elements):
		#strain field
		dyc[m] = dy
		yc[m] = yc[m-1] + dy/2
		ec[m] = (c-yc[m])*math.tan(phi)
		
		#concrete material model
		if ec[m] > 0: #compressive strain (+), concrete can't support tension
			fc[m] = ec[m]*Ec
			
		#axial force
		Pc[m] = fc[m]*dyc[m]*b
		Pct = Pc[m] + Pct
		
		#moment		
		Mc[m] = Pc[m]*(c-yc[m])
		Mct = Mc[m] + Mct
		
	for n in range(1,num_rows):
		es[n] = (c-ys[n])*math.tan(phi)
		
		
