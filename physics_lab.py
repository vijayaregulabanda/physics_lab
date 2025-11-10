import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# --- Page config ---
st.set_page_config(page_title="Engineering Physics Virtual Lab", layout="wide")

# --- Dark theme + glowing title CSS ---
st.markdown("""
<style>
body { background-color: #0c0c0c; color: #ffffff; }
.glow-title {
    font-size: 48px; font-weight: bold; text-align: center;
    color: #00ffe7;
    text-shadow: 0 0 5px #00ffe7, 0 0 10px #00ffe7, 0 0 20px #00ffe7, 0 0 40px #00ffe7;
    animation: glow 1.5s infinite alternate;
}
@keyframes glow {
    from { text-shadow: 0 0 5px #00ffe7, 0 0 10px #00ffe7, 0 0 20px #00ffe7, 0 0 40px #00ffe7; }
    to   { text-shadow: 0 0 20px #00ffae, 0 0 30px #00ffae, 0 0 40px #00ffae, 0 0 50px #00ffae; }
}
</style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="glow-title">🔬 Engineering Physics Virtual Lab</h1>', unsafe_allow_html=True)

# --- Helper function to avoid slider step errors ---
def safe_step(step, default):
    if step == 0:
        return 1 if isinstance(default, int) else 0.01
    return step

# --- Plotting function ---
def plot_simulation(exp_name, x, y, result=None):
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(x, y, color="cyan", label="Simulation")
    ax.set_facecolor("#1a1a1a")
    ax.set_title(f"{exp_name} - Simulation Output", color="white")
    ax.tick_params(colors="white")
    ax.spines['bottom'].set_color('white')
    ax.spines['left'].set_color('white')
    ax.legend()
    ax.grid(True, color="gray")
    st.pyplot(fig)

# --- All 17 experiments ---
EXPERIMENTS = {
    "1. Radius of Curvature by Newton's Rings": {
        "theory": "Newton's rings are interference patterns formed by reflection between a plano-convex lens and a flat glass plate.",
        "description": "Find the radius of curvature of a plano-convex lens.",
        "formula": "R = r² / (n × λ)",
        "inputs": {"Radius of ring (cm)": (0.1, 10.0, 0.1, 0.5), "Wavelength (μm)": (0.0003, 0.0008, 0.00001, 0.0006), "Ring order (n)": (1, 20, 1, 1)},
        "simulate": lambda r, wl, n: (np.linspace(0, r*2, 400), (np.sin(2*np.pi*np.linspace(0, r*2, 400)/wl))**2, (r**2)/(n*wl))
    },
    "2. Wavelengths of Mercury Spectrum": {
        "theory": "Using a diffraction grating, the wavelengths of mercury's spectral lines are measured from the diffraction angles.",
        "description": "Calculate wavelengths of mercury spectral lines using diffraction grating.",
        "formula": "nλ = d sin θ",
        "inputs": {"Grating spacing (μm)": (0.1, 5.0, 0.01, 1.0), "Diffraction order (n)": (1, 5, 1, 1)},
        "simulate": lambda d, n: (["Violet","Blue","Green","Yellow","Orange"], np.arcsin(np.clip(n*0.332/d,-1,1))*180/np.pi)
    },
    "3. Verification of Brewster's Law": {
        "theory": "Brewster's angle is the angle of incidence where reflected light is completely polarized.",
        "description": "Verify Brewster's law and calculate Brewster's angle.",
        "formula": "θ_B = arctan(n₂ / n₁)",
        "inputs": {"Refractive index n₂": (1.0,3.0,0.01,1.5)},
        "simulate": lambda n2: (np.linspace(0,90,180), np.abs(np.cos(np.deg2rad(np.linspace(0,90,180))))*(n2-1)/(n2+1))
    },
    "4. Wavelength of Laser Light using Diffraction Grating": {
        "theory": "Laser wavelength can be determined using diffraction grating by measuring the diffraction angles.",
        "description": "Determine laser light wavelength using grating and diffraction order.",
        "formula": "nλ = d sin θ",
        "inputs": {"Grating spacing (μm)": (0.1,5.0,0.01,1.0), "Diffraction order (n)": (1,5,1,1)},
        "simulate": lambda d,n: (np.linspace(0,90,180), np.sin(np.deg2rad(np.linspace(0,90,180)))*d*n)
    },
    "5. Estimation of Planck's Constant": {
        "theory": "Planck's constant can be estimated from the photoelectric effect relating frequency and stopping potential.",
        "description": "Calculate Planck's constant from frequency and stopping potential.",
        "formula": "eV = hν - φ",
        "inputs": {"Frequency (THz)": (400,800,1,500), "Stopping Potential (V)": (0,5,0.01,1)},
        "simulate": lambda f,V: (np.array([f]), np.array([V]), 6.626e-34)
    },
    "6. Energy Band Gap of Semiconductor": {
        "theory": "Energy band gap of a semiconductor is determined from temperature dependence of resistance.",
        "description": "Determine band gap of semiconductor using temperature and resistance.",
        "formula": "Eg = 2kT ln(R2/R1)",
        "inputs": {"Temperature (K)": (250,350,1,300), "Resistance (Ω)": (100,1000,10,500)},
        "simulate": lambda T,R: (np.linspace(250,350,100), np.exp(-1/(np.linspace(250,350,100)/300)), 1.12)
    },
    "7. Solar Cell Characteristics": {
        "theory": "Solar cell characteristics are studied by measuring current-voltage behavior under illumination.",
        "description": "Plot I-V characteristics of a solar cell.",
        "formula": "I = I₀ (exp(qV/kT) - 1)",
        "inputs": {"Light intensity (%)": (10,100,10,50)},
        "simulate": lambda I: (np.linspace(0,1,100), I*(1-np.linspace(0,1,100)))
    },
    "8. Diffraction of Light through Slit": {
        "theory": "Light diffraction occurs when it passes through a narrow slit causing spreading of waves.",
        "description": "Observe diffraction pattern and intensity variation.",
        "formula": "I = I₀ (sinβ/β)²",
        "inputs": {"Slit width (mm)": (0.01,1.0,0.01,0.2), "Wavelength (μm)": (0.0003,0.0008,0.00001,0.0006)},
        "simulate": lambda a,wl: (np.linspace(-0.02,0.02,400), (np.sinc(np.linspace(-0.02,0.02,400)/wl))**2)
    },
    "9. Hall Effect Experiment": {
        "theory": "The Hall effect determines carrier concentration and type of charge carriers in semiconductors.",
        "description": "Study Hall voltage variation with magnetic field.",
        "formula": "V_H = (IB) / (net)",
        "inputs": {"Magnetic field (T)": (0.1,2.0,0.1,1.0), "Current (A)": (0.01,0.1,0.01,0.05)},
        "simulate": lambda B,I: (np.linspace(0,2,100), I*np.linspace(0,2,100))
    },
    "10. Ultrasonic Diffraction": {
        "theory": "Ultrasonic waves diffract light producing fringes similar to optical diffraction.",
        "description": "Find wavelength and velocity of ultrasonic waves in liquid.",
        "formula": "λ = (x₂ - x₁) / n",
        "inputs": {"Separation distance (mm)": (1,10,0.1,5), "Number of fringes (n)": (1,10,1,5)},
        "simulate": lambda d,n: (np.linspace(1,10,10), np.linspace(1,10,10)/n)
    },
    "11. Melde’s String Experiment": {
        "theory": "Melde’s experiment determines frequency of AC supply using transverse or longitudinal vibrations.",
        "description": "Calculate frequency using tension and linear density.",
        "formula": "f = (1/2L) √(T/μ)",
        "inputs": {"Tension (N)": (0.1,10,0.1,1), "Length (m)": (0.1,2,0.1,1), "Mass per unit length (kg/m)": (0.001,0.1,0.001,0.01)},
        "simulate": lambda T,L,mu: (np.linspace(0.1,2,100), (1/(2*L))*np.sqrt(T/mu))
    },
    "12. LCR Circuit Resonance": {
        "theory": "At resonance, the inductive and capacitive reactances cancel, giving maximum current.",
        "description": "Verify resonance in an LCR circuit.",
        "formula": "f = 1 / (2π√(LC))",
        "inputs": {"Inductance (H)": (0.001,1.0,0.001,0.1), "Capacitance (μF)": (0.1,100.0,0.1,10)},
        "simulate": lambda L,C: (np.linspace(10,1000,200), 1/(2*np.pi*np.sqrt(L*(C*1e-6))))
    },
    "13. Magnetic Field along Axis of Coil": {
        "theory": "The magnetic field at a point on the axis of a coil carrying current is determined using Biot–Savart law.",
        "description": "Calculate magnetic field along coil axis.",
        "formula": "B = (μ₀NIa²) / (2(a² + x²)^(3/2))",
        "inputs": {"Current (A)": (0.1,5.0,0.1,1), "Radius (cm)": (1,10,0.1,5), "Turns (N)": (10,200,1,100)},
        "simulate": lambda I,a,N: (np.linspace(-10,10,200), (4*np.pi*1e-7*N*I*(a**2))/(2*(a**2+np.linspace(-10,10,200)**2)**1.5))
    },
    "14. Determination of e/m by Thomson’s Method": {
        "theory": "Electron charge-to-mass ratio is determined by balancing electric and magnetic forces on electron beam.",
        "description": "Find e/m using deflection method.",
        "formula": "e/m = 2V / (B²r²)",
        "inputs": {"Voltage (V)": (50,500,10,200), "Magnetic field (T)": (0.001,0.01,0.001,0.005), "Radius (cm)": (1,10,1,5)},
        "simulate": lambda V,B,r: (np.linspace(0,10,100), 2*V/(B**2*r**2))
    },
    "15. Semiconductor Diode Characteristics": {
        "theory": "Study V-I characteristics of semiconductor diode in forward and reverse bias.",
        "description": "Plot diode current vs voltage characteristics.",
        "formula": "I = I₀ (exp(qV/kT) - 1)",
        "inputs": {"Voltage (V)": (0,1,0.01,0.5)},
        "simulate": lambda V: (np.linspace(0,1,100), np.exp(np.linspace(0,1,100)*20)-1)
    },
    "16. Determination of Numerical Aperture of Optical Fiber": {
        "theory": "Numerical aperture defines light acceptance angle of an optical fiber.",
        "description": "Find NA using acceptance angle measurement.",
        "formula": "NA = sin(θ)",
        "inputs": {"Acceptance angle (°)": (10,90,1,30)},
        "simulate": lambda theta: (np.linspace(10,90,100), np.sin(np.deg2rad(np.linspace(10,90,100))))
    },
    "17. Study of Thermistor Characteristics": {
        "theory": "Thermistors show resistance changes with temperature, used for sensing and control.",
        "description": "Plot resistance vs temperature characteristics.",
        "formula": "R = R₀ exp(β(1/T - 1/T₀))",
        "inputs": {"Temperature (°C)": (0,100,1,25)},
        "simulate": lambda T: (np.linspace(0,100,100), np.exp(3500*(1/(np.linspace(273,373,100))-1/298)))
    },
}

# --- Sidebar experiment selection ---
st.sidebar.header("🧪 Experiments")
selected_exp = st.sidebar.radio("Select an Experiment:", list(EXPERIMENTS.keys()))

# --- Main area ---
if selected_exp:
    exp = EXPERIMENTS[selected_exp]
    st.header(selected_exp)
    st.subheader("📘 Theory")
    st.write(exp["theory"])
    st.subheader("🧾 Description")
    st.write(exp["description"])
    st.subheader("🧮 Formula")
    st.code(exp["formula"])

    st.subheader("🎛️ Input Parameters")
    inputs = {}
    for label,(min_v,max_v,step,default) in exp["inputs"].items():
        step = safe_step(step, default)
        if isinstance(default,int):
            inputs[label] = st.slider(label,int(min_v),int(max_v),int(default),step=int(step))
        else:
            inputs[label] = st.slider(label,float(min_v),float(max_v),float(default),step=float(step))

    if st.button("🚀 Run Simulation"):
        try:
            params = [inputs[key] for key in exp["inputs"].keys()]
            result = exp["simulate"](*params)
            if len(result) == 3:
                x,y,r = result
                plot_simulation(selected_exp,x,y,r)
                st.success(f"✅ Calculated Result: {r:.4e}")
            else:
                x,y = result
                plot_simulation(selected_exp,x,y)
        except Exception as e:
            st.error(f"⚠️ Simulation error: {e}")
