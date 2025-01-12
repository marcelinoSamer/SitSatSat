# SitSatSat 🌟

This project explores the use of **Quantum Annealing** to solve the classic **3SAT** problem. The aim is to maximize the number of satisfied clauses in a given **Boolean formula** using **D-Wave's quantum annealer** (via their Ocean SDK) and **SimulatedAnnealingSampler** for optimization.

🎯 **Project Goal**: Solve 3SAT instances with quantum annealing techniques to optimize the truth assignments that maximize the number of satisfied clauses.

---

## 📚 Table of Contents

- [Project Overview](#project-overview)
- [Installation & Setup](#installation--setup)
- [Usage Instructions](#usage-instructions)
- [How It Works](#how-it-works)
- [Results and Analysis](#results-and-analysis)
- [Visualization of Results](#visualization-of-results)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

---

## 💡 Project Overview

### Project Description:
- **Objective**: Solve the **3SAT** problem using **quantum annealing** and **optimization** techniques.
- **Key Technologies**: **D-Wave Quantum Annealing**, **SimulatedAnnealingSampler**, **QUBO Formulation**.

### Features:
- Maximize the number of satisfied clauses in a 3SAT problem.
- Use quantum computing to solve **NP-complete** problems in an efficient manner.

### Expected Results:
- **Optimal Assignment**: The solution that satisfies the maximum number of clauses.
- **Energy Calculation**: The "energy" of each configuration.
- **Visual Data**: Insights into the solution process and results.

---

## 🛠️ Installation & Setup

### Prerequisites:
Before running the project, make sure you have the following installed:
- **Python 3.x**
- Required libraries: `dimod`, `dwave-ocean-sdk`

### Installation Steps:

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/your-username/quantum-annealing-3SAT.git
    cd quantum-annealing-3SAT
    ```

2. **Install Dependencies**:
    ```bash
    pip install dimod
    pip install dwave-ocean-sdk
    ```

3. **Create a D-Wave Account**:
   - Go to [D-Wave Leap](https://cloud.dwavesys.com/leap/) and sign up.
   - Obtain your **API token** from the D-Wave console.

4. **Set Up Your API Token**:
    ```bash
    export DWAVE_API_TOKEN="your-api-token"
    ```

---

## 🚀 Usage Instructions

### Prepare the 3SAT Formula:
- **Input Format**: Represent the Boolean formula in a standard form (e.g., `(x1 OR x2 OR NOT x3) AND (NOT x1 OR x3 OR x4)`).

### Running the Code:
1. Navigate to the project folder in the terminal.
2. Run the main script to solve the 3SAT problem:
    ```bash
    python main.py
    ```

3. The output will include:
    - The optimal binary assignments for the variables.
    - The total number of satisfied clauses.
    - Visualization results (optional).

---

## 🔍 How It Works

### Problem Transformation:
1. Convert the **3SAT problem** to a **QUBO model**.
2. Define a **quadratic objective function** based on the Boolean formula.
3. Assign a binary variable for each clause in the formula.

### Quantum Annealing Optimization:
- **Optimization Goal**: Find the assignment of binary variables that maximizes the number of satisfied clauses.
- **Quantum Annealing** is used to explore the solution space and search for an optimal solution.

### Classical vs. Quantum Optimization:
- While classical methods involve exhaustive search, quantum annealing uses probabilistic techniques for faster exploration of the solution space.

---

## 📊 Results and Analysis

### Example 1: Small 3SAT Instance
- **Formula**: `(x1 OR x2 OR NOT x3) AND (NOT x1 OR x3 OR x4)`
- **Variables**: 4
- **Clauses**: 2
- **Maximum Clauses Satisfied**: 2

### Example 2: Larger 3SAT Instance
- **Formula**: `((x1 OR x2 OR x3) AND (NOT x2 OR x3 OR x4) AND (x4 OR x5 OR NOT x1))`
- **Variables**: 5
- **Clauses**: 3
- **Maximum Clauses Satisfied**: 3

### Performance:
- **Time Taken**: Insert time taken for solving problems.
- **Energy Calculations**: Insert analysis on how the energy varied with different formulations.

---

## 💡 Visualization of Results

### Energy of Solutions:
- Insert chart that visualizes the energy levels of different solutions.

    ![Energy Graph](https://via.placeholder.com/500x300?text=Energy+Graph)

### Variable Assignment Frequency:
- Insert graph that shows how often each variable is assigned a particular value across all solutions.

    ![Variable Frequency](https://via.placeholder.com/500x300?text=Variable+Frequency)

---

## 🤝 Contributing

We welcome contributions from the open-source community! If you'd like to help improve this project, here’s how to contribute:

### Steps:
1. **Fork** the repository on GitHub.
2. Create a **new branch** to make your changes.
3. **Commit** your changes and push them to your fork.
4. Open a **pull request** for review.

---

## 📝 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for more details.

---

## 🌟 Acknowledgments

- **D-Wave Systems**: Thanks for providing the quantum hardware and access to their Leap platform.
- This project was part of the **Quantum Computing Contest 2025**.

---

### 💬 Questions or Feedback?

If you have any questions, suggestions, or issues, feel free to [open an issue](https://github.com/your-username/quantum-annealing-3SAT/issues) on GitHub.

---

**Happy Coding and Quantum Computing!** ✨
