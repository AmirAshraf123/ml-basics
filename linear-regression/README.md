
 Linear Regression — From Scratch

This module implements **simple linear regression** without using NumPy, scikit-learn, or any ML frameworks.

The purpose is to learn:

- what a loss function is  
- how gradient descent finds better parameters  
- why linear models behave the way they do  
- how to implement ML with only core Python  

I am still learning, so the explanations aim to be clear and beginner-friendly.

---

## 📌 What’s inside this module?
linear-regression/
│
├── linear_regression_from_scratch.py   # The implementation
├── examples/
│   └── simple_demo.py                  # How to run it
└── notes/
└── math_derivation.md              # Formulas + gradient breakdown

---

## 🧠 Summary of the Model

We are trying to fit a line:

\[
\hat{y} = mx + b
\]

We minimize Mean Squared Error using gradient descent:

\[
m := m - \alpha \frac{\partial L}{\partial m}
\]
\[
b := b - \alpha \frac{\partial L}{\partial b}
\]

Full details are in `notes/math_derivation.md`.

---

## ▶ How to Run the Example

```bash
python examples/simple_demo.py