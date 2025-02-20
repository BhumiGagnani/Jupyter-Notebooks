# Loading the required Python libraries
import numpy as np
import matplotlib.pyplot as plt
import scipy.special
import streamlit as st
import streamlit_book as stb
from streamlit_extras.stylable_container import stylable_container
from streamlit_extras.stateful_button import button
from streamlit_extras.stodo import to_do


st.title('Transient Flow toward a well in a confined aquifer is described by the Theis Solution')

st.subheader(':blue-background[Conceptualizing the response of a confined aquifer to pumping]', divider="blue")

st.markdown('''
            ### To start your investigation of the topic it is useful to think about the system using this initial assessment ...
                       '''
)
# Initial assessment
   
with st.expander(":green[**Show/Hide the initial assessment**]"):
    columnsQ1 = st.columns((1,1))
    
    with columnsQ1[0]:
        stb.single_choice(":blue[**What conditions are applicable for use of the Theis equaiton?**]",
                  ["Steady state flow, confined aquifer", "Transient flow, confined aquifer", "Steady state flow, unconfined aquifer",
                  "Transient flow, unconfined aquifer"],
                  1,success='CORRECT! The Theis Solution describes transeint flow to a well in a confined aquifer.', error='This is not correct ... You can learn more about the Theis Solution [by downloading An Introduction to Hydraulic Testing in Hydrogeology - Basic Pumping, Slug, and Packer Methods​​ and reading Section 8](https://gw-project.org/books/an-introduction-to-hydraulic-testing-in-hydrogeology-basic-pumping-slug-and-packer-methods/). Feel free to answer again.')
        stb.single_choice(":blue[**If there is no recharge to an aquifer how does the cone of depression behave with ongoing time?**]",
                  ["The cone of depression will reach a steady state", "The cone of depression continue to increase", "The cone of depression is not dependent on time", "The cone of depression will decrease"],
                  1,success='CORRECT! Without recharge, the cone of depression will increase.', error='This is not correct ... Without recharge, the cone of depression will increase with ongoing time. You can explore this by using the interactive tool to investigate this behavior. Feel free to answer again.') 
    with columnsQ1[1]:
        stb.single_choice(":blue[**How does storativity (_S_) influence the response of an aquifer to pumping?**]",
                  ["A higher storativity results in a slower drawdown response", "A higher storativity leads to more rapid flow to the well", "Storativity only affects steady-state conditions", "Storativity is not relevant for confined aquifers"],
                  0,success='CORRECT! A higher storativity results in a slower drawdown response', error='This is not correct ... You can use the interactive tool to explore this and learn more about Storativity [by downloading Basic Hydrogeology - An Introduction to the Fundamentals of Groundwater Science​ and reading Section 5.3](https://gw-project.org/books/basic-hydrogeology/). Feel free to answer again.')  
        stb.single_choice(":blue[**Which of the following statements describes the drawdown at a point due to pumping in a confined aquifer?**]",
                  ["It decreases with time", "It increases with time", "It remains constant over time", "It is independent of the pumping rate"],
                  1,success='CORRECT! Drawdown continues to increase with time as pumping continues', error='This is not correct ...  You can use the interactive tool to explore this. Feel free to answer again.')

# Create ToDos to proceed with the steps of the exercise

with st.expander(":blue[**Proceed with Exercise Step 1**] - See here for instructions"):
    st.markdown("""
            **STEP 1:**
            First we investigate drawdown around a pumping well in response to water abstraction as function of space and time.
            
           _To proceed,_ use the interactive plot below and observe the response to the following actions:
           """)
    to_do(
        [(st.write, "Increase the pumping rate. What happens with the drawdown? Adjust the slider 'Print drawdown at _r_ (m)' (middle column) to print specific values below the graph.")],"td01",)
    to_do(
        [(st.write, "Now use the toggle on the left side to 'Show drawdown vs time plot'. Modify the 'Distance to show (m)' and see how the drawdown vs time changes depending of the distance from the abstraction well.")], "td02",)


with st.expander(":blue[**Proceed with Exercise Step 2**] - See here for instructions"):
    st.markdown("""
            **STEP 2:**
            Now we investigate the sensitivity of the hydraulic conductivity _K_ and the storativity _S_ on the drawdown in response to a specific abstraction rate.
            
           _To proceed_ (with the interactive plot):
           """)
    to_do(
        [(st.write, "Modify the Transmissivity. What happens?")],"td03",)
    to_do(
        [(st.write, "Modify the Storativity. What happens?")], "td04",)

with st.expander(":blue[**Proceed with Exercise Step 3**] - See here for instructions"):
    st.markdown("""
            **STEP 3:**
            Now you can use the interactive plot to compare two variants with different transmissivity and storativity. 
            
           _To proceed_ (with the interactive plot):
           """)
    to_do(
        [(st.write, "Use the toggle 'Compute a second variant for comparison'.")],"td05",)
    to_do(
        [(st.write, "Decrease the transmissivity and compare. Then increase the transmissivity and compare.")], "td06",) 
    to_do(
        [(st.write, "Decrease the storativity and compare. Then increase the storativity and compare.")], "td07",)        
"---"

st.markdown('''
            ### Computation of the drawdown
            The subsequent interactive plot demonstrate the response of a confined aquifer to pumping. You can modify the settings and parameters of the interactive plot with the sliders and toggles above. You can follow the instructions of the exercises, or you can do your own investigations.
            '''
)

# (Here the necessary functions like the well function $W(u)$ are defined. Later, those functions are used in the computation)
# Define a function, class, and object for Theis Well analysis

def well_function(u):
    return scipy.special.exp1(u)

def theis_u(T,S,r,t):
    u = r ** 2 * S / 4. / T / t
    return u

def theis_s(Q, T, u):
    s = Q / 4. / np.pi / T * well_function(u)
    return s

# (Here, the method computes the data for the well function. Those data can be used to generate a type curve.)
u_max = 1
r_max = 10000
u  = [u_max for x in range(r_max)]
u_inv  = [r_max/u_max for x in range(r_max)]
w_u  = [well_function(u_max/r_max) for x in range(r_max)]

def compute_s(T, S, t, Q, r):
    u = theis_u(T, S, r, t)
    s = theis_s(Q, T, u)
    return s

# This is the function to plot the graph with the data     

# Get input data
# Define the minimum and maximum for the logarithmic scale

log_min1 = -7.0 # T / Corresponds to 10^-7 = 0.0000001
log_max1 = 0.0  # T / Corresponds to 10^0 = 1

log_min2 = -7.0 # S / Corresponds to 10^-7 = 0.0000001
log_max2 = 0.0  # S / Corresponds to 10^0 = 1
   
columns = st.columns((1,1,1), gap = 'large')

with columns[0]:
    Q = st.slider(f'**Pumping rate (m³/s)**', 0.001,0.03,0.000,0.001,format="%5.3f")
    show_time = st.toggle('Show drawdown vs time plot')
    comparison = st.toggle('Compute a second variant for comparison')
    max_s = 20
    max_r = 1000

with columns[1]:
    r_show = st.slider(f'**Print Drawdown at _r_ (m)**',0,1000,100,1)
    t_show = st.slider(f'**Time to show(s)**',0.001,86400.*7,86400.,600.,format="%5.0f") 
    
with columns[2]:
    #Logaritmic T-Slider
    container = st.container()
    T_slider_value=st.slider('_(log of) Transmissivity T_', log_min1,log_max1,-3.0,0.01,format="%4.2f", key='T1' )
    T = 10 ** T_slider_value
    container.write("**_T_ in m²/s:** %5.2e" %T)
    if comparison:
        container = st.container()
        T2_slider_value=st.slider('_(log of) Transmissivity T2_', log_min1,log_max1,-3.0,0.01,format="%4.2f", key='T2' )
        T2 = 10 ** T2_slider_value
        container.write("**_T2_ in m²/s:** %5.2e" %T2)
    #Logaritmic S-Slider
    container = st.container()
    S_slider_value=st.slider('_(log of) Storativity S_', log_min2,log_max2,-4.0,0.01,format="%4.2f", key='S1' )
    S = 10 ** S_slider_value
    container.write("**_S_ (dimensionless):** %5.2e" %S)
    if comparison:
        #Logaritmic S-Slider
        container = st.container()
        S2_slider_value=st.slider('_(log of) Storativity S2_', log_min2,log_max2,-4.0,0.01,format="%4.2f", key='S2' )
        S2 = 10 ** S2_slider_value
        container.write("**_S2_ (dimensionless):** %5.2e" %S2)
        
    
# Range of temporal / spatial coordinate
r = np.linspace(1, max_r, 200)
r_neg = r * -1.0
t = np.linspace(1, 604800, 200)

# Compute drawdown for  1 and 2
s1 = compute_s(T, S, t_show, Q, r)
s2  = compute_s(T, S, t, Q, r_show)
if comparison:
    # Compute drawdown for  1_2
    s1_2 = compute_s(T2, S2, t_show, Q, r)
    s2_2 = compute_s(T2, S2, t, Q, r_show)

# Compute drawdown for a specific point
x_point = r_show
y_point = compute_s(T, S, t_show, Q, r_show)
x2_point = t_show
y2_point = compute_s(T, S, t_show, Q, r_show)

# Plotting and printing of results
fig=plt.figure(figsize=(15, 6))

plt.subplot(1, 2, 1)    
plt.title('Drawdown along distance with Theis', fontsize=16)
plt.plot(r, s1, linewidth=1., color='b', label=r'drawdown prediction')
plt.plot(r_neg, s1, linewidth=1, color='b')
if comparison:
    plt.plot(r, s1_2, linewidth=1., color='black', label=r'comparison', linestyle='dashed')
    plt.plot(r_neg, s1_2, linewidth=1, color='black', linestyle='dashed')
plt.fill_between(r,s1,max_s, facecolor='lightblue')
plt.fill_between(r_neg,s1,max_s, facecolor='lightblue')
plt.xlim(-max_r, max_r)
plt.ylim(max_s,-5)
plt.plot(x_point,y_point, marker='o', color='r',linestyle ='None', label='drawdown output') 
plt.xlabel(r'Distance from the well in m', fontsize=14)
plt.ylabel(r'Drawdown in m', fontsize=14)
plt.legend()
plt.grid(True)

plt.subplot(1, 2, 2)
if not show_time: 
    plt.axis('off')
if show_time:    
    plt.title('Drawdown vs time with Theis', fontsize=16)
    plt.plot(t, s2, linewidth=1., color='r', label=r'drawdown prediction')
    if comparison:
        plt.plot(t, s2_2, linewidth=1., color='black', label=r'drawdown prediction', linestyle='dashed')
    plt.fill_between(t,s2,max_s, facecolor='mistyrose')
    plt.plot(x2_point,y2_point, marker='o', color='b',linestyle ='None', label='drawdown output') 
    plt.xlim(0, 86400*7)
    plt.ylim(max_s,-5)
    plt.xlabel(r'time in s', fontsize=14)
    plt.ylabel(r'Drawdown in m', fontsize=14)
    plt.xticks(np.arange(0, 7*86400, step=86400))  # Set label locations.
    plt.legend()
    plt.grid(True)

st.pyplot(fig)

st.write("**DRAWDOWN output:**")
st.write("Distance from the well (in m): %8.2f" %x_point)
st.write('Time (in sec): %8i' %x2_point)
st.write('Drawdown at this distance (in m):  %5.2f' %y_point)


st.markdown('''
            ### Follow-up steps for the investigation
            Now that you have an impression for the interactive plot we can move on to understand the system more in detail. We will guide this with the following questions:
            '''
)
# Second assessment

with st.expander(":green[**Show/Hide the second assessment**]"):
    # Assessment to guide users through the interactive plot
    stb.single_choice(":blue[**How does the drawdown reaction change at one specific place if the storativity is decreased**]",
                  ["The drawdown is less.", "The drawdown is more", "The drawdown is not affected."],
                  1,success='CORRECT!   ...', error='Not quite. You can use the app to investigate what happens when you decrease storativity ... If required, you can read again about storativity _S_ in the following ressources _reference to GWP books...')
    stb.single_choice(":blue[**If the estimated transmissivity (T) is too low, how will the predicted drawdown compare to the true drawdown?**]",
                  ["The predicted drawdown will be too small", "The predicted drawdown will remain unchanged", "The predicted drawdown will be too large", "The predicted drawdown will fluctuate randomly"],
                  2,success='CORRECT!The predicted drawdown will be too large', error='Not quite. Feel free to answer again.')

st.markdown('''
            ### Intermediate conclusion and next steps
            So far, we investigated the flow to a well in a confined aquifer. We saw how the Theis solution can be used to calculate the drawdown in response to pumping for a specific place and time.
            
            In the next part of the application, we will see how we can derive the parameters of the aquifer with measured data. Move to the next section by using the sidemenu or the subsequent buttons.
            '''
)
"---"
# Navigation at the bottom of the side - useful for mobile phone users     
        
columnsN1 = st.columns((1,1,1), gap = 'large')
with columnsN1[0]:
    if st.button("Previous page"):
        st.switch_page("pages/01_📃_Theory.py")
with columnsN1[1]:
    st.subheader(':orange[**Navigation**]')
with columnsN1[2]:
    if st.button("Next page"):
        st.switch_page("pages/03_🟠_▶️ Theis_solution.py")
