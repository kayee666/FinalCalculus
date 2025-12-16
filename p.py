import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import re

# Set page config for theme
st.set_page_config(
    page_title="Calculus Explorer",
    page_icon="🧮",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for colorful calculus theme
st.markdown("""
<style>
    /* APP CONTAINER */
    [data-testid="stApp"] {
        background-color: #f0ffff !important;
    }

    /* MAIN CONTENT AREA */
    [data-testid="stAppViewContainer"] {
        background-color: #b9f2ff !important;
    }

    /* BLOCK CONTAINER */
    [data-testid="stVerticalBlock"] {
        background-color: #b9f2ff !important;
    }

    /* BODY fallback */
    body {
        background-color: #f0ffff !important;
    }

    /* SIDEBAR */
    section[data-testid="stSidebar"] {
        background-color: #f0ffff !important;
    }

    section[data-testid="stSidebar"] * {
        background-color: #b9f2ff !important;
    }

    /* BUTTON */
    .stButton>button {
        background: linear-gradient(45deg, #ff6b6b, #4ecdc4);
        color: #ffcba4;
        border-radius: 10px;
        border: none;
    }

    /* INPUT */
    .stTextInput input,
    .stSelectbox select {
        background: rgba(255,255,255,0.9);
        color: #ffcba4;
        border-radius: 10px;
    }

    /* HEADERS */
    h1, h2, h3 {
        color: #f0ffff;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }

    /* CARD */
    .card {
        background-color: #ffcba4 !important;
        padding: 20px;
        border-radius: 15px;
        margin-bottom: 20px;
        box-shadow: 0 8px 32px rgba(0,0,0,0.3);
    }
</style>
""", unsafe_allow_html=True)

# Language selection
lang = st.sidebar.selectbox("Language", ["English", "Indonesia"])

# Text dictionaries for localization
texts = {
    "English": {
        "title": "🧮 Calculus Explorer",
        "subtitle": "Dive into the vibrant world of derivatives, integrals, and optimizations!",
        "function_input": "Enter a function of x (e.g., lambda x: x**2 + 3*x + 1):",
        "plot_button": "Plot 2D Function",
        "derivative_button": "Compute and Plot Derivative",
        "3d_button": "Plot 3D Surface",
        "3d_input": "Enter a 3D function of x and y (e.g., lambda x, y: x**2 + y**2):",
        "surface_select": "Choose a surface:",
        "surfaces": ["x² + y²", "sin(x) + cos(y)", "x · y"],
        "opt_title": "Optimization Problems",
        "opt_select": "Select a problem:",
        "story_input": "Enter a story-based problem (e.g., 'Maximize the area of a rectangle with perimeter 20.'):",
        "solve_story_button": "Solve Story-Based Problem",
        "members_title": "Our Calculus Enthusiasts",
        "members": [
            {"name": "Rizki Adiputra", "image": "ki.jpg", "role": "Leader"},
            {"name": "Nailah Nurramadhanti", "image": "sayang.jpg", "role": "Member"},
            {"name": "Suci Khadijah Siregar", "image": "suci.jpg", "role": "Member"},
            {"name": "Salsabila Cantika", "image": "cantika.jpg", "role": "Member"}
        ],
        "problems": {
            "area": "Maximize area of a rectangle with fixed perimeter.",
            "perimeter": "Minimize perimeter for fixed area.",
            "volume": "Maximize volume of a box with fixed surface area.",
            "profit": "Maximize profit for a product."
        }
    },
    "Indonesia": {
        "title": "🧮 Penjelajah Kalkulus",
        "subtitle": "Jelajahi dunia turunan, integral, dan optimasi yang berwarna!",
        "function_input": "Masukkan fungsi dari x (contoh: lambda x: x**2 + 3*x + 1):",
        "plot_button": "Plot Fungsi 2D",
        "derivative_button": "Hitung dan Plot Turunan",
        "3d_button": "Plot Permukaan 3D",
        "3d_input": "Masukkan fungsi 3D dari x dan y (contoh: lambda x, y: x**2 + y**2):",
        "surface_select": "Pilih permukaan:",
        "surfaces": ["x² + y²", "sin(x) + cos(y)", "x · y"],
        "opt_title": "Masalah Optimasi",
        "opt_select": "Pilih masalah:",
        "story_input": "Masukkan masalah berbasis cerita (contoh: 'Maksimalkan luas persegi panjang dengan keliling 20.'):",
        "solve_story_button": "Selesaikan Masalah Berbasis Cerita",
        "members_title": "Penggemar Kalkulus Kami",
        "members": [
            {"name": "Rizki Adiputra", "image": "https://via.placeholder.com/60x60?text=KI", "role": "Leader"},
            {"name": "Nailah Nurramadhanti", "image": "https://via.placeholder.com/60x60?text=NAILAH", "role": "Member"},
            {"name": "Suci Khadijah Siregar", "image": "https://via.placeholder.com/60x60?text=SUCI", "role": "Member"},
            {"name": "Salsabila Cantika", "image": "https://via.placeholder.com/60x60?text=CANTIKA", "role": "Member"}
        ],
        "problems": {
            "area": "Maksimalkan luas persegi panjang dengan keliling tetap.",
            "perimeter": "Minimalkan keliling untuk luas tetap.",
            "volume": "Maksimalkan volume kotak dengan luas permukaan tetap.",
            "profit": "Maksimalkan keuntungan untuk produk."
        }
    }
}

# Get current language texts
current_texts = texts[lang]

# Sidebar: Our Members section with calculus theme and cat gif
with st.sidebar.expander(current_texts["members_title"] + " 🧠"):
    # Add a cat gif at the top
    st.markdown('<div class="gif-container"><img src="https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif" width="200" alt="Cute Cat Animation"></div>', unsafe_allow_html=True)
    st.markdown("---")
    for member in current_texts["members"]:
        col1, col2 = st.columns([1, 3])
        with col1:
            try:
                st.image(member["image"], width=60)
            except Exception as e:
                st.error(f"Image for {member['name']} could not be loaded.")
        with col2:
            st.markdown(f"**{member['name']}**<br>{member['role']}", unsafe_allow_html=True)
        st.markdown("---")

# Main title and subtitle
st.title(current_texts["title"])
st.markdown(current_texts["subtitle"])

# Function to plot 2D function
def plot_2d_function(func_str):
    try:
        func = eval(func_str)
        x_vals = np.linspace(-10, 10, 400)
        y_vals = func(x_vals)
        fig, ax = plt.subplots(figsize=(8, 5))
        ax.plot(x_vals, y_vals, color='#ffd700', linewidth=3)
        ax.fill_between(x_vals, y_vals, alpha=0.5, color='#ff6b6b')
        ax.set_xlabel('x', fontsize=12, color='white')
        ax.set_ylabel('f(x)', fontsize=12, color='white')
        ax.set_title('2D Plot of Function', fontsize=14, color='#ffd700')
        ax.grid(True, alpha=0.5, color='white')
        ax.set_facecolor((0, 0, 0, 0.1))
        st.pyplot(fig)
    except Exception as e:
        st.error(f"Error plotting function: {e}")

# Function to plot derivative
def plot_derivative(func_str):
    try:
        func = eval(func_str)
        x_vals = np.linspace(-10, 10, 400)
        y_vals = func(x_vals)
        deriv_vals = np.gradient(y_vals, x_vals)
        fig, ax = plt.subplots(figsize=(8, 5))
        ax.plot(x_vals, deriv_vals, color='#4ecdc4', linewidth=3)
        ax.fill_between(x_vals, deriv_vals, alpha=0.5, color='#45b7d1')
        ax.set_xlabel('x', fontsize=12, color='white')
        ax.set_ylabel("f'(x)", fontsize=12, color='white')
        ax.set_title('2D Plot of Numerical Derivative', fontsize=14, color='#4ecdc4')
        ax.grid(True, alpha=0.5, color='white')
        ax.set_facecolor((0, 0, 0, 0.1))
        st.pyplot(fig)
        st.info("Note: This is a numerical approximation of the derivative using calculus principles.")
    except Exception as e:
        st.error(f"Error plotting derivative: {e}")

# Function to plot 3D surface
def plot_3d_surface(surface_type):
    x = np.linspace(-5, 5, 50)
    y = np.linspace(-5, 5, 50)
    X, Y = np.meshgrid(x, y)
    
    if surface_type == "x² + y²":
        Z = X**2 + Y**2
    elif surface_type == "sin(x) + cos(y)":
        Z = np.sin(X) + np.cos(Y)
    else:  # "x · y"
        Z = X * Y
    
    fig = plt.figure(figsize=(7, 5))
    ax = fig.add_subplot(111, projection="3d")
    ax.plot_surface(X, Y, Z, cmap="viridis", edgecolor="none")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    ax.set_title("3D Surface Plot")
    st.pyplot(fig)

# Function to analyze story-based problem
def analyze_problem(text, lang):
    text_lower = text.lower()
    numbers = re.findall(r'\d+', text)
    param = float(numbers[0]) if numbers else None
    
    if lang == "English":
        if "area" in text_lower and ("maximize" in text_lower or "maximum" in text_lower):
            return "area", param
        elif "perimeter" in text_lower and ("minimize" in text_lower or "minimum" in text_lower):
            return "perimeter", param
        elif "volume" in text_lower and ("maximize" in text_lower or "maximum" in text_lower):
            return "volume", param
        elif "profit" in text_lower and ("maximize" in text_lower or "maximum" in text_lower):
            return "profit", param
    elif lang == "Indonesia":
        if "luas" in text_lower and ("maksimalkan" in text_lower or "maksimum" in text_lower):
            return "area", param
        elif "keliling" in text_lower and ("minimalkan" in text_lower or "minimum" in text_lower):
            return "perimeter", param
        elif "volume" in text_lower and ("maksimalkan" in text_lower or "maksimum" in text_lower):
            return "volume", param
        elif "keuntungan" in text_lower and ("maksimalkan" in text_lower or "maksimum" in text_lower):
            return "profit", param
    return None, None

# Function to handle optimization problems
def solve_optimization(problem, param=None, lang=None):
    if problem == "area":
        P = param if param else st.number_input("P (Perimeter)", value=20.0)
        x_opt = P / 4
        y_opt = P / 4
        A_max = x_opt * y_opt
        st.success(f"Optimal x: {x_opt}, y: {y_opt}, Max Area: {A_max}")
    elif problem == "perimeter":
        A = param if param else st.number_input("A (Area)", value=100.0)
        x_opt = np.sqrt(A)
        y_opt = A / x_opt
        P_min = 2 * x_opt + 2 * y_opt
        st.success(f"Optimal x: {x_opt}, y: {y_opt}, Min Perimeter: {P_min}")
    elif problem == "volume":
        S = param if param else st.number_input("S (Surface Area)", value=24.0)
        x_opt = np.sqrt(S / 6)
        V_max = x_opt ** 3
        st.success(f"Optimal x=y=z: {x_opt}, Max Volume: {V_max}")
    elif problem == "profit":
        x_opt = 500
        P_max = 100 * 500 - 0.1 * 500 ** 2 - 50
        st.success(f"Optimal x: {x_opt}, Max Profit: {P_max}")

# 2D Function Plotting Section
st.markdown('<div class="card">', unsafe_allow_html=True)
st.header("📈 2D Function Plotting")
func_str = st.text_input(current_texts["function_input"], "lambda x: x**2")
if st.button(current_texts["plot_button"]):
    plot_2d_function(func_str)
st.markdown('</div>', unsafe_allow_html=True)

# Derivative Plotting Section
st.markdown('<div class="card">', unsafe_allow_html=True)
st.header("📉 Derivative Plotting")
if st.button(current_texts["derivative_button"]):
    plot_derivative(func_str)
st.markdown('</div>', unsafe_allow_html=True)

# 3D Surface Plotting Section
st.markdown('<div class="card">', unsafe_allow_html=True)
st.header("🌐 3D Surface Plotting")
surface_type = st.selectbox(current_texts["surface_select"], current_texts["surfaces"])
plot_3d_surface(surface_type)
st.markdown('</div>', unsafe_allow_html=True)

# Optimization Section
st.markdown('<div class="card">', unsafe_allow_html=True)
st.header("⚖ " + current_texts["opt_title"])

# Option to choose between predefined or story-based
opt_type = st.radio("Choose optimization type:", ["Predefined Problem", "Story-Based Problem"])

if opt_type == "Predefined Problem":
    problem = st.selectbox(current_texts["opt_select"], list(current_texts["problems"].keys()), format_func=lambda x: current_texts["problems"][x])
    solve_optimization(problem, lang=lang)
elif opt_type == "Story-Based Problem":
    story_text = st.text_area(current_texts["story_input"], "")
    if st.button(current_texts["solve_story_button"]):
        problem_type, param = analyze_problem(story_text, lang)
        if problem_type:
            solve_optimization(problem_type, param=param, lang=lang)
        else:
            st.error("Unable to analyze the problem. Please ensure it involves area, perimeter, volume, or profit with a clear maximize/minimize intent and a numeric parameter.")

st.markdown('</div>', unsafe_allow_html=True)
