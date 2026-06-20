import numpy as np
import matplotlib.pyplot as plt

#parameters
Vrest= -60.0
R= 10.0 #Mohm
dt=0.01
tau= 10
Vth= -50.0
#voltage in neuron is measured in mv, real neurons sit below zero at rest

#time
T = 200  #total time
time = np.arange(0,200,dt)

#voltage
V= np.zeros(len(time))
V[0]=Vrest
spikes=[]


#exteral current
Iext= np.zeros(len(time))
a= int(20/dt) #just some scaling
b=int(180/dt)
Iext[a:b]=2.0

#the formula
for i in range(1,len(time)):
    dv= (-(V[i-1] - Vrest)+R*Iext[i-1])/tau
    V[i] = V[i-1] + dv*dt

    if V[i] >= Vth:
        V[i]= Vrest
        spikes.append(time[i])


# Plot
plt.subplot(3,1,1)
plt.plot(time,V)
plt.ylabel("VOLTAGE(mv)")

plt.subplot(3,1,2)
plt.plot(time,Iext)
plt.ylabel("Current")

plt.subplot(3,1,3)
for s in spikes:
    plt.axvline(s,color='red')
plt.ylabel("spikes")
plt.show()
