
# Math Derivation — Linear Regression

This is a beginner‑friendly derivation of the gradients.

## Hypothesis

\[
\hat{y} = mx + b
\]

## Loss (MSE)

\[
L = \frac{1}{n} \sum (\hat{y} - y)^2
\]

## Gradients

\[
\frac{\partial L}{\partial m}
  = \frac{2}{n} \sum ((mx + b) - y)x
\]

\[
\frac{\partial L}{\partial b}
  = \frac{2}{n} \sum ((mx + b) - y)
\]

These tell us how to update:

\[
m := m - \alpha \frac{\partial L}{\partial m}
\]

\[
b := b - \alpha \frac{\partial L}{\partial b}
\]
