#Create fcc lattice structure with python 3
#A.M.Pourattar | Pourattar96@ut.ac.ir | University of Tehran | April 2022



primitive_positions=[[0,0,0],[0,0.5,0.5],[0.5,0,0.5],[0.5,0.5,0]]
a=float(input("Enter lattice constant: "))
lx=int(input("Enter box length in x-direction: "))
ly=int(input("Enter box length in y-direction: "))
lz=int(input("Enter box length in z-direction: "))
lx=int(lx/2)
ly=int(ly/2)
lz=int(lz/2)
count=0
positions=list()
for i in range(-lx,lx+1,1):
    for j in range(-ly,ly+1,1):
        for k in range(-lz,lz+1,1):
            if k<0:
                for h in primitive_positions:
                    if j<ly:
                        x=h[0]*a+a*i
                        y=h[1]*a+a*j
                        z=h[2]*a+a*k
                        positions.append([x,y,z])
            else:
                for h in primitive_positions:
                    x=h[0]*a+a*i
                    y=h[1]*a+a*j
                    z=h[2]*a+a*k
                    positions.append([x,y,z])

n_of_atoms=len(positions)
print('* Lattice constant: %f \n* Number of atoms: %i '%(a,n_of_atoms))
f=open("datafile.xyz","w")

str_1=str(n_of_atoms)+'\n\n'
f.write(str_1)
for e in positions:
    f.write("Al"+'\t'+str(e[0])+'\t'+str(e[1])+'\t'+str(e[2])+'\n')
    
