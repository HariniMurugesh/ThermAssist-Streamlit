import streamlit as st

st.set_page_config(
    page_title="ThermAssist",
    layout="wide"
)
st.title("ThermAssist")
st.subheader(
    "Flanged Tapered Thermowell Engineering Review, Learning & Decision Assistant"
)
st.markdown("---")
st.header("Module 1 : Geometry Inputs")
col1,col2=st.columns(2)
with col1:
    root_dia=st.number_input(
        "Root Diameter (mm)",
        min_value=0.0,
        value=25.0
    )
    tip_dia=st.number_input(
        "Tip Diameter (mm)",
        min_value=0.0,
        value=16.0
    )
    bore_dia=st.number_input(
        "Bore Diameter (mm)",
        min_value=0.0,
        value=7.0
    )
with col2:
    insertion_length=st.number_input(
        "Insertion Length (mm)",
        min_value=0.0,
        value=300.0
    )
    immersion_length=st.number_input(
        "Immersion Length (mm)",
        min_value=0.0,
        value=280.0
    )
st.header("Module 2 : Geometry Review")
wall_thickness=(tip_dia-bore_dia)/2
taper_ratio=tip_dia/root_dia
slenderness_ratio=insertion_length/root_dia
st.subheader("Wall Thickness Review")
st.write(
    f"Wall Thickness = {wall_thickness:.2f} mm"
)
if wall_thickness >=4:
    st.success("PASS")
    st.info(
"Why?\n"
"\nAdequate wall thickness improves:\n"
"\n-Mechanical Strength\n"
"\n-Fatigue Resistance\n"
"\n-Vibration Resistance\n"            
 )
else:
    st.error("CHECK REQUIRED")
    st.warning(
"Why?\n"
"\nLow wall thickness reduces stiffness.\n"
"\nPotential Impact:\n"
"\n-Reduced mechanical strength\n"
"\n-Higher vibration susceptibility\n"
"\n-Lower fatigue resistance"
 )
    st.info(
"Recommended Actions:\n"
"\n-Increase Tip Diameter\n"
"\n-Reduce Bore Diameter\n"
"\n-Review Geometry"
 )
st.subheader("Taper Ratio Review")
st.write(
    f"Taper Ratio={taper_ratio:.2f}"
)
if 0.58<=taper_ratio<=1.0:
    st.success("PASS")
    st.info(
"Why PASS?\n"
"\nTaper ratio complies with ASME PTC 19.3 dimensional limits.\n"
"\nThe tapered geometry provides a good balance between mechanical strength and vibration performance."
 )
else:
    st.error("CKECK REQUIRED")
    st.info(
"Why?\n"
"\nTaper ratio is outside the ASME PTC 19.3 dimensional limits.\n"
"\nPotential Impact:\n"
"\n-Reduced thermowell strength\n"
"\n-Additional design review required"
 )
    st.info(
"\nRecommended Actions:\n"
"\n-Review Root Diameter\n"
"\n-Review Tip Diameter\n"
"\n-Recalculate Taper Ratio\n"
"\n-Verify WFC results after modification"
 )
st.subheader("Slenderness Ratio Review")
st.write(
    f"Slenderness Ratio={slenderness_ratio:.2f}"
)
if slenderness_ratio<=30:
    st.success("PASS")
else:
    st.warning("REVIEW")
    st.info(
"\nHigh slenderness ratio indicates a more flexible thermowell.\n"
"\nPotential Impact:\n"
"\n-Lower Natural Frequency\n"
"\n-Increased vibration tendency\n"
"\n-Higher resonance risk"
 )
st.header("Geometry Dashboard")
if wall_thickness >=4:
    wall_status="PASS"
else:
    wall_status="REVIEW"
if 0.58<=taper_ratio<=1.0:
    taper_status="PASS"
else:
    taper_status="REVIEW"
if slenderness_ratio<=30:
    slender_status="PASS"
else:
    slender_status="REVIEW"
st.code(f"""
INSERTION LENGTH REVIEW      {slender_status}
WALL THICKNESS REVIEW        {wall_status}
TAPER RATIO REVIEW           {taper_status}
""")
st.header("Module 8:ASME PTC 19.3 Review")
col1,col2=st.columns(2)
with col1:
    wake_frequency=st.number_input(
        "Wake Frequency (Hz)",
        min_value=0.0,
        value=45.0
    )
    natural_frequency=st.number_input(
        "Natural Frequency (Hz)",
        min_value=0.1,
        value=70.0
    )
with col2:
    dynamic_stress_ratio=st.number_input(
        "Dynamic Stress Ratio",
        min_value=0.0,
        value=0.60
    )
    velocity_ratio=st.number_input(
        "Velocity Ratio",
        min_value=0.0,
        value=0.50
    )
frequency_ratio=wake_frequency/natural_frequency
st.subheader("ASME Frequency Ratio Assessment")
st.write(
    f"Frequency Ratio (fs/fn)={frequency_ratio:.2f}"
)
st.write("Criterion 1 : Resonance Assessment")
if frequency_ratio<0.8:
    st.success("PASS")
    st.info(
"\nASME recommends maintaining fs/fn below 0.8\n"
"\nAlthough maximum vibration occurs near fs/fn = 1, vibration levels can increase significantly even before exact resonance is reached.\n"
"\nThis region is referred to as lock-in region.\n"
"\nMaintaining separation from resonance provides additional safety margin."
 )
else:
    st.error("FAIL")
    st.warning("""
Wake frequency is approaching natural frequency. Potential resonance condition exists.
The thermowell may experience significant vibration amplitudes.
""")
st.write("Criterion 2 : In-Line Vibration Assessment")
if 0.4<frequency_ratio<0.6:
    st.error("CHECK REQUIRED")
    st.warning(
"\nFrequency Ratio lies within:\n"
"\n0.4<fs/fn<0.6\n"
"\nASME identifies this region as potentially susceptible to in-line vibration.\n"
"\nIn-Line vibration is associated with drag-force fluctuations rather than lift-force fluctuations."
 )
    st.info(
"\nPotential Impact:\n"
"\n-Cyclic Loading\n"
"\n-Fatigue crack initiation\n"
"\n-Long-term thermowell damage\n"
"\n-Premature failure"
 )
else:
    st.success("PASS")
    st.info("""
Frequency Ratio lies outside the in-line vibration sensitive region.
No in-line vibration concern identified.
""")
primary_resonance_fail=frequency_ratio>=0.8
inline_vibration_fail=(
    0.4<frequency_ratio<0.6
)
if primary_resonance_fail or inline_vibration_fail:
    st.subheader("Recommended Actions")
    st.markdown(
"\n#1. Increase Stem Diameter\n"
"\nEffect:\n"
"\n-Increases stiffness\n"
"\n-Raises natural frequency\n"
"\n-Reduces vibration risk\n"
"\n--------------------------------------------------------------------------\n"
"\n#2. Reduce Insertion Length\n"
"\nEffect:\n"
"\n-Reduces flexibility\n"
"\n-Raises natural frequency\n"
"\n-Reduces vibration susceptibility\n"
"\n---------------------------------------------------------------------------\n"
"\n#3. Increase Root Diameter\n"
"\nEffect:\n"
"\n-Improves stiffness\n"
"\n-Improves fatigue resistance\n"
"\n----------------------------------------------------------------------------\n"
"\n#4. Review Process Velocity\n"
"\nEffect:\n"
"\n-Reduces wake excitation\n"
"\n-Lowers vibration tendency\n"
"\n-----------------------------------------------------------------------------\n"
"\n#5. Revalidate Thermowell Design\n"
"\nEngineering Note:\n"
"\nAny geometry change may affect:\n"
"\n-Frequency Ratio\n"
"\n-Taper Ratio\n"
"\n-Dynamic Stress\n"
"\n-Velocity Ratio.\n"
"\nRecalculate ASME assessment after modification."            
    )
st.subheader("Dynamic Stress Ratio Review")
st.write(
    f"Dynamic Stress Ratio={dynamic_stress_ratio:.2f}"
)
if dynamic_stress_ratio<=1:
    st.success("PASS")
    st.info("""
Dynamic stress remains within allowable limits.
Fatigue risk is acceptable.
""")
else:
    st.error("FAIL")
    st.warning("""
Dynamic stress exceeds allowable limit.
Potential fatigue damage may occur.
""")
st.subheader("Velocity Ratio Review")
st.write(
    f"Velocity Ratio={velocity_ratio:.2f}"
)
if velocity_ratio<=1:
    st.success("PASS")
else:
    st.warning("REVIEW")
    st.info("""
Higher velocity can increase flow-induced excitation.
Review vibration calculations.
""")
st.subheader("Failure Mode Predictor")
if primary_resonance_fail:
    failure_mode="Vortex-Induced Vibration"
    reason="""
Wake frequency is approaching natural frequency.
Potential resonance condition exists.
High vibration amplitudes may occur
"""
elif inline_vibration_fail:
    failure_mode="In-Line Vibration"
    reason="""
Frequency ratio falls within ASME in-line vibration region.
Drag-force fluctuations can produce repeated cyclic loading and fatigue damage.
"""
elif dynamic_stress_ratio>1:
    failure_mode="Fatigue Failure"
    reason="""
Dynamic stress exceeds allowable limit.
Repeated cyclic loading may result in fatigue cracking
"""
else:
    failure_mode="No Significant Failure Risk"
    reason="""
Current inputs do not indicate a major thermowell vibration concern.
"""
st.write(f"Most Likely Failure Mode : {failure_mode}")
st.info(reason)
st.header("ASME Review Dashboard")
freq_status=(
    "PASS"
    if not primary_resonance_fail
    else "FAIL"
)
inline_status=(
    "PASS"
    if not inline_vibration_fail
    else "CHECK REQUIRED"
)
stress_status=(
    "PASS"
    if dynamic_stress_ratio<=1
    else "FAIL"
)
velocity_status=(
    "PASS"
    if velocity_ratio<=1
    else "REVIEW"
)
st.code(f"""
ASME PTC 19.3 REVIEW
Primary Resonance Review : {freq_status}
In-Line Vibration Review : {inline_status}
Dynamic Stress Review : {stress_status}
Velocity Ratio Review : {velocity_status}
Failure Mode : {failure_mode}
""")
st.header("Engineering Concepts & Learning Centre")
with st.expander("What is Wake Frequency?"):
    st.write("""
Wake Frequency is the frequency at which vortices are shed from the thermowell.It acts as the excitation frequency
and directly affects thermowell vibration
""")
with st.expander("What is Natural Frequency?"):
    st.write("""
Every structure has a frequency at which it naturally prefers to vibrate. This is called Natural Frequency.
When wake freq approaches natural freq, resonance may occur, leading to high vibration amplitudes.
""")
with st.expander("What is Dynamic Stress Ratio?"):
    st.write("""
Dynamic Stress Ratio compares actual dynamic stress with allowable stress.
If the ratio exceeds allowable limits, fatigue damage can occur
""")
with st.expander("What is Reynolds Number?"):
    st.write(
"\nReynolds Number describes the nature of fluid flow.\n"
"\nLow Reynolds Number ---> Laminar flow\n"
"\nHigh Reynolds Number ---> Turbulent flow.\n"
"\nThis influences vortex shedding and wake frequency calculations."
 )
with st.expander("What is Strouhal Number?"):
    st.write(
"\nStrouhal Number relates:\n"
"\nVortex Shedding Frequency to Fluid Velocity ad Thermowell Diameter. \n"
"\nWake frequency is calculated using Strouhal Number. Therefore, it directly affects resonance assessment."
 )
with st.expander("What is Scruton Number?"):
    st.write(
"\nScruton Number represents the combined effect of mass and damping.\n"
"\nThink of damping as the ability to absorb vibration energy.\n" 
"\nExample:\n"
"\nLow damping ---> A swing keeps oscillating.\n"
"\nHigh damping ---> A swing settles quickly.\n"
"\nHigher Scruton Number generally means:\n"
"\n-Lower vibration amplitude\n"
"\n-Reduced Resonance Risk\n"
"\n-Improved thermowell reliability."
 )
st.header("What-If Analysys")
option=st.selectbox(
    "Select Design Change",
    [
        "Increase Stem Diameter",
        "Increase Root Diameter",
        "Reduce Insertion Length",
        "Increase Tip Diameter"
    ]
)
if option=="Increase Stem Diameter":
    st.success("Expected Impact")
    st.write(
"\n-Higher stiffness\n"
"\n-Higher natural frequency\n"
"\n-Reduced resonance risk.\n"
"\nPotential Drawbacks:\n"
"\n-Higher drag force\n"
"\n-Larger obstruction to flow"
 )
elif option=="Increase Root Diameter":
    st.success("Expected Impact")
    st.write(
"\n-Improved stiffness\n"
"\n-Better fatigue resistance\n"
"\n-Reduced vibration amplitude.\n"
"\nPotential Drawbacks:\n"
"\n-Geometry Review Required\n"
"\n-Flange compatibility check required."
 )
elif option=="Reduce Insertion Length":
    st.success("Expected Impact")
    st.write(
"\n-Higher stiffness\n"
"\n-Higher Natural frequency\n"
"\n-Reduced resonance susceptibility.\n"
"\nPotential Drawbacks:\n"
"\n-Measurement accuracy review required\n"
"\n-Reduced immersion possible."
 )
elif option == "Increase Tip Diameter":
    st.warning("CHECK REQUIRED")
    st.write(
"\nIncreasing Tip Diameter affects:\n"
"\n-Taper Ratio\n"
"\n-Wall Thickness\n"
"\n-Wake Frequency Characteristics\n"
"\n-Drag Force.\n"
"\nEngineering Note: \n"
"\nReassess geometry and ASME vibration criteria after modification."
 )
st.header("Final Engineering Recommendation")
if(
    primary_resonance_fail
    or inline_vibration_fail
    or dynamic_stress_ratio>1
):
    final_status="THERMOWELL REQUIRES REVIEW"
else:
    final_status="THERMOWELL ACCEPTABLE"
st.code(f"""
--------------------------------------------------------------------------------------
FLANGED TAPERED THERMOWELL REVIEW 
--------------------------------------------------------------------------------------
Wll Thickness Review : {wall_status}
Taper Ratio Review : {taper_status}
Slenderness Review : {slender_status}
Primary Resonance Review : {freq_status}
In-Line Vibration Review : {inline_status}
Dynamic Stress Review : {stress_status}
Velocity Ratio Review : {velocity_status}
--------------------------------------------------------------------------------------
LIKELY FAILURE MODE
{failure_mode}
--------------------------------------------------------------------------------------
FINAL STATUS 
{final_status}
--------------------------------------------------------------------------------------
""")
