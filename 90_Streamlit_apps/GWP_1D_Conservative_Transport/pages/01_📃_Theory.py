import streamlit as st

st.title('📃 Theory ')
st.title(' 1D Conservative Transport')

st.markdown(
    """
    ## Conceptual Model
"""
)

st.markdown(
    """
    At time = 0  source is in place
    
"""
)

left_co, cent_co, last_co = st.columns((20,60,20))
with cent_co:
    st.image('C:\_1_GitHub\Jupyter-Notebooks\90_Streamlit_apps\GWP_1D_Conservative_Transport/assets/images/1DtransportConceptualModel_1.jpg')


st.markdown(
    """
    Some time later, the solutes have migrated down gradient with the average flow velocity and have spread in the longitudinal direction due to local velocity varations that are 'lumped' mathematically into a term known as dispersion.
    
"""
)


left_co, cent_co, last_co = st.columns((20,60,20))
with cent_co:
    st.image('C:\_1_GitHub\Jupyter-Notebooks\90_Streamlit_apps\GWP_1D_Conservative_Transport/assets/images/1DtransportConceptualModel_2.jpg')


st.markdown(
    """
    :blue[The 1-dimensional solution represents conditions where lateral confinement prevents spreading except in the direction of flow.] For example, this is applicable to a column in a labroatory filled with a porous medium and with the source spread across the inflow end of the column.
"""
)

st.markdown(
    """
   The solute plumes differ due to the nature of the source. 
    - The :blue[Mass Pulse Source is a mass instantaneously introduced to the inflow end of the column.] The solutes move with the water flow and spread with ever decreasing concentration.
    - The :blue[Volume Pulse Source is a specified volume containing an evenly distributed specified mass introduced to the inflow end of the column.] The concentration is determined as a specified mass divided by the volume. The solutes flow in for the period of time required to take in that volume given the flow rate in the column. The solutes move with the groundwater flow and spread longitudinally with ever decreasing concentration.
    - The :blue[Continuous Source is water of specified concentration continuously introduced to the inflow end of the column such that mass is continuously added to the system.] The solutes move with the groundwater flow rising to the source concentration and spreading to lower concentrations at the front of the plume.   
"""
)

st.markdown(
    """
    ## Mathematical Models
"""
)

st.markdown(
    """   
    Solutions are based on Ogata A., Banks R. B. (1961): A solution of the differential equation of longitudinal dispersion in porous media, USGS Prof. Paper 411-A. https://pubs.usgs.gov/pp/0411a/report.pdf
"""
)
   
st.markdown(
    """
    - M : mass (grams)
    - Co : initial concentration (grams/cubic meter)
    - C : concentration (grams/cubic meter)
    - A : area of flow column (square meters)
    - K : hydraulic conducitivity (meters/second)
    - i : hydraulic gradient (dimensionless)
    - n : effective porosity (dimensionless)
    - v : average linear velocity = Ki/n (meters/second)
    - a : dispersivity (meters)
    - D : dispersion coefficient - product of dispersivity and average linear velocity (square meters/second)
    - x : distance from the source (meters)
    - t : time since the source was introduced (seconds)

"""
)

st.markdown(
    """
      
    ## :blue[Mass Pulse Source 1D Transport]

"""
)

st.latex(r'''C(x,t) = \frac{M}{2  A  n \sqrt{\pi  D  t}} e^{-\frac{(x - v t)^2}{4 D t}}''')

st.markdown(
    """
     ## :blue[Volume Pulse Source 1D Transport]

"""
)


st.markdown(
    """
  
  This is a combination of two superposed continuous source solutions. The first solution starts at time zero with Co equal to the source concentration and continues indefinitely. The second solution is summed to the first and using negative source concentration and begins at the time when injection of the specified volume is complete then continues indefinitely.

"""
)


st.latex(r'''C(x,t) = \frac{Co}{ 2 }  \left( erfc \left( \frac{x - vt}{2 \sqrt{Dt}} \right) \right) + \frac{-Co}{ 2 }  \left( erfc \left( \frac{x - v(t-tduration)}{2 \sqrt{D(t-tduration)}} \right) \right)''')


st.markdown(
    """
     ## :blue[Continuous Source 1D Transport]

"""
)

st.latex(r'''C(x,t) = \frac{Co}{ 2 }  ( erfc ( \frac{x - vt}{2 \sqrt{Dt}} )''')

st.markdown(
    """

"""
)
st.markdown (
    """   
    :green
    ___
  
"""
)


st.markdown(
    """
        :green[The Groundwater Project is nonprofit with one full-time staff and over a 1000 volunteers.]
        """
)
st.markdown(
    """
        :green[Please help us by using the following link when sharing this tool with others.]
        """   
)

st.markdown(
    """
        https://interactive-education.gw-project.org/1D_conservative_transport/
        """   
)

