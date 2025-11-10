# 🔬 Engineering Physics Virtual Lab

This project is a web-based virtual laboratory for Engineering Physics experiments, built using Python and Streamlit. It provides an interactive platform for students and enthusiasts to simulate various physics phenomena, visualize the results, and understand the underlying principles and formulas.

![Physics Lab Demo](https://i.imgur.com/your-demo-image.gif)  <!-- It's recommended to replace this with a GIF of your running application -->

## ✨ Features

*   **Interactive UI**: A modern, dark-themed interface built with Streamlit.
*   **17 Physics Experiments**: A comprehensive collection of common engineering physics experiments.
*   **Detailed Information**: Each experiment includes:
    *   📘 **Theory**: A brief explanation of the underlying physics principles.
    *   🧾 **Description**: The objective of the experiment.
    *   🧮 **Formula**: The key mathematical formula used for calculations.
*   **Dynamic Simulations**:
    *   Adjustable input parameters using interactive sliders.
    *   Real-time simulation and data visualization with Matplotlib.
    *   Calculation of final results where applicable.

## 🧪 Experiments Included

1.  Radius of Curvature by Newton's Rings
2.  Wavelengths of Mercury Spectrum
3.  Verification of Brewster's Law
4.  Wavelength of Laser Light using Diffraction Grating
5.  Estimation of Planck's Constant
6.  Energy Band Gap of Semiconductor
7.  Solar Cell Characteristics
8.  Diffraction of Light through Slit
9.  Hall Effect Experiment
10. Ultrasonic Diffraction
11. Melde’s String Experiment
12. LCR Circuit Resonance
13. Magnetic Field along Axis of Coil
14. Determination of e/m by Thomson’s Method
15. Semiconductor Diode Characteristics
16. Determination of Numerical Aperture of Optical Fiber
17. Study of Thermistor Characteristics

## 🛠️ Technologies Used

*   **Python**: Core programming language.
*   **Streamlit**: For creating the interactive web application.
*   **NumPy**: For numerical operations and simulations.
*   **Matplotlib**: For plotting and visualizing data.

## 🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

*   Python 3.7+
*   `pip` (Python package installer)

### Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name
    ```

2.  **Create and activate a virtual environment (recommended):**
    *   On macOS and Linux:
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```
    *   On Windows:
        ```bash
        python -m venv venv
        .\venv\Scripts\activate
        ```

3.  **Install the required dependencies:**
    Create a `requirements.txt` file with the following content:
    ```
    streamlit
    numpy
    matplotlib
    ```
    Then, run the following command to install them:
    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

1.  Ensure you are in the project directory and your virtual environment is activated.

2.  Run the Streamlit application using the following command (replace `physics_lab.py` with your script name if different):
    ```bash
    streamlit run physics_lab.py
    ```

3.  Open your web browser and navigate to the local URL provided by Streamlit (usually `http://localhost:8501`).

---

Feel free to contribute to this project by submitting issues or pull requests.

