# Initialize librarys
from scipy.special import erfc, erf
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import math
import streamlit as st

st.title('Reservoir head - Introductionary Example to Model Calibration -  (based on materials from John Doherty)')

st.write('The example is taken from a tutorial by John Doherty (author of the software PEST). A catchment area is described by a lumped-parameter model (i.e., the entire area is described with a few effective parameters).')

st.write('The interactive document addresses the following **learning objectives**: *After successfully completing the worksheet, you will be able to*:')
st.write('+ explain the functionality of a simple conceptual model,')
st.write('+ calibrate a simple model,')
st.write('+ explain the significance and consequences of parameter correlation in a model,')
st.write('+ understand how to effectively calibrate a model with correlated parameters.')

st.subheader('Model Concept')
st.write('A reservoir is defined by a storage *S*. An inflow of water is generated by recharge *R*. The outflow *q* depends on the conductance *C* (also known as the conductance or hydraulic resistance) and the water level *h*.')

st.subheader('Mathematical Model')

st.write('The following equations describe the behavior of the catchment area. The outflow *q* results from the conductance *C* and the water level *h*.')
st.write('**Outflow *q*** ')
st.latex(r'''\large q = Kh''')
st.write('The higher the water level, the more water flows out of the reservoir.')
st.write('**Flow Equation with Continuity / Mass Conservation**')
st.write('The flow equation is derived from the combination of outflow and mass conservation (continuity):')
st.latex(r'''\large S\frac{\partial h}{\partial t}=R-Kh''')
st.write('with ')
st.write('*S* = storage and  ')
st.write('*R* = recharge.  ')
st.write('**Initial Condition**')
st.write('To solve the equation, an initial condition is necessary: ')
st.latex(r'''\large h(t=0) = h_i''')
st.write('with')
st.write('*hi* = initial water level.')

st.subheader('Solution and Graphical Representation')
st.write('The flow equation can be solved as follows, describing the water level *h* as a function of time *t*: ')
st.latex(r'''\large h(t) = h_i+(\frac{R}{K}-h_i)(1-e^{\frac{-Kt}{S}})''')
st.write('The equation will be solved in the following section.')

"---"
#Computation

log_min1 = -5.0 # T / Corresponds to 10^-7 = 0.0000001
log_max1 = 3.0  # T / Corresponds to 10^0 = 1

log_min2 = -5.0 # S / Corresponds to 10^-7 = 0.0000001
log_max2 = 3.0  # S / Corresponds to 10^0 = 1

log_min3 = -5.0 # S / Corresponds to 10^-7 = 0.0000001
log_max3 = 3.0  # S / Corresponds to 10^0 = 1

columns = st.columns((1,1), gap = 'large')

with columns[0]:
    h_i = st.slider(f'**Initial head**', 10,150,0,1)
    R_slider_value=st.slider('(log of) Recharge', log_min3,log_max3,-1.0,0.01,format="%4.2f" )
    # Convert the slider value to the logarithmic scale
    R = 10 ** R_slider_value
    # Display the logarithmic value
    st.write("**Recharge:** %5.2e" %R)


with columns[1]:
    K_slider_value=st.slider('(log of) Conductivity', log_min1,log_max1,-2.0,0.01,format="%4.2f" )
    # Convert the slider value to the logarithmic scale
    K = 10 ** K_slider_value
    # Display the logarithmic value
    st.write("**Conductivity:** %5.2e" %K)
    S_slider_value=st.slider('(log of) Storage', log_min2,log_max2,-3.0,0.01,format="%4.2f" )
    # Convert the slider value to the logarithmic scale
    S = 10 ** S_slider_value
    # Display the logarithmic value
    st.write("**Storage:** %5.2e" %S)


    


# Measured data
t_meas = [0.1, 0.2, 0.5, 1, 2, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]
h_meas = [0.0499875, 0.0999500, 0.2496878, 0.4987521, 0.9950166, 2.4690090, 4.8770580, 9.5162580, 22.1199200, 39.3469400, 63.2120600, 91.7915000, 99.3262000, 99.9954600, 100.0000000, 100.0000000]

t_max = 10000
t = np.arange(0, t_max, t_max/100)
h=h_i+(R/K-h_i)*(1-math.e**(-K*t/S))
    
# PLOT FIGURE
fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(1, 1, 1)
ax.plot(t,h, linewidth=2, label='Computed')
ax.plot(t_meas, h_meas, 'ro', label='Measured')
plt.xlim(-1000,t_max*1.05)
plt.ylim(0,150)
plt.xlabel('t',fontsize=14)
plt.ylabel('head',fontsize=14)
plt.title('Hydraulic head in the reservoir', fontsize=16)
plt.legend(fontsize=14)

st.pyplot(fig)