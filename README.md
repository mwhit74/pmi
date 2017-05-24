I have been fumbling around this for a while now, say a couple of years off and
on. I have played with different ideas and approaches. Read some stuff, read
some other stuff, re-read the original stuff. Talked with people about how it
works. Doodled endlessly and wrote pages of notes. All to discover that it was
right in front of me the whole time and it really is fairly straight forward. 

P-M interaction diagrams determine the capacity envelope of a reinforced concrete
member with a combination of axial force and moment applied at a section of the
member. 

The maximum usable concrete strain is given from experimentation as 0.003. Then
it is a matter of iterating over a range of curvature values or neutral
axis locations, either one works because they are related by a single equation.
The strain in the steel is determined based on distance from the neutral axis.
The stress in the steel is then calculated based on the strain in the steel and
modulus of elasticity. Alternatively, a value directly from the stress-strain
diagram could be use. Also depending on the material model it could be
elastic-perfectly plastic or a more exact model. Finally, the forces and moments
on the cross-section are summed. For each iteration a corresponding P-M pair are
added to the array. 

The one thing I am still unsure about is how a cracked section analysis plays
into the development of P-M interaction diagrams. The answer to this is that the
cracked section is taken care of by the stress-strain diagram of the concrete.
Instead of using a Whitney stress block one can find the actual strain at
discrete points, calculate the stress based on the strain and the stress-strain
diagram, multiply the stress by the assumed area the discrete point represents
to get a force for use in the force and moment equilibrium. 
