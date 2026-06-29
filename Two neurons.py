#With gaussian noise
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
#voltage for N2
V2= np.zeros(len(time))
V2[0]= Vrest
spikes2=[]

#exteral current
Iext= np.zeros(len(time))
a= int(20/dt) #just some scaling
b=int(180/dt)
#noise strength = 0.5 say
Iext[a:b]=2.0 + 0.5*np.random.randn(b-a)

#for neuron 2 (defining the current as I_syn)
I_syn=np.zeros(len(time))
g_syn=15.0  #strength of I_syn
tau_syn= 5.0  #time of decay of each signal to neuron 2
#the formula
refractory_counter= 0
refractory_counter2= 0
#steps for the counter 2/0.01=200 steps
for i in range(1,len(time)):
    I_syn[i]=I_syn[i-1] + (-I_syn[i-1]/tau_syn) *dt
    if refractory_counter>0:
        V[i]= Vrest
        refractory_counter-=1
    else:
        dv= (-(V[i-1] - Vrest)+R*Iext[i-1])/tau
        V[i] = V[i-1] + dv*dt

        if V[i] >= Vth:
            V[i]= Vrest


            I_syn[i]+= g_syn

            spikes.append(time[i])
            refractory_counter=200


#neuron 2
    if refractory_counter2>0:
        V2[i]= Vrest
        refractory_counter2-=1
    else:
        dv2= (-(V2[i-1] - Vrest)+R*(I_syn[i-1])/tau)
        V2[i] = V2[i-1] + dv2*dt
        if V2[i] >= Vth:
            V2[i]= Vrest
            spikes2.append(time[i])
            refractory_counter2=200





# Plot
plt.subplot(3,1,1)
plt.plot(time,V)
plt.plot(time,V2)
plt.ylabel("VOLTAGE(mv)")

plt.subplot(3,1,2)
plt.plot(time,Iext)
plt.plot(time,I_syn)
plt.ylabel("Current")

plt.subplot(3,1,3)
for s in spikes:
    plt.axvline(s,color='red')
for s2 in spikes2:
    plt.axvline(s2, color='yellow')
plt.ylabel("spikes")

plt.show()
