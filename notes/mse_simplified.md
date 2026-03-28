Mean Squared Error (MSE) is a way to measure how wrong a machine learning model is.
It gives us a single number that represents how far off our predictions are from the real answers.
The lower the MSE, the better the model is doing.

## 1. What Problem Does MSE Solve?
When a model makes a prediction, it will usually not be perfect.
Example:

The model predicts: 10
The real answer is: 7
The error is: 3

Every prediction has its own error.
MSE gives us one number that tells us how big these errors are overall.

## 2. Why Not Just Average the Errors?
If we simply average errors, the positive and negative differences might cancel each other out.
Example:

Predict 5 instead of 10 → error = -5
Predict 15 instead of 10 → error = +5

Averaging these gives 0, even though both predictions are wrong.
This would be misleading.

## 3. How MSE Fixes This Problem
To avoid the cancellation issue, MSE:

Looks at each error
Squares it (turns negative errors into positive ones)
Averages the squared errors

This gives a single number that reflects how wrong the model is on average.

## 4. Why Square the Errors?
Squaring errors has two benefits:

All errors become positive, so they don’t cancel out.
Big mistakes get punished more than small mistakes.

For example:

Error of 1 → squared = 1
Error of 5 → squared = 25

This means MSE strongly discourages large errors, which helps the model learn better.

## 5. What Does a “Good” MSE Look Like?

MSE close to 0 means the model is making very small mistakes.
Larger MSE values mean the model is more incorrect.

There is no “perfect” number — it depends on the scale of the data.

## 6. Why MSE Works Well With Gradient Descent
MSE is smooth and forms a simple, bowl-shaped curve when plotted.
Because of this shape:

Gradient descent has a clear direction to move
There is only one minimum
The model can easily find the best parameters

This is why MSE is one of the most commonly used loss functions in machine learning.

## 7. Summary
Mean Squared Error is:

A measure of how wrong a model is
An average of squared prediction errors
Larger mistakes count more
Perfect for optimization
Easy to compute
Easy for gradient descent to follow

MSE helps the model understand how to improve itself, step by step.