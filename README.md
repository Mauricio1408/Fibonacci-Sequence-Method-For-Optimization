# 📉 Fibonacci Search Method (FSM) Optimization Tool

### CCS 239 - Optimization Theory and Application | Final Term Project

## 📖 Project Overview

This application is an interactive decision-support tool designed to demonstrate the **Fibonacci Search Method**, a derivative-free optimization algorithm. The tool allows users to find the minimum of unimodal functions (polynomials and transcendental functions) within a specified interval without manual calculation.

Developed as a requirement for **CCS 239**, this project focuses on automating the iterative process of optimization while providing clear visual and tabular insights.

## 👥 Team Members

**Section:** BSCS 4 - A AI

  * **Mauricio Manuel F. Bergancia**
  * **Mherlie Joy U. Chavez**
  * **Michael Rey T. Tuando**

-----

## ✅ Compliance with Project Criteria

This application has been developed to strictly adhere to the requirements outlined in the **CCS 239 Final Term Project Guidelines**. Below is a checklist of the satisfied criteria:

| Criteria Category | Requirement [Source PDF] | Implementation Status |
| :--- | :--- | :--- |
| **Method Selection** | Implement one chosen method (Fibonacci Search Method). | ✅ **Implemented** a custom Python solver for FSM. |
| **Platform** | Develop using Python via Streamlit, Tkinter, etc. | ✅ **Implemented** using Streamlit web framework. |
| **Input Flexibility** | Input polynomial functions ($a_nx^n...$) and expressions like $\sin(x), \cos(x), e^x$. | ✅ **Supported:** Accepts arbitrary math strings including polynomials and NumPy functions. |
| **Input Parameters** | Specify left/right endpoints ($a, b$) and Tolerance ($e$). | ✅ **Included** input fields for interval boundaries and customizable tolerance. |
| **Results: Iterations** | Compute and display the number of iterations within tolerance. | ✅ **Displayed** as a primary metric card in the results section. |
| **Results: Minimizer** | Compute and display the approximate root or minimizer. | ✅ **Calculated** and displayed with high precision (up to 6 decimal places). |
| **Results: Tabular** | Display a table with values from each iteration (intervals, function values). | ✅ **Included** a Pandas DataFrame showing $a, b, x_1, x_2, f(x_1), f(x_2)$ per step. |
| **Graphical Output** | Graphically display the function and the root/minimizer. | ✅ **Visualized** using Matplotlib, marking the function curve and the calculated minimum point. |
| **User Interface** | User-friendly, visually appealing, and functional layout. | ✅ **Designed** with a "Notion-style" sidebar, consistent iconography, and aesthetic headers. |

-----

## 🚀 Features

### 1\. Custom FSM Solver

Unlike generic libraries, this project features a **custom-built Python algorithm** that manually calculates Fibonacci ratios and reduces intervals step-by-step, ensuring full transparency in the logic.

### 2\. Interactive Playground

  * **Dynamic Inputs:** Users can type equations directly (e.g., `x**2 - 4*x + 4` or `sin(x) + x`).
  * **Real-time Validation:** Prevents errors such as $a > b$.

### 3\. Comprehensive Visualization

  * **Plotting:** Auto-generates a graph of the function over the search interval.
  * **Indicators:** Visually marks the initial interval bounds and the final calculated minimum.

### 4\. Data Export & Reporting

  * **📄 CSV Download:** Users can download the full iteration history table.
  * **📝 Text Report:** Generates a summary text file with initial parameters and final results.
  * **📊 PDF Plot:** Allows users to download the high-quality optimization graph.

### 5\. Educational Resources

  * **Video Embed:** Includes an embedded tutorial video explaining the concepts of FSM.
  * **Methodology Page:** Explains the algorithmic logic and steps used by the solver.

-----

## 🛠️ Installation & Usage

### Prerequisites

Ensure you have Python installed. You will need the following libraries:

```bash
pip install streamlit numpy pandas matplotlib
```

### Running the Application

1.  Clone this repository or download the source code.
2.  Navigate to the project directory in your terminal.
3.  Run the Streamlit app:

<!-- end list -->

```bash
streamlit run app.py
```

4.  The application will open automatically in your default web browser (usually at `http://localhost:8501`).

-----

## 📂 Project Structure

```text
FSM_Project/
├── app.py                # Main application code containing UI and Solver logic
├── README.md             # Project documentation
└── requirements.txt      # List of dependencies
```

-----

## 🎓 Acknowledgments

**Subject:** CCS 239 - Optimization Theory and Application  
**Instructor:** John Alexis B. Gemino, M.A.  
**Date:** December 2025  
**College:** College of Arts and Sciences
