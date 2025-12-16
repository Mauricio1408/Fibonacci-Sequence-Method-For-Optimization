import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import io

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="FSM Optimization Tool",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CUSTOM CSS FOR STYLING & 4:1 HEADER ---
st.markdown("""
<style>
    /* Sidebar Navigation Button Styling */
    div[data-testid="stSidebar"] button {
        width: 100%;
        text-align: left;
        border: none;
        background-color: transparent;
        color: inherit;
        padding: 12px;
        font-size: 16px;
        font-weight: 500;
        transition: background-color 0.3s;
    }
    div[data-testid="stSidebar"] button:hover {
        background-color: #f0f2f6;
        border-radius: 8px;
    }
    
    /* Header Image Styling (4:1 Aspect Ratio) */
    .header-img-container {
        width: 100%;
        height: 200px; /* Fixed height for consistency */
        overflow: hidden;
        border-radius: 12px;
        margin-bottom: 25px;
        position: relative;
    }
    .header-img-container img {
        width: 100%;
        height: 100%;
        object-fit: cover; /* This forces the 4:1 crop */
        object-position: center;
    }
</style>
""", unsafe_allow_html=True)

# --- SESSION STATE NAVIGATION ---
if 'page' not in st.session_state:
    st.session_state['page'] = 'Title Page'

def navigate_to(page_name):
    st.session_state['page'] = page_name

# --- HELPER: RENDER HEADER IMAGE ---
def render_header_image(url):
    st.markdown(f"""
    <div class="header-img-container">
        <img src="{url}" alt="Page Header">
    </div>
    """, unsafe_allow_html=True)

# --- CUSTOM SOLVER IMPLEMENTATION ---
def solver_fibonacci_search(func_str, a, b, tol):
    """
    Performs Fibonacci Search to find the minimum of a function.
    Returns: (minimizer_x, minimum_val, history_dataframe, num_iterations, report_text)
    """
    
    # Safety wrapper for eval
    def f(x):
        allowed_names = {"abs": abs, "min": min, "max": max, "pow": pow, 
                         "np": np, "sin": np.sin, "cos": np.cos, 
                         "exp": np.exp, "log": np.log, "sqrt": np.sqrt}
        try:
            return eval(func_str, {"__builtins__": {}}, allowed_names | {"x": x})
        except Exception:
            return None

    # Algorithm Init
    L_initial = b - a
    fibs = [1, 1]
    
    # Generate Fibonacci numbers until inequality is met
    # Inequality: F_n > (b - a) / tol
    while fibs[-1] <= L_initial / tol:
        fibs.append(fibs[-1] + fibs[-2])
    
    n = len(fibs) - 1
    L = b - a
    
    # Initial Ratios
    # x1 = a + (F_n-2 / F_n) * L
    x1 = a + (fibs[n - 2] / fibs[n]) * L
    x2 = a + (fibs[n - 1] / fibs[n]) * L
    
    f1 = f(x1)
    f2 = f(x2)
    
    history = []

    # Iteration Loop
    # We iterate until k = n - 1
    for k in range(1, n):
        history.append({
            "Iter": k,
            "a": a,
            "b": b,
            "x1": x1,
            "x2": x2,
            "f(x1)": f1,
            "f(x2)": f2,
            "L (Interval)": b - a
        })

        # Logic to narrow interval
        if f1 < f2:
            b = x2
            x2 = x1
            f2 = f1
            # Check to prevent index error at end of loop
            if (n - k - 1) < 0: break 
            
            x1 = a + (fibs[n - k - 2] / fibs[n - k]) * (b - a)
            f1 = f(x1)
        else:
            a = x1
            x1 = x2
            f1 = f2
            if (n - k - 1) < 0: break
            
            x2 = a + (fibs[n - k - 1] / fibs[n - k]) * (b - a)
            f2 = f(x2)

    if f1 < f2:
        best_x = x1
        best_y = f1
    else:
        best_x = x2
        best_y = f2
    
    # Generate Text Report
    report = f"""
    FIBONACCI SEARCH METHOD - EXECUTION REPORT
    ==========================================
    Function: {func_str}
    Initial Interval: [{history[0]['a']}, {history[0]['b']}]
    Tolerance: {tol}
    
    RESULTS
    -------
    Total Iterations: {n}
    Converged Interval: [{a:.8f}, {b:.8f}]
    Approximate Minimizer (x): {best_x:.8f}
    Minimum Value f(x): {best_y:.8f}
    
    Final Interval Width: {b-a:.8f}
    """

    return best_x, best_y, pd.DataFrame(history), n, report

# --- SIDEBAR UI ---
with st.sidebar:
    st.title("📂 Navigation")
    st.markdown("---")
    
    # Consistent Icons for Navigation
    if st.button("🏠  Title Page"): navigate_to("Title Page")
    if st.button("📖  Introduction"): navigate_to("Introduction")
    if st.button("⚙️  Methodology"): navigate_to("Methodology")
    if st.button("💻  Implementation"): navigate_to("Implementation")
    if st.button("🏆  Thank You"): navigate_to("Thank You")
    
    st.markdown("---")
    st.caption("FSM Project • Dec 2025")

# --- PAGE ROUTING ---
page = st.session_state['page']

# 1. TITLE PAGE
if page == "Title Page":
    render_header_image("https://images.unsplash.com/photo-1636466497217-26a8cbeaf0aa?q=80&w=1374&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D")
    
    st.markdown("<div style='text-align: center; margin-top: 20px;'>", unsafe_allow_html=True)
    st.title("Fibonacci Search Method for Optimization")
    st.subheader("An Interactive Solver for CCS 239")
    st.write("---")
    
    st.write("**Submitted by:**")
    st.write("Mauricio Manuel F. Bergancia • Mherlie Joy U. Chavez • Michael Rey T. Tuando")
    
    st.write("") 
    st.write("**Section:** BSCS 4 - A AI")
    st.write("**Date:** December 2025")
    
    st.write("---")
    st.write("Prepared for:")
    st.markdown("#### CCS 239 - Optimization Theory and Application")
    st.markdown("</div>", unsafe_allow_html=True)

# 2. INTRODUCTION
elif page == "Introduction":
    render_header_image("https://plus.unsplash.com/premium_photo-1666583590174-1da9a2def2f9?q=80&w=1632&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D")
    
    st.title("Introduction")
    st.info("Goal: To implement a custom solver for the Fibonacci Search Method.")
    
    # VIDEO EMBED (Updated Link)
    st.markdown("### 🎥 How It Works")
    st.video("https://youtu.be/2tv6Ej6JVho?si=7JisgixUdNTfr9mJ") 
    
    st.markdown("### What is the Fibonacci Search Method?")
    st.write("""
    The **Fibonacci Search Method** is a comparison-based optimization algorithm used to find the minimum (or maximum) of a unimodal function.
    It uses the **Fibonacci sequence** (1, 1, 2, 3, 5, 8...) to systematically narrow down the search interval.
    
    Unlike the Golden Section Search which uses a constant ratio, FSM adjusts its ratio at every step, making it the most efficient method 
    for a fixed number of function evaluations.
    """)

# 3. METHODOLOGY
elif page == "Methodology":
    render_header_image("https://images.unsplash.com/photo-1711075781376-bc5107736730?q=80&w=1470&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D")

    st.title("Methodology")
    
    col1, col2 = st.columns([1, 1])
    with col1:
        st.subheader("Algorithm Logic")
        st.markdown("""
        1.  **Define Inputs**: $f(x)$, $[a, b]$, and $\epsilon$ (tolerance).
        2.  **Determine $n$**: Find the smallest Fibonacci number $F_n$ such that $F_n > (b-a)/\epsilon$.
        3.  **Place Probes**: Calculate points $x_1$ and $x_2$ using Fibonacci ratios $F_{n-2}/F_n$ and $F_{n-1}/F_n$.
        4.  **Reduce Interval**:
            * If $f(x_1) < f(x_2)$: New interval is $[a, x_2]$.
            * If $f(x_1) > f(x_2)$: New interval is $[x_1, b]$.
        5.  **Repeat**: Update ratios and points until $n$ iterations are complete.
        """)
    with col2:
        st.subheader("Tech Stack")
        st.success("**Python 3.10+** - Core Logic")
        st.warning("**Streamlit** - User Interface")
        st.info("**Matplotlib** - Visualization")
        st.error("**Pandas** - Data Tables")

# 4. IMPLEMENTATION (PLAYGROUND)
elif page == "Implementation":
    render_header_image("https://images.unsplash.com/photo-1653926381713-8ef07485724e?q=80&w=1512&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D")
    
    st.title("Implementation Playground")
    st.write("Enter your parameters below to run the solver.")

    # 1. Input Fields
    col1, col2 = st.columns(2)
    with col1:
        func_input = st.text_input("Enter Function f(x)", value="x**2 - 4*x + 4")
        st.caption("Try: `x**2 + 2*x`, `sin(x)`, `exp(x) - 2*x`.")
    
    with col2:
        # Default tolerance increased to 1e-5 to ensure >20 iterations
        tolerance = st.number_input("Tolerance Level", value=0.00001, format="%.6f", step=0.00001)
        
    c1, c2 = st.columns(2)
    with c1:
        a_input = st.number_input("Left Endpoint (a)", value=0.0)
    with c2:
        b_input = st.number_input("Right Endpoint (b)", value=5.0)

    if st.button("Run Fibonacci Search"):
        if a_input >= b_input:
            st.error("Error: 'a' must be less than 'b'.")
        else:
            try:
                # CALLING CUSTOM SOLVER
                minimizer, min_val, df_history, n_iters, report_txt = solver_fibonacci_search(
                    func_input, a_input, b_input, tolerance
                )
                
                # 2. Results Generation
                st.markdown("### Optimization Results")
                
                m1, m2, m3 = st.columns(3)
                m1.metric("Iterations Run", n_iters)
                m2.metric("Minimizer (x)", f"{minimizer:.6f}")
                m3.metric("Minimum Value f(x)", f"{min_val:.6f}")

                # 3. Graphical Output
                st.subheader("Function Visualization")
                
                x_plot = np.linspace(a_input - 1, b_input + 1, 400)
                y_plot = []
                for x_val in x_plot:
                    try:
                        y_val = eval(func_input, {"__builtins__": {}}, 
                                     {"x": x_val, "sin": np.sin, "cos": np.cos, "exp": np.exp, "np": np})
                        y_plot.append(y_val)
                    except:
                        y_plot.append(np.nan)

                fig, ax = plt.subplots(figsize=(10, 4))
                ax.plot(x_plot, y_plot, label=f"f(x)={func_input}", color="#2E86C1", linewidth=2)
                ax.axvline(a_input, color="gray", linestyle="--", alpha=0.5, label="Start Interval")
                ax.axvline(b_input, color="gray", linestyle="--", alpha=0.5)
                ax.scatter([minimizer], [min_val], color="#E74C3C", s=100, zorder=5, label="Calculated Minimum")
                
                ax.set_title(f"Optimization of {func_input}")
                ax.set_xlabel("x")
                ax.set_ylabel("f(x)")
                ax.legend()
                ax.grid(True, alpha=0.3)
                st.pyplot(fig)
                
                # 4. Table Display
                st.subheader("Iteration History Table")
                st.write(f"Displaying all **{len(df_history)}** iterations.")
                st.dataframe(df_history.style.format("{:.6f}"), use_container_width=True)

                # 5. DOWNLOAD SECTION
                st.markdown("---")
                st.subheader("📥 Download Report & Data")
                d_col1, d_col2, d_col3 = st.columns(3)
                
                # CSV Download
                csv = df_history.to_csv(index=False).encode('utf-8')
                d_col1.download_button(
                    label="📄 Download CSV Data",
                    data=csv,
                    file_name='fsm_iteration_history.csv',
                    mime='text/csv',
                )
                
                # Report Download
                d_col2.download_button(
                    label="📝 Download Text Report",
                    data=report_txt,
                    file_name='fsm_analysis_report.txt',
                    mime='text/plain'
                )
                
                # Plot PDF Download
                img_buffer = io.BytesIO()
                fig.savefig(img_buffer, format='pdf')
                img_buffer.seek(0)
                
                d_col3.download_button(
                    label="📊 Download Plot (PDF)",
                    data=img_buffer,
                    file_name="fsm_visualization.pdf",
                    mime="application/pdf"
                )

            except Exception as e:
                st.error(f"An error occurred. Please check your syntax. Error: {e}")

# 5. THANK YOU PAGE
elif page == "Thank You":
    render_header_image("https://images.unsplash.com/photo-1635372722656-389f87a941b7?q=80&w=1631&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D")
    
    st.markdown("<div style='text-align: center; margin-top: 50px;'>", unsafe_allow_html=True)
    st.header("Thank You!")
    st.write("We appreciate you using our Fibonacci Search Method application.")
    st.write("Created for **CCS 239 - Optimization Theory**")
    
    st.success("End of Application")
    st.balloons()
    st.markdown("</div>", unsafe_allow_html=True)