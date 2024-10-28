# Loading the required Python libraries
import numpy as np
import matplotlib.pyplot as plt
import scipy.special
import streamlit as st

st.title('Theis drawdown prediction - Fitting Formation parameter to measured data')
st.markdown("""
            This interactive document allows to apply the Theis principle for pumping test evaluation in confined, transient setups. The notebook is based on an Spreadsheet from Prof. Rudolf Liedl.
            
            ### General situation
            We consider a confined aquifer with constant transmissivity. If a well is pumping water out of the aquifer, radial flow towards the well is induced. To calculate the hydraulic situation, the following simplified flow equation can be used. This equation accounts for 1D radial transient flow towards a fully penetrating well within a confined aquifer without further sinks and sources:
"""
)
st.latex(r'''\frac{\partial^2 h}{\partial r^2}+\frac{1}{r}\frac{\partial h}{\partial r}=\frac{S}{T}\frac{\partial h}{\partial t}''')
st.markdown("""
            ### Mathematical model and solution
            Charles V. Theis presented a solution for this by deriving
"""
)
st.latex(r'''s(r,t)=\frac{Q}{4\pi T}W(u)''')
st.markdown("""
            with the well function
"""
)
st.latex(r'''W(u) = \int_{u }^{+\infty} \frac{e^{-\tilde u}}{\tilde u}d\tilde u''')
st.markdown("""
            and the dimensionless variable
"""
)
st.latex(r'''u = \frac{Sr^2}{4Tt}''')
st.markdown("""
            This equations are not easy to solve. Historically, values for the well function were provided by tables or as so called type-curve. The type-curve matching with experimental data for pumping test analysis can be considered as one of the basic hydrogeological methods. However, modern computer provide an easier and more convinient way to solve the 1D radial flow equation based on the Theis approach. Subsequently, the Theis equation is solved with Python routines. The results for the measured data are graphically presented in an interactive plot.
            
            The red dots are the measured data.
            
            Modify the transmissivity _**T**_ and the storativity _**S**_ to fit the measured data to the well function.
            
            **Select the data below!**
"""
)            

# Computation

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

def theis_wu(Q, T, s):
    wu = s * 4. * np.pi * T / Q
    return wu

def compute_s(T, S, t, Q, r):
    u = theis_u(T, S, r, t)
    s = theis_s(Q, T, u)
    return s

# (Here, the methode computes the data for the well function. Those data can be used to generate a type curve.)
u_max = 1
r_max = 100000
u  = [u_max for x in range(r_max)]
um = [u_max for x in range(r_max)]
u_inv  = [r_max/u_max for x in range(r_max)]
um_inv = [r_max/u_max for x in range(r_max)]
w_u  = [well_function(u_max/r_max) for x in range(r_max)]
w_um = [well_function(u_max/r_max) for x in range(r_max)]

for x in range(1,r_max,1):
    if x>0:
        u[x] = x*u_max/r_max
        u_inv[x] = 1/u[x]
        w_u[x] = well_function(u[x])

# Select data
columns = st.columns((10,80,10), gap = 'large')
with columns[1]:
    datasource = st.selectbox("**What data should be used?**",
    ("Synthetic textbook data", "Viterbo 2023", "Varnum 2018 - R14", "Random data with noise"), key = 'Data')

if (st.session_state.Data == "Synthetic textbook data"):
    # Data from SYMPLE exercise
    m_time = [1,1.5,2,2.5,3,4,5,6,8,10,12,14,18,24,30,40,50,60,100,120] # time in minutes
    m_ddown = [0.66,0.87,0.99,1.11,1.21,1.36,1.49,1.59,1.75,1.86,1.97,2.08,2.20,2.36,2.49,2.65,2.78,2.88,3.16,3.28]   # drawdown in meters
    # Parameters needed to solve Theis (From the SYMPLE example/excercise)
    r = 120       # m
    b = 8.5       # m
    Qs = 0.3/60   # m^3/s
    Qd = Qs*60*60*24 # m^3/d
elif(st.session_state.Data == "Viterbo 2023"):
    # Data from Viterbo 2023
    m_time = [0.083333333, 1, 1.416666667, 2.166666667, 2.5, 2.916666667, 3.566666667, 3.916666667, 4.416666667, 4.833333333, 5.633333333, 6.516666667, 7.5, 8.916666667, 10.13333333, 11.16666667, 12.6, 16.5, 18.53333333, 22.83333333, 27.15, 34.71666667, 39.91666667, 48.21666667, 60.4, 72.66666667, 81.91666667, 94.66666667, 114.7166667, 123.5]
    m_ddown = [0.04, 0.09, 0.12, 0.185, 0.235, 0.22, 0.26, 0.3, 0.31, 0.285, 0.34, 0.4, 0.34, 0.38, 0.405, 0.38, 0.385, 0.415, 0.425, 0.44, 0.44, 0.46, 0.47, 0.495, 0.54, 0.525, 0.53, 0.56, 0.57, 0.58]
    # Parameters needed to solve Theis (From the SYMPLE example/excercise) !!! UPDATE !!!
    r = 130       # m
    b = 8.5       # m
    Qs = 0.3/60   # m^3/s
    Qd = Qs*60*60*24 # m^3/d
elif(st.session_state.Data == "Varnum 2018 - R14"):
    #R14\n",
    m_time  = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226,227,228,229,230,231,232,233,234,235,236,237,238,239,240,241,242,243,244,245,246,247,248,249,250,251,252,253,254,255,256,257,258,259,260,261,262,263,264,265,266,267,268,269,270,271,272,273,274,275,276,277,278,279,280,281,282,283,284,285,286,287,288,289,290,291,292,293,294,295,296,297,298,299,300,301,302,303,304,305,306,307,308,309,310,311,312,313,314,315,316,317,318,319,320,321,322,323,324,325,326,327,328,329,330,331,332,333,334,335,336,337,338,339,340,341,342,343,344,345,346,347,348,349,350,351,352,353,354,355,356,357,358,359,360,361,362,363,364,365,366,367,368,369,370,371,372,373,374,375,376,377,378,379,380,381,382,383,384,385,386,387,388,389,390,391,392,393,394,395,396,397,398,399,400,401,402,403,404,405,406,407,408,409,410,411,412,413,414,415,416,417,418,419,420,421,422,423,424,425,426,427,428,429,430,431,432,433,434,435,436,437,438,439,440,441,442,443,444,445,446,447,448,449,450,451,452,453,454,455,456,457,458,459,460,461,462,463,464,465,466,467,468,469,470,471,472,473,474,475,476,477,478,479,480,481,482,483,484,485,486,487,488,489,490,491,492,493,494,495,496,497,498,499,500,501,502,503,504,505,506,507,508,509,510,511,512,513,514,515,516,517,518,519,520,521,522,523,524,525,526,527,528,529,530,531,532,533,534,535,536,537,538,539,540,541,542,543,544,545,546,547,548,549,550,551,552,553,554,555,556,557,558,559,560,561,562,563,564,565,566,567,568,569,570,571,572,573,574,575,576,577,578,579,580,581,582,583,584,585,586,587,588,589,590,591,592,593,594,595,596,597,598,599,600,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633,634,635,636,637,638,639,640,641,642,643,644,645,646,647,648,649,650,651,652,653,654,655,656,657,658,659,660,661,662,663,664,665,666,667,668,669,670,671,672,673,674,675,676,677,678,679,680,681,682,683,684,685,686,687,688,689,690,691,692,693,694,695,696,697,698,699,700,701,702,703,704,705,706,707,708,709,710,711,712,713,714,715,716,717,718,719,720,721]
    m_ddown = [0.003,0.01,0.022,0.034,0.028,0.04,0.04,0.052,0.058,0.052,0.062,0.068,0.057,0.063,0.081,0.069,0.081,0.057,0.076,0.07,0.085,0.091,0.103,0.085,0.079,0.091,0.115,0.098,0.092,0.098,0.113,0.131,0.101,0.095,0.083,0.107,0.107,0.107,0.119,0.113,0.101,0.083,0.108,0.12,0.114,0.121,0.121,0.127,0.133,0.116,0.117,0.098,0.104,0.122,0.116,0.115,0.109,0.109,0.115,0.115,0.107,0.118,0.118,0.111,0.11,0.122,0.103,0.121,0.108,0.107,0.113,0.124,0.112,0.112,0.112,0.112,0.124,0.13,0.112,0.124,0.126,0.126,0.119,0.131,0.119,0.131,0.125,0.113,0.113,0.137,0.115,0.121,0.115,0.115,0.145,0.115,0.109,0.127,0.115,0.133,0.108,0.114,0.132,0.12,0.138,0.12,0.12,0.126,0.115,0.151,0.12,0.126,0.114,0.114,0.132,0.126,0.109,0.127,0.127,0.109,0.131,0.125,0.131,0.13,0.124,0.118,0.13,0.118,0.117,0.123,0.133,0.11,0.134,0.122,0.122,0.135,0.123,0.135,0.136,0.13,0.124,0.118,0.112,0.112,0.106,0.112,0.124,0.142,0.118,0.123,0.114,0.119,0.125,0.119,0.137,0.119,0.113,0.118,0.112,0.118,0.115,0.001,0.103,0.133,0.103,0.11,0.212,0.116,0.14,0.02,0.132,0.072,0.168,0.126,0.108,0.096,0.132,0.108,0.06,0.126,0.085,0.049,0.08,0.08,0.062,0.068,0.063,0.069,0.081,0.075,0.065,0.077,0.059,0.083,0.065,0.077,0.083,0.077,0.077,0.071,0.089,0.071,0.083,0.077,0.064,0.076,0.076,0.076,0.076,0.057,0.067,0.079,0.073,0.079,0.073,0.078,0.078,0.078,0.072,0.06,0.068,0.062,0.074,0.067,0.061,0.067,0.079,0.085,0.055,0.06,0.075,0.081,0.069,0.081,0.087,0.069,0.087,0.201,0.123,0.116,0.106,0.095,0.101,0.089,0.089,0.108,0.108,0.102,0.114,0.109,0.104,0.116,0.104,0.104,0.104,0.104,0.098,0.111,0.099,0.111,0.104,0.115,0.109,0.097,0.103,0.091,0.097,0.097,0.097,0.102,0.111,0.105,0.093,0.093,0.087,0.1,0.094,0.112,0.1,-0.044,0.085,0.115,0.115,0.096,-0.066,0.072,0.09,0.102,0.102,0.114,0.116,0.218,0.11,0.11,0.097,0.109,0.115,0.109,0.114,0.12,0.113,0.118,0.112,0.111,0.117,0.098,0.098,0.109,0.085,0.096,0.106,0.111,0.105,0.105,0.098,0.116,0.104,0.098,0.109,0.091,0.115,0.115,0.127,0.115,0.115,0.127,0.122,0.104,0.116,0.104,0.108,0.119,0.119,0.119,0.119,0.101,0.101,0.119,0.101,0.107,0.097,0.103,0.097,0.127,0.115,0.116,0.11,0.11,0.116,0.122,0.101,0.107,0.113,0.113,0.107,0.107,0.119,0.12,0.114,0.096,0.094,0.088,0.107,0.113,0.113,0.107,0.102,0.102,0.102,0.108,0.116,0.092,0.092,0.103,0.103,0.109,0.103,0.078,0.102,0.12,0.106,0.106,0.1,0.112,0.106,0.1,0.094,0.111,0.105,0.117,0.108,0.108,0.113,0.101,0.125,0.107,0.095,0.112,0.106,0.094,0.11,0.104,0.104,0.115,0.109,0.121,0.115,0.103,0.097,0.102,0.118,0.11,0.115,0.102,0.113,0.075,0.104,0.085,0.083,0.1,0.125,0.131,0.119,0.113,0.114,0.102,0.108,0.12,0.139,0.115,0.123,0.123,0.111,0.111,0.112,0.118,0.112,0.118,0.112,0.125,0.102,0.12,0.102,0.115,0.121,0.109,0.103,0.109,0.115,0.109,0.131,0.084,0.102,0.12,0.109,0.103,0.109,0.122,0.11,0.123,0.104,0.103,0.097,0.102,0.108,0.107,0.107,0.1,0.094,0.105,0.115,0.103,0.103,0.121,0.098,0.104,0.128,0.104,0.11,0.128,0.102,0.114,0.108,0.108,0.103,0.109,0.121,0.115,0.109,0.103,0.107,0.113,0.088,0.118,0.106,0.106,0.106,0.112,0.112,0.112,0.107,0.107,0.107,0.119,0.107,0.125,0.107,0.101,0.113,0.119,0.094,0.112,0.088,0.111,0.099,0.105,0.093,0.098,0.098,0.11,0.109,0.127,0.103,0.121,0.115,0.109,0.091,0.115,0.115,0.121,0.116,0.11,0.104,0.098,0.098,0.11,0.116,0.092,0.104,0.122,0.122,0.11,0.104,0.104,0.104,0.122,0.11,0.104,0.11,0.122,0.121,0.108,0.108,0.101,0.113,0.112,0.105,0.105,0.092,0.098,0.121,0.127,0.12,0.114,0.126,0.12,0.114,0.107,0.101,0.101,0.099,0.117,0.111,0.123,0.123,0.111,0.13,0.106,0.1,0.112,0.103,0.109,0.115,0.109,0.122,0.116,0.11,0.116,0.122,0.11,0.115,0.115,0.115,0.115,0.115,0.121,0.091,0.115,0.127,0.121,0.108,0.108,0.12,0.102,0.114,0.113,0.107,0.107,0.119,0.125,0.104,0.116,0.103,0.109,0.109,0.121,0.102,0.114,0.102,0.108,0.113,0.125,0.106,0.118,0.106,0.112,0.118,0.1,0.118,0.106,0.125,0.119,0.131,0.131,0.107,0.119,0.101,0.119,0.107,0.119,0.107,0.125,0.113,0.119,0.106,0.13,0.118,0.105,0.117,0.111,0.128,0.11,0.122,0.11,0.122,0.111,0.141,0.129,0.117,0.135,0.115,0.109,0.121,0.127,0.115,0.109,0.121,0.127,0.115,0.115,0.115,0.133,0.121,0.109,0.103,0.133,0.114,0.126,0.108,0.126,0.122,0.128,0.122,0.116,0.128,0.11,0.122,0.123,0.111,0.123,0.122,0.122,0.121,0.121,0.115,0.121,0.127,0.109,0.109,0.121,0.111,0.117,0.123,0.117,0.117,0.129,0.11,0.134,0.134,0.122,0.099,0.123,0.111,0.117,0.105,0.135,0.148,0.112,0.124,0.112,0.123]
    # Parameters needed to solve Theis (From the SYMPLE example/excercise) !!! UPDATE !!!
    r = 10       # m
    b = 15.0       # m
    Qs = 0.0115   # m^3/s
    Qd = Qs*60*60*24 # m^3/d
elif(st.session_state.Data == "Random data with noise"):
    r = 20       # m
    b = 20       # m
    Qs = 0.2/60   # m^3/s
    Qd = Qs*60*60*24 # m^3/d
    T_random = 1.23E-4*b*np.random.randint(1, 10000)/100
    S_random = 1E-5*b*np.random.randint(1, 10000)/100
    st.session_state.T_random = T_random
    st.session_state.S_random = S_random
    st.write(T_random)
    st.write(S_random)
    m_time_all  = [1,2,3,4,5,6,7,8,9,10,12,14,16,18,20,25,30,35,40,45,50,55,60,70,80,90,100,110,120,130,140,150,160,170,180,210,240,270,300,330,360,420,480,540,600,660,720,780,840,900]
    m_ddown_all = [compute_s(T_random, S_random, i, Qs, r)*np.random.randint(92, 108)/100 for i in m_time_all] # time in seconds
    n_samples = np.random.randint(24, 49)
    m_time = m_time_all[:n_samples]
    m_ddown = m_ddown_all[:n_samples]
    # Parameters needed to solve Theis (From the SYMPLE example/excercise) !!! UPDATE !!!

m_time_s = [i*60 for i in m_time] # time in seconds
num_times = len(m_time)


@st.experimental_fragment
def inverse():
    # This is the function to plot the graph with the data     
    # Get input data
    # Define the minimum and maximum for the logarithmic scale
    log_min1 = -7.0 # T / Corresponds to 10^-7 = 0.0000001
    log_max1 = 0.0  # T / Corresponds to 10^0 = 1
    log_min2 = -7.0 # S / Corresponds to 10^-7 = 0.0000001
    log_max2 = 0.0  # S / Corresponds to 10^0 = 1
   
    columns2 = st.columns((1,1), gap = 'large')
    with columns2[0]:
        T_slider_value=st.slider('(log of) **Transmissivity** in m2/s', log_min1,log_max1,-3.0,0.01,format="%4.2f" )
        # Convert the slider value to the logarithmic scale
        T = 10 ** T_slider_value
        # Display the logarithmic value
        st.write("_Transmissivity_ in m2/s: %5.2e" %T)
        S_slider_value=st.slider('(log of) **Storativity**', log_min2,log_max2,-4.0,0.01,format="%4.2f" )
        # Convert the slider value to the logarithmic scale
        S = 10 ** S_slider_value
        # Display the logarithmic value
        st.write("_Storativity_ (dimensionless):** %5.2e" %S)
        refine_theis = st.toggle("**Refine** the range of the **Theis matching plot**")
    with columns2[1]:
        Q_pred = st.slider(f'**Pumping rate** (m^3/s) for the **prediction**', 0.001,0.100,Qs,0.001,format="%5.3f")
        r_pred = st.slider(f'**Distance** (m) from the **well** for the **prediction**', 1,1000,r,1)
        per_pred = st.slider(f'**Duration** of the **prediction period** (days)',1,3652,3,1) 
        max_t = 86400*per_pred
        if per_pred <= 3:
            t_search = st.slider(f'**Select the value of time (s) for printout**', 1,max_t,1,1)
        elif per_pred <= 7:
            t_search_h = st.slider(f'**Select the value of time (hours) for printout**', 1.,24.*per_pred,1.)
            t_search = t_search_h*3600
        elif per_pred <= 366:
            t_search_d = st.slider(f'**Select the value of time (days) for printout**', 1.,per_pred*1.0,1.)
            t_search = t_search_d*86400
        else:
            t_search_mo = st.slider(f'**Select the value of time (months) for printout**', 1.,per_pred/30.4375,1.)
            t_search = t_search_mo*2629800
        auto_y = st.toggle("Adjust the range of drawdown plotting")

    

    # PLOT MEASURED DATA
    max_s = 20
    x = 0
    for t1 in m_time_s:
        um[x] = theis_u(T,S,r,t1)
        um_inv[x] = 1/um[x]
        w_um[x] = theis_wu(Qs,T,m_ddown[x])
        x = x+1

    # PLOT DRAWDOWN VS TIME
    # Range of delta_h / delta_l values (hydraulic gradient)
    t2 = np.linspace(1, max_t, 100)
    t2_h = t2/3600
    t2_d = t2/86400
    t2_mo = t2/2629800

    # Compute s for prediction
    s  = compute_s(T, S, t2, Q_pred, r_pred)

    # Compute s for a specific point
    x_point = t_search
    y_point = compute_s(T, S, t_search, Q_pred, r_pred)
    
    fig = plt.figure(figsize=(12,7))
    ax = fig.add_subplot(1, 2, 1)
    ax.plot(u_inv, w_u)
    ax.plot(um_inv[:num_times], w_um[:num_times],'ro')
    plt.yscale("log")
    plt.xscale("log")
    if refine_theis:
        plt.axis([1,1E5,1E-2,1E+2])
    else:
        plt.axis([1e-1,1E7,1E-4,1E+4])
        ax.text((2E-1),5E+3,'Coarse plot - Refine for final fitting')
    plt.xlabel(r'1/u', fontsize=14)
    plt.ylabel(r'w(u)', fontsize=14)
    plt.title('Theis drawdown', fontsize=16)
    ax.grid(which="both")
    plt.legend(('well function','measured'))

    ax = fig.add_subplot(1, 2, 2)
    if per_pred <= 3:
        plt.plot(t2, s, linewidth=3., color='r', label=r'Drawdown prediction')
        plt.plot(t_search,y_point, marker='o', color='b',linestyle ='None', label='drawdown output')
        plt.xlabel(r'Time in sec', fontsize=14)
        plt.xlim(0, max_t)
    elif per_pred <= 7:
        plt.plot(t2_h, s, linewidth=3., color='r', label=r'Drawdown prediction')
        plt.plot(t_search_h,y_point, marker='o', color='b',linestyle ='None', label='drawdown output')
        plt.xlabel(r'Time in hours', fontsize=14)
        plt.xlim(0, max_t/3600)
    elif per_pred <= 366:
        plt.plot(t2_d, s, linewidth=3., color='r', label=r'Drawdown prediction')
        plt.plot(t_search_d,y_point, marker='o', color='b',linestyle ='None', label='drawdown output')
        plt.xlabel(r'Time in days', fontsize=14)
        plt.xlim(0, max_t/86400)
    else:
        plt.plot(t2_mo, s, linewidth=3., color='r', label=r'Drawdown prediction')
        plt.plot(t_search_mo,y_point, marker='o', color='b',linestyle ='None', label='drawdown output')
        plt.xlabel(r'Time in months', fontsize=14)
        plt.xlim(0, max_t/2629800)

    #plt.ylim(max_s, 0)
    if auto_y:
        plt.ylim(bottom=0, top=None)
    else:
        plt.ylim(bottom=0, top=max_s)
    ax.invert_yaxis()
    plt.plot(x_point,y_point, marker='o', color='b',linestyle ='None', label='drawdown output') 
    plt.ylabel(r'Drawdown in m', fontsize=14)
    plt.title('Drawdown prediction with Theis', fontsize=16)
    plt.legend()
    plt.grid(True)
    
    st.pyplot(fig)

    columns3 = st.columns((1,1), gap = 'medium')
    with columns3[0]:
        st.write("**Parameter estimation**")
        st.write("Distance of measurement from the well (in m): %3i" %r)
        st.write("Pumping rate of measurement (in m^3/s): %5.3f" %Qs)
        st.write("Thickness of formation b = ","% 5.2f"% b, " m")
        st.write("Transmissivity T = ","% 10.2E"% T, " m^2/s")
        st.write("(Hydr. cond. K) = ","% 10.2E"% (T/b), " m^2/s")
        st.write("Storativity    S = ","% 10.2E"% S, "[-]")

    with columns3[1]:
        st.write("**Prediction**")
        st.write("Distance of prediction from the well (in m): %3i" %r_pred)
        st.write("Pumping rate of prediction (in m^3/s): %5.3f" %Q_pred)
        st.write("Time since pumping start (in s): %3i" %x_point)
        if per_pred <= 3:
            st.write("Time since pumping start (in s): %3i" %t_search)
        elif per_pred <= 7:
            st.write("Time since pumping start (in hours): %5.2f" %t_search_h)
        elif per_pred <= 366:
            st.write("Time since pumping start (in days): %5.2f" %t_search_d)
        else:
            st.write("Time since pumping start (in months): %5.2f" %t_search_mo)
        st.write("Predicted drawdown at this distance and time (in m):  %5.2f" %y_point)
    
    if (st.session_state.Data == "Random data with noise"):
        st.write("'True' Transmissivity T = ","% 10.2E"% st.session_state.T_random, " m^2/s")
        st.write("'True' Storativity    S = ","% 10.2E"% st.session_state.S_random, "[-]")
inverse()
