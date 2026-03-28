
from linear_regression_from_scratch import LinearRegressionScratch

x = [1, 2, 3, 4]
y = [2, 4, 5, 4]

model = LinearRegressionScratch(0.01, 1500)
model.fit(x, y)

print("Prediction for x=10:", model.predict(10))
