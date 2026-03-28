
# ML Basics — Learning Machine Learning from First Principles

Welcome!
This repository documents my journey in learning **machine learning from the ground up** — focusing on intuition, math, and from-scratch implementations.

I’m a beginner, so the goal here isn’t perfection or advanced techniques.  
It’s **understanding**. One concept at a time.

If you're also learning, feel free to explore, fork, or suggest improvements!

---

# Repository Structure
ml-basics/
│
├── README.md
│
├── linear-regression/
│   ├── README.md
│   ├── linear_regression_from_scratch.py
│   ├── examples/
│   │   └── simple_demo.py
│   └── notes/
│       └── math_derivation.md
│
└── assets/
└── images/
├── linear_regression_fit.png
├── mse_curve.png
├── gd_bowl.png
├── loss_surface.png
└── gd_step_diagram.png
---

# Goal of This Project

I want to:

- build ML algorithms **from scratch**
- understand *why* things work, not just how to call `sklearn`
- practice clean, simple Python code
- build intuition with diagrams and experiments
- document everything as I learn

This repo is both a study notebook and a personal milestone tracker.

---

# 📘 Completed Concepts

## 1. Linear Regression (from scratch)

- Mean Squared Error (MSE)
- Gradient Descent
- Convex loss surfaces
- Manual parameter updates (no NumPy)
- Visual intuition diagrams
- Math derivations

Folder: `linear-regression/`

---

# Visual Intuition (All Images Below)

### **What Linear Regression Tries to Do**

Fitting a line through noisy data:

assets/images/linear_regression_fit.png

---

### **How the Loss Decreases During Training (MSE Curve)**

Shows gradient descent learning over time:

assets/images/mse_curve.png

---

### **Why Gradient Descent Works — Bowl-Shaped Loss**

A simple picture of descending the error:

assets/images/gd_bowl.png

---

### **Convex Loss Surface of Linear Regression (m vs b)**

There is only **one** global minimum:

assets/images/loss_surface.png

---

### **Step-by-Step Gradient Update Explanation**

A simple overview of the 4-step process:

assets/images/gd_step_diagram.png

---

# 🧩 Code Snippet Example

From the `linear_regression_from_scratch.py`:

```python
model = LinearRegressionScratch(learning_rate=0.01, epochs=2000)
model.fit(x, y)
prediction = model.predict(6)

This is what I plan to explore next:

✔ Linear Regression
☐ Logistic Regression (from scratch)
☐ Gradient Descent variants (SGD, Momentum)
☐ Decision Trees
☐ k‑Nearest Neighbors
☐ Multivariable regression
☐ Implement models with NumPy
☐ Small datasets + visualizations
☐ Intro Neural Networks

As I grow, this repo will grow too.

Machine Learning is deep, beautiful, and mathematical.
I don’t want to skip steps — I want to really understand the fundamentals.
This repo helps me:

slow down
build intuition
stay consistent
and track my progress publicly

Thanks for checking it out!
If you have feedback or suggestions, I’d love to hear them.